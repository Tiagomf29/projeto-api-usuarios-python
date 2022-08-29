import secrets

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

from service.UserService import UserService

app = FastAPI()

security = HTTPBasic()

class UserController:
    @app.get("/usuarios")
    def buscarTodosUsuarios(credentials: HTTPBasicCredentials = Depends(security)):
        current_username_bytes = credentials.username.encode("utf8")
        correct_username_bytes = b"tiago"
        is_correct_username = secrets.compare_digest(
            current_username_bytes, correct_username_bytes
        )
        current_password_bytes = credentials.password.encode("utf8")
        correct_password_bytes = b"123"
        is_correct_password = secrets.compare_digest(
            current_password_bytes, correct_password_bytes
        )
        if not (is_correct_username and is_correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        usuarios = UserService()
        return usuarios.buscarTodosUsuarios()
