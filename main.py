import json

# Plik, w którym przechowujemy listę
file_name = "lista_zakupow.json"


# Funkcja do zapisywania listy do pliku
def save_to_file(items):
    with open(file_name, "w") as file:
        json.dump(items, file)


# Funkcja do odczytywania listy z pliku
def load_from_file():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Błąd: Plik jest uszkodzony. Tworzę nową, pustą listę.")
        return []


items = load_from_file()

print("Lista zakupów")
while True:
    try:
        option = int(input("Co chcesz zrobić:\n1. Wyświetl listę\n2. Dodaj do listy\n3. Usuń z listy\n4. Zapisz i wyjdź\n>> "))

        # Wyświetlanie listy
        if option == 1:
            if not items:
                print("Lista jest pusta.")
            else:
                print("Twoja lista zakupów:")
                for i, thing in enumerate(items, start=1):
                    print(f"{i}, {thing}")

        # Dodawanie do listy
        elif option == 2:
            while True:
                thing = str(input("Co chcesz dodać (0 oznacza koniec)\n>> "))
                if thing == "0":
                    break
                items.append(thing)
            save_to_file(items)

        # Usuwanie z listy
        elif option == 3:
            unwanted = str(input("Co chcesz usunąć\n>> "))
            if unwanted in items:
                items.remove(unwanted)
                save_to_file(items)
            else:
                print("Nie znaleziono elementu na liście")

        elif option == 4:
            print("pa")
            break

        else:
            print("Nieprawidłowa opcja, wybierz ponownie.")
            continue

    except ValueError:
        print("Błąd wprowadzono nieprawidłową wartość. Spróboj ponownie")
