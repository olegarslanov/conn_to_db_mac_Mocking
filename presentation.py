from database import Database, SqliteDatabase
from modules import User, Todo, Base
from welcome import welcome
from sqlalchemy.orm.decl_api import DeclarativeMeta

class App:
    def __init__(self, db_conn: Database) -> None:
        self.db_conn = db_conn
        self.db_conn.create_detabase()
    
    def run(self)-> None:
        welcome()
        self.print_options()
        self.get_option()
        if self.get_option == 1:
            name, surname, email, password = self.get_login_credential()
            self.db_conn.create_user(name=name, surname=surname, email=email, password=password)
        if self.get_option == 2:

    @staticmethod
    def print_options()-> None:
        print("\n1- Register account \n2- Login \n3- Exit")

    @staticmethod
    def get_option() -> int:
        option = int(input("Please choose your action: "))
        return option
    
    @staticmethod
    def get_user_credential()-> str:
        name = input("Please define your name: ")
        surname = input("Please define surname: ")
        email = input("Please define email: ")
        password = input("Please define password: ")
        return name, surname, email, password
    
    def create_user(self, name: str, surname: str, email: str, password: str) -> None:
        self.db_conn.create_user(name=name, surname=surname, email=email, password=password)

    def get_login_credential()-> None:
        pass


app = App(SqliteDatabase("test.db", Base))
