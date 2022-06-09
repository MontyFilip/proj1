import menu

# zla nazwa funkcji - wbudowana funkcja - przyslania list


def menu_list():
    menu_string = {
        1: 'Dodaj wydarzenie',
        2: 'Wypisz wydarzenia',
        3: 'Wypisz wydarzena w formacie iCalendar',
        4: 'Zamknij program'
    }
    for i in menu_string:
        print(f'{i}. {menu_string[i]}')


def main():
    calendar = menu.Calendar()
    # słownik zawierający wywołania odpowiednich klas i metod
    commands = {
        1: menu.AddNewCommand(calendar),
        2: menu.ListCommand(calendar),
        3: menu.ListICalendarCommand(calendar),
        4: menu.ExitCommand()
    }

    while True:
        menu_list()
        # pobranie wyboru od użytkownika wraz ze sprawdzeniem poprawności
        try:
            selected = int(input('\nSelect menu item 1-4: '))
            commands[selected].execute()
        except ValueError:
            print('Błędny wybór.')


if __name__ == '__main__':
    main()
