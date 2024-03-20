import psycopg2 as ps
from settings import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USER

class ConexaoFactory():
    def get_conexao(self):
        return ps.connect(host=DB_HOST, database= DB_DATABASE, user=DB_USER, password=DB_PASSWORD)
