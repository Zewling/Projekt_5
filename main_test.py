"""
main_test.py: Čtvrtý projekt do Engeto Akademie Tester s Pythonem

author: Josef Věrovský
email: pepa.verovsky@seznam.cz / josef.verovsky@outlook.com
"""

import pytest
import mysql.connector
from main import pridat_ukol, aktualizovat_ukol, smazat_ukol

@pytest.fixture(scope="module")
def conn():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1111",  
        database="task_manager_test"
    )
    yield connection
    connection.close()

@pytest.fixture(autouse=True)
def clean_table(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ukoly")
    cursor.execute("ALTER TABLE ukoly AUTO_INCREMENT = 1")
    conn.commit()
    yield
    cursor.execute("DELETE FROM ukoly")
    cursor.execute("ALTER TABLE ukoly AUTO_INCREMENT = 1")
    conn.commit()


def test_pridat_ukol_pozitiv(conn, monkeypatch):
    inputs = iter(["Test úkol", "Popis testu"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    pridat_ukol(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ukoly WHERE nazev='Test úkol'")
    assert cursor.fetchone()[0] == 1

def test_pridat_ukol_negativ(conn, monkeypatch):
    inputs = iter(["", "Popis testu", "Název", ""])  # první název prázdný, pak popis prázdný
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Voláme dvakrát, vždy by nemělo dojít k vložení kvůli prázdnému vstupu
    pridat_ukol(conn)
    pridat_ukol(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ukoly")
    assert cursor.fetchone()[0] == 0

def test_aktualizovat_ukol_pozitiv(conn, monkeypatch):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ukoly (nazev, popis, stav) VALUES ('Úkol', 'Popis', 'Nezahájeno')")
    conn.commit()

    inputs = iter([
        "1",      # ID úkolu
        "1",      # změna názvu
        "Nový název",
        "2",      # změna popisu
        "Nový popis",
        "3",      # změna stavu
        "2",      # vybrat "Hotovo"
        "0"       # ukončit aktualizaci
    ])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    aktualizovat_ukol(conn)

    cursor.execute("SELECT nazev, popis, stav FROM ukoly WHERE id=1")
    nazev, popis, stav = cursor.fetchone()

    assert nazev == "Nový název"
    assert popis == "Nový popis"
    assert stav == "Hotovo"

def test_aktualizovat_ukol_negativ(conn, monkeypatch):
    inputs = iter([
        "999",  # neexistující ID
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    aktualizovat_ukol(conn)  # mělo by vypsat, že úkol neexistuje, ale nic měnit nebude
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ukoly")
    assert cursor.fetchone()[0] == 0

def test_smazat_ukol_pozitiv(conn, monkeypatch):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ukoly (nazev, popis, stav) VALUES ('Úkol', 'Popis', 'Nezahájeno')")
    conn.commit()
    inputs = iter(["1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    smazat_ukol(conn)
    cursor.execute("SELECT COUNT(*) FROM ukoly")
    assert cursor.fetchone()[0] == 0

def test_smazat_ukol_negativ(conn, monkeypatch):
    inputs = iter(["999"])  # neexistující ID
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    smazat_ukol(conn)  # mělo by vypsat chybu, ale nesmazat nic
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ukoly")
    assert cursor.fetchone()[0] == 0
