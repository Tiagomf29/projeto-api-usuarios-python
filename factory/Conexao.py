import psycopg2


class Conexao:

    @staticmethod
    def conectar():
        db = psycopg2.connect(host='ec2-34-233-115-14.compute-1.amazonaws.com',
                              database='dd2b5jm5v5gpsg',
                              user='tozekvgcqqqwbz',
                              password='6948c75bb05afd43909011b3fd176e13506b31659adf5268411c460b5baebdbd')

        return db
