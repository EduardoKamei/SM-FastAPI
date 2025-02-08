from fastapi import FastAPI


# Criando Instância da nossa API
app = FastAPI(title="API Sorteio", description="Api para gerenciar sorteios")

# Lista de Participantes
participants = []


# O @ é um decorador coloca uma função sobre outra função
@app.get("/info")
def info():
    return {"title": app.title, "description": app.description}


# Definindo o endpoint para buscar todos os participantes.
@app.get("/sorteio/participantes")
def get_all_participants(search: str | None = None):
    results = []

    if search is not None:
        for name in participants:
            if search.lower() in name.lower():
                results.append(name)
    else:
        results.extend(participants)

    return participants


@app.post("/sorteio/{name}/adicionar")
def add_new_participant(name: str):
    participants.append(name)
    return {"message": "Participante adicionado com sucesso."}
