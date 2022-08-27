from fastapi import FastAPI
from service.UserService import UserService

app = FastAPI()


class UserController:
    @app.get("/usuarios")
    def buscarTodosUsuarios():
        usuarios = UserService()
        return usuarios.buscarTodosUsuarios()
