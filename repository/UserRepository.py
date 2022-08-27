from factory.Conexao import Conexao


class UserRepository:

    def buscarTodosUsuarios(self):
        con = Conexao.conectar()
        cursor = con.cursor()
        cursor.execute("select * from users")
        return cursor.fetchall()



