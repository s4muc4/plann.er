import sqlite3
from sqlite3 import Connection

class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string =  "storage.db"
        self.__conn = None

    def connect(self) -> None: ##Significa que nao vai retornar nada
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)#Para usar essa conexao em varios lugares
        self.__conn = conn

    def get_connection(self) -> Connection:
        return self.__conn
db_connection_handler = DbConnectionHandler()