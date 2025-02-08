from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#Exercício 02 - É um Site? (Sim)
app = FastAPI(title='Meu site API.')

@app.get('/home')
def site():
    return HTMLResponse('<h1> Título do meu site API </h1>')