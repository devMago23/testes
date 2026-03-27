from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from sqlalchemy import select

from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB, UserList

from fast_zero.database import get_Section
from fast_zero.models import UserModel



app = FastAPI(title='API ZERO')

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olá mundo'}


# cria um usúario
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session=Depends(get_Section)):
#   session= get_Section()
  db_user = session.scalar(
      select(UserModel).where((UserModel.username == user.username) | (UserModel.email == user.email))
  )
  if  db_user:
      if db_user.username == user.username:
       raise HTTPException(
           detail='username already exists',
           status_code=HTTPStatus.CONFLICT
       )
      elif db_user.email == user.email:
        raise HTTPException(
           detail='email already exists',
           status_code=HTTPStatus.CONFLICT
       )
  db_user=UserModel(
      username=user.username,
      email=user.email,
      password=user.password
  )     
  
  session.add(db_user)
  session.commit()
  session.refresh(db_user)
  return db_user
      

# @app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
# def create_user(user: UserSchema):
#     user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
#     database.append(user_with_id)
#     return user_with_id
# recupera todos os usúarios
@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_Users(session: Session= Depends(get_Section)):
    users= session.scalars(select(UserModel))
    return users


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_User(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    database[user_id - 1] = user_with_id
    return user_with_id


# @app.delete(
#     '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
# )
# def delete_user(user_id: int):
#     if not user_id:
#         raise HTTPException(
#             status_code=HTTPStatus.NOT_FOUND, detail='User not found'
#         )
    
#     del  database[user_id - 1]
#     return {'message': 'User deleted'}
   

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    
    return database.pop(user_id - 1),'message User deleted'

@app.get('/hellow', response_class=HTMLResponse)
def create_template():
    return """

    <html>
     <head>
     <style>
      h1{
          text-align:center;
          margin-top:20px;
          font-weigth:bold;
          color:#333;
      }
     </style>
       <title>meu mundo</title>
     </head>
     <body>
       <h1>Olá mundo</h1>
     </body>
    </html>
    """
