from models import User
from tinydb import TinyDB, Query


db = TinyDB('./database.json', indent=2)


def get_all_users() -> list[User]:
    ... # Codigo Anterior

# Nova função para buscar usuário pelo email
def get_by_email(email: str) -> User | None:
    # Query Object do TinyDB para fazer pesquisa
    QUser = Query()
    # Pesquisando se existe algum usuário com o email informado, retorna uma lista
    result = db.table('users').search(QUser.email == email)
    
    # Se a lista estiver vazia, retorna None
    if len(result) == 0:
        return None
    
    # Se não, pega o primeiro valor (já que o email é para ser unico) e retorna um usuário.
    return User(**result[0])


def create_new_user(user: User) -> None:
    user_document = user.model_dump()
    user_document.update({
        'id': str(user.id),
        'created_at': user.created_at.isoformat()
    })
    db.table('users').insert(user_document)