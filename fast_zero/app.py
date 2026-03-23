from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI(title="API ZERO")


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olá mundo'}

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
