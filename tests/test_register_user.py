import unittest
from unittest.mock import patch
from main import register_user
from modules import User


class TestRegisterUser(unittest.TestCase):
    # dekoratoiumi pakeiciam funkcija input(), sukuriam 'mock_input'(laisvas pavadinimas) galima nustatyti reikiamus ivedimo parametrus
    @patch("builtins.input")
    # dekoratorius naudojamas pakeisti klase 'SqliteDatabase', kad nenaudoti realia baze, sukuriam 'mock_databaze'(laisvas pavadinimas) kuria naudosime vietoje "SqliteDatabase"
    @patch("database.SqliteDatabase")
    def test_register_user(self, mock_database, mock_input):
        # naudojama nustatyti grąžinamąją reikšmę "return value" parametre
        mock_database.get_user_by_email.return_value = User(
            id=1, name="a", surname="b", email="c", password="d"
        )
        # Čia 'side_effect' yra sąrašas reikšmių, kurios bus grąžinamos paeiliui kiekvieną kartą, kai input() yra kviečiamas
        mock_input.side_effect = ["a", "b", "c", "d"]

        # Kodas 'user = register_user(mock_database)' yra kvietimas į 'register_user' funkciją, perduodant mock_database objektą kaip argumentą.
        user = register_user(mock_database)
        # šioje vietoje tikrinama, ar vartotojo objekto (user) name atributas yra lygus "a". Jei tai atitinka tikimybę, testas bus sėkmingas.
        assert user.name == "a"
        assert user.surname == "b"
        # tikrinimas, ar metodas create_user buvo iškvietas tik vieną kartą per testą. Tai yra dalis testavimo scenarijaus, kuriuo patikrinama, ar create_user metodas yra teisingai naudojamas.
        assert mock_database.create_user.call_count == 1
        # tikrina, ar create_user metodo kvietimo parametrai (kwargs) yra lygūs nurodytiems reikšmėms. Čia yra tikrinama, ar create_user metodo iškvietimo metu buvo perduoti teisingi parametrai, t.y., ar name yra "a", surname yra "b", email yra "c" ir password yra "d".
        assert mock_database.create_user.call_args.kwargs == {
            "name": "a",
            "surname": "b",
            "email": "c",
            "password": "d",
        }
        # teiginys, kuris tikrina, ar get_user_by_email metodo iškvietimas buvo atliktas tik vieną kartą. Tai patikrina, ar call_count atributas, kuris laikomas Mock objekte, yra lygus 1.
        assert mock_database.get_user_by_email.call_count == 1
        # tikrina, ar get_user_by_email metodo iškvietimo pirmasis argumentas (args[0]) yra lygus "c". Tai reiškia, kad tikrinama, ar metodo iškvietimo metu buvo perduotas teisingas pirmasis argumentas, t.y., ar email yra "c"
        assert mock_database.get_user_by_email.call_args.args[0] == "c"


if __name__ == "__main__":
    unittest.main()


# testas paleidziamas is terminalo:
# py -m unittest tests/test_register_user.py -v
