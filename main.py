
# Připojení k databázi
import mysql.connector

def pripojit_db():
    try:
        spojeni = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",  # případně doplň heslo
            database="task_manager"
        )
        return spojeni
    except mysql.connector.Error as chyba:
        print(f"Chyba při připojení k databázi: {chyba}")
        return None


# Přidání úkolu
def pridat_ukol(conn):
    nazev = input("Zadej název úkolu: ").strip()
    popis = input("Zadej popis úkolu: ").strip()
    if not nazev or not popis:
        print("Název i popis musí být vyplněny.")
        return
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ukoly (nazev, popis, stav) VALUES (%s, %s, %s)",
                   (nazev, popis, "Nezahájeno"))
    conn.commit()
    print("Úkol byl přidán.")

# Pouze zobrazení úkolů
def zobrazit_ukoly(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, nazev, popis, stav FROM ukoly WHERE stav IN ('Nezahájeno', 'Probíhá')")
    ukoly = cursor.fetchall()

    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")
    for u in ukoly:
        print(f"ID: {u[0]}, Název: {u[1]}, Popis: {u[2]}, Stav: {u[3]}")

# Aktualizace úkolu – název, popis nebo stav
def aktualizovat_ukol(conn):
    cursor = conn.cursor()
    while True:
        cursor.execute("SELECT id, nazev, stav FROM ukoly")
        ukoly = cursor.fetchall()
        if not ukoly:
            print("Žádné úkoly k aktualizaci.")
            return

        print("\nDostupné úkoly:")
        for u in ukoly:
            print(f"ID: {u[0]}, Název: {u[1]}, Stav: {u[2]}")

        id_input = input("Zadejte ID úkolu k aktualizaci (nebo Enter pro návrat): ").strip()
        if id_input == "":
            return

        if not id_input.isdigit():
            print("Zadejte prosím číslo.")
            continue

        id_ukolu = int(id_input)
        cursor.execute("SELECT id FROM ukoly WHERE id=%s", (id_ukolu,))
        if cursor.fetchone() is None:
            print("Úkol s tímto ID neexistuje.")
            continue

        while True:
            print("\nVyberte, co chcete aktualizovat:")
            print("1. Změnit název")
            print("2. Změnit popis")
            print("3. Změnit stav")
            print("0. Ukončit aktualizaci")

            volba = input("Vaše volba: ").strip()

            if volba == "1":
                novy_nazev = input("Zadejte nový název: ").strip()
                if novy_nazev:
                    cursor.execute("UPDATE ukoly SET nazev=%s WHERE id=%s", (novy_nazev, id_ukolu))
                    conn.commit()
                    print("Název úkolu byl aktualizován.")
                else:
                    print("Název nemůže být prázdný.")
            elif volba == "2":
                novy_popis = input("Zadejte nový popis: ").strip()
                if novy_popis:
                    cursor.execute("UPDATE ukoly SET popis=%s WHERE id=%s", (novy_popis, id_ukolu))
                    conn.commit()
                    print("Popis úkolu byl aktualizován.")
                else:
                    print("Popis nemůže být prázdný.")
            elif volba == "3":
                while True:
                    print("\nVyberte nový stav úkolu:")
                    print("1. Probíhá")
                    print("2. Hotovo")
                    print("Stiskněte Enter pro návrat zpět bez změny stavu.")
                    stav_volba = input("Vaše volba (1/2): ").strip()
                    if stav_volba == "":
                        # návrat zpět do hlavní nabídky aktualizace
                        break
                    elif stav_volba == "1":
                        novy_stav = "Probíhá"
                        cursor.execute("UPDATE ukoly SET stav=%s WHERE id=%s", (novy_stav, id_ukolu))
                        conn.commit()
                        print("Stav úkolu byl aktualizován.")
                        break
                    elif stav_volba == "2":
                        novy_stav = "Hotovo"
                        cursor.execute("UPDATE ukoly SET stav=%s WHERE id=%s", (novy_stav, id_ukolu))
                        conn.commit()
                        print("Stav úkolu byl aktualizován.")
                        break
                    else:
                        print("Neplatná volba, zvolte 1, 2 nebo Enter pro návrat.")
            elif volba == "0":
                print("Ukončuji aktualizaci.")
                return
            else:
                print("Neplatná volba, zkuste to znovu.")


# Smazání úkolu
def smazat_ukol(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, nazev FROM ukoly")
    ukoly = cursor.fetchall()

    if not ukoly:
        print("Žádné úkoly k odstranění.")
        return

    print("\nDostupné úkoly:")
    for u in ukoly:
        print(f"ID: {u[0]}, Název: {u[1]}")

    try:
        id_ukolu = int(input("Zadej ID úkolu k odstranění: "))
    except ValueError:
        print("Neplatné ID.")
        return

    cursor.execute("DELETE FROM ukoly WHERE id = %s", (id_ukolu,))
    conn.commit()
    print("Úkol byl odstraněn.")

# Hlavní menu
def hlavni_menu(conn):
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Aktualizovat úkol")
        print("4. Smazat úkol")
        print("5. Konec")

        volba = input("Zadej volbu: ")

        if volba == "1":
            pridat_ukol(conn)
        elif volba == "2":
            zobrazit_ukoly(conn)
        elif volba == "3":
            aktualizovat_ukol(conn)
        elif volba == "4":
            smazat_ukol(conn)
        elif volba == "5":
            print("Ukončuji program...")
            break
        else:
            print("Neplatná volba.")

# Spuštění programu
if __name__ == "__main__":
    conn = pripojit_db()
    hlavni_menu(conn)
    conn.close()
