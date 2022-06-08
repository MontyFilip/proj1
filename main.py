from menu import *


def list():
    menu_string ={
    1: "Dodaj wydarzenie",
    2: "Wypisz wydarzenia",
    3: "Wypisz wydarzenia w formacie iCalendar",
    4: "Zamknij program"
    }
    for i in menu_string:
        print(f'{i}. {menu_string[i]}')


def main():
    calendar = Calendar()
    # słownik zawirający wywołania odpowiednich klas i metod
    commands = {
        1: AddNewCommand(calendar),
        2: ListCommand(calendar),
        3: ListICalendarCommand(calendar),
        4: ExitCommand()
    }

    while True:            
        list()
        # pobranie wyboru od użytkownika wraz ze sprawdzeniem poprawności
        try:
            selected = int(input("Select menu item 1-4: "))
            commands[selected].execute()
        except ValueError:
            print("Błędny wybór.")


if __name__ == '__main__':
    main()
