# Projekt_5
# Vylepšený Task Manager

## Popis projektu
Jednoduchý správce úkolů napsaný v Pythonu, který využívá MySQL databázi pro ukládání úkolů. Umožňuje přidávat, zobrazovat, aktualizovat a odstraňovat úkoly s různými stavy.

## Použité technologie
- Python 3.13.2
- MySQL Server
- Knihovna mysql-connector-python pro komunikaci s MySQL
- pytest pro automatizované testování

## Požadavky
- Nainstalovaný Python 3.13.2 (doporučeno od 3.8+)
- MySQL server s vytvořenou databází `task_manager` (nebo `task_manager_test` pro testy)
- Python balíčky: `mysql-connector-python`, `pytest` (instalace přes `pip install -r requirements.txt`)

## Instalace a nastavení
1. Vytvořte databázi a tabulku pomocí přiloženého SQL skriptu `create_task_manager.sql`.
2. Upravte přihlašovací údaje k databázi ve zdrojovém kódu (`main.py`).

## Připojení k databázi

Před spuštěním programu je potřeba upravit přihlašovací údaje k databázi ve funkci `pripojeni_db()` ve zdrojovém kódu (soubor `main.py`).  
Musíte nastavit správně tyto proměnné podle vaší databáze:

- `host` — například `"localhost"`  
- `user` — uživatelské jméno pro přístup k MySQL  
- `password` — heslo k uživatelskému účtu  
- `database` — název databáze (např. `"task_manager"`)

Pokud některá z těchto hodnot nebude správná nebo databáze neexistuje, program se nepřipojí a vypíše chybovou zprávu.

---

Příklad úpravy ve funkci `pripojeni_db()`:

```python
def pripojeni_db():
    try:
        spojeni = mysql.connector.connect(
            host="localhost",         # upravte podle vaší DB
            user="root",              # upravte podle vaší DB
            password="vase_heslo",    # upravte podle vaší DB
            database="task_manager"   # upravte podle vaší DB
        )
        return spojeni
    except mysql.connector.Error as err:
        print(f"Chyba připojení k DB: {err}")
        exit(1)

