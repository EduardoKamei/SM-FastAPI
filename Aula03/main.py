#https://davi-lucciola.notion.site/Aula-03-Arquitetura-REST-CRUD-1807b0fd58088082ac3ef7a804e9ea1d
# main.py
import db
from fastapi import FastAPI, HTTPException, status
from models import User
from schemas import MessageOut, UserIn, UserOut


app = FastAPI()


# Read
@app.get('/users')
def get_all_users() -> list[UserOut]:
    ... # Código Anterior

# Create    
@app.post('/users')
def create_new_user(user: UserIn) -> MessageOut:
    # Busca o usuário pelo email
    exist_user = db.get_by_email(user.email)
    
    # Se for encontrado um resultado, significa que já há um usuário com esse email
    # Então, lança uma exception para retornar o status code 400 (Bad Request)
    if exist_user is not None:
        raise HTTPException(
            detail='Já existe um usuário cadastrado com esse email.',
            status_code=status.HTTP_400_BAD_REQUEST
        )

    new_user = User(**user.model_dump())
    db.create_new_user(new_user)
    return MessageOut(message='Usuário cadastrado com sucesso.')