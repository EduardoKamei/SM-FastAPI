""" # main.py
from fastapi import FastAPI

# Criando Instância da nossa API
app = FastAPI(title='Hello FastAPI')

# Definindo a Rota Raiz
@app.get('/')
def hello_world():
		# Retornando um JSON
    return {
        'message': 'Hello World!'
    }

# Retornando um Texto
@app.get('/text')
def endpoint_text():
	return 'Retornando um Texto Plano'

# Retornando um JSON
@app.get('/json')
def endpoint_json():
	return {'message': 'Aqui temos um JSON'} """

from fastapi import FastAPI, status
from fastapi.responses import Response, JSONResponse


lista = []
app = FastAPI()


@app.get('/')
def listar_todos():
    if len(lista) == 0:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    return JSONResponse(content=lista, status_code=status.HTTP_200_OK)