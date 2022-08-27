from fastapi import FastAPI

from service.UserService import UserService

app = FastAPI()

@app.get("/usuarios")
def buscarTodosUsuarios():
    usuarios = UserService()
    return usuarios.buscarTodosUsuarios()
