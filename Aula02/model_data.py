from fastapi import FastAPI
from pydantic import BaseModel

class Messageout(BaseModel):
    message: str

# Criando nosso Modelo "Animal" que 
# está herdando da classe BaseModel
class AnimalIn(BaseModel):
    name: str | None = None
    type: str | None = None
    color: str | None = None

#Classe
app = FastAPI()

#lista de todos animais.
animals = []

#consulta os todos animais casatrados.
@app.get('/animal')
def get_all_animals():
    return animals

#cadastra um animal.
@app.post('/animal')
def create_new_animal(animal: AnimalIn):
    animals.append(animal.model_dump())
    return {'message': 'Animal Cadastrador com Sucesso.'}
