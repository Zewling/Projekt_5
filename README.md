# Projekt_5
# Vylepšený Task Manager

## Popis projektu
Jednoduchý správce úkolů napsaný v Pythonu, který využívá MySQL databázi pro ukládání úkolů. Umožňuje přidávat, zobrazovat, aktualizovat a odstraňovat úkoly s různými stavy.

## Použité technologie
- Python 3.x
- MySQL Server
- Knihovna mysql-connector-python pro komunikaci s MySQL
- pytest pro automatizované testování

## Požadavky
- Nainstalovaný Python 3 (doporučeno 3.8+)
- MySQL server s vytvořenou databází `task_manager` (nebo `task_manager_test` pro testy)
- Python balíčky: `mysql-connector-python`, `pytest` (instalace přes `pip install -r requirements.txt`)

## Instalace a nastavení
1. Vytvořte databázi a tabulku pomocí přiloženého SQL skriptu `create_task_manager.sql`.
2. Upravte přihlašovací údaje k databázi ve zdrojovém kódu (`main_taskman.py`).
3. Nainstalujte závislosti:  
