from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

pessoas:list[object] = []


class PessoaIn(BaseModel):
    nome:str
    idade:int
    altura:float

class MessageOut(BaseModel):
    message:str

@app.get("/pessoas/")
def get_all_peoples(search:str |None = None):
    results =  []
    if search is not None:
        for pessoa in pessoas:
            print(search)

            if search.lower() in pessoa["nome"].lower():
                print(pessoa.get("nome"))
                print(pessoa["nome"])
                results.append(pessoa)
        return results
    return pessoas


@app.post("/pessoas/")
def create_new_people(pessoa:PessoaIn):
    pessoas.append(pessoa.model_dump())
    return MessageOut(message="Pessoa cadastrada com sucesso !")