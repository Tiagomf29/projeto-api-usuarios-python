from model.User import User
from repository.UserRepository import UserRepository


class UserService:

    def buscarTodosUsuarios(self):
        repository = UserRepository()
        usuarios = repository.buscarTodosUsuarios()
        lista = []
        for user in usuarios:
            usuario = User(user[0], user[1], user[2], user[3], user[4], user[5])
            lista.append(usuario)
        
        return lista
