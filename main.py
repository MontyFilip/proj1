from menu import *


def main():
    calendar = Calendar()
    commands = {
        1: AddNewCommand(calendar),
        2: ListCommand(calendar),
        3: ListICalendarCommand(calendar),
        4: ExitCommand()
    }

    while True:
        print("""
    1. Dodaj wydarzenie
    2. Wypisz wydarzenia
    3. Wypisz wydarzenia w formacie iCalendar
    4. Zamknij program
        """)

# poranie wybory od użytkownika
        try:
            selected = int(input("Select menu item 1-4: "))
            commands[selected].execute()
        except ValueError:
            print("Błędny wybór.")


if __name__ == '__main__':
    main()
