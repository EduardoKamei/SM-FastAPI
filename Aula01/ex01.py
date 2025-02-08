from fastapi import FastAPI

#Exercício 01 - Olá Mundo!
app = FastAPI(title='Olá Mundo!')

@app.get('/')
def ola_mundo():
    return {
        'message': 'Olá Mundo!'
    }
