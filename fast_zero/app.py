from http import HTTPStatus

from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB, UserList


app = FastAPI(title='API ZERO')

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olá mundo'}

# cria um usúario 
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id

# recupera todos os usúarios 
@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_Users():
    return {'users': database}

@app.put('/users/{user_id}',
         status_code=HTTPStatus.OK,
         response_model=UserPublic)
def update_User(user_id:int, user: UserSchema):
     user_with_id = UserDB(**user.model_dump(), id=user_id)
     if user_id < 1 or user_id > len(database):
       raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='user not fould!...')
     database[user_id-1]= user_with_id
     return user_with_id
 
@app.delete('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def delete_user(user_id: int):
    return  database.pop(user_id -1)
# @app.get('/hellow', response_class=HTMLResponse)
# def create_template():
#     return """

#     <html>
#      <head>
#      <style>
#       h1{
#           text-align:center;
#           margin-top:20px;
#           font-weigth:bold;
#           color:#333;
#       }
#      </style>
#        <title>meu mundo</title>
#      </head>
#      <body>
#        <h1>Olá mundo</h1>
#      </body>
#     </html>
#     """
