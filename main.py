import sqlite3

conn = sqlite3.connect("lista_zakupow.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS shopping_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL
)
""")
conn.commit()


# Funkcja do zapisywania nowego elementu
def save_to_db(item_name):
    cursor.execute("INSERT INTO shopping_list (item) VALUES (?)", (item_name,))
    conn.commit()


# Funkcja do pobierania listy zakupów
def load_from_db():
    cursor.execute("SELECT item FROM shopping_list")
    return [row[0] for row in cursor.fetchall()]


# Funkcja do usuwania elementu z listy
def remove_from_db(item_name):
    cursor.execute("DELETE FROM shopping_list WHERE item = ?", (item_name,))
    conn.commit()


while True:
    try:
        option = int(
            input("Co chcesz zrobić:\n1. Wyświetl listę\n2. Dodaj do listy\n3. Usuń z listy\n4. Zapisz i wyjdź\n>> "))

        # Wyświetlanie listy
        if option == 1:
            items = load_from_db()
            if not items:
                print("Lista jest pusta.")
            else:
                print("Twoja lista zakupów:")
                for i, item in enumerate(items, start=1):
                    print(f"{i}. {item}")

        # Dodawanie do listy
        elif option == 2:
            while True:
                item = str(input("Co chcesz dodać (0 oznacza koniec)\n>> "))
                if item == "0":
                    break
                save_to_db(item)
            print("Dodano do listy!")

        # Usuwanie z listy
        elif option == 3:
            unwanted = str(input("Co chcesz usunąć\n>> "))
            remove_from_db(unwanted)
            print("Usunięto z listy!")

        elif option == 4:
            print("pa")
            break

        else:
            print("Nieprawidłowa opcja, wybierz ponownie.")
            continue

    except ValueError:
        print("Błąd wprowadzono nieprawidłową wartość. Spróboj ponownie")

conn.close()
