from callendar import SimpleListingStrategy, ICalListingStrategy, list_calendar
from dataclasses import dataclass
from abc import ABC, abstractmethod
import datetime
from time import sleep as sleep_soft
import re


class Calendar:
    def __init__(self) -> None:
        self.events = []

    def add_event(self, event):
        self.events.append(event)

# klasa formatująca parametry obiektu


@dataclass
class Event:
    title: str
    date: datetime.date
    time: datetime.time


class MenuCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

# klasa zakańczająca działanie programu


class ExitCommand(MenuCommand):
    def execute(self):
        print("Bye!")
        exit(0)


# dodawanie nowego wydarzenia


class AddNewCommand(MenuCommand):
    def __init__(self, calendar) -> None:
        self.calendar = calendar

    def execute(self):
        # tutaj while do poprawy - na kazdym inpucie ze sprawdzeniem
        try:
            pattern = '^[a-zA-Z0-9\-\,\.\s]+$'
            # if not re.compile(pattern).match(title):
            title = input("\nPodaj tytuł wydarzenia: ")
        #  ^ pocz zdania,  [przedział z jakiego znaki  mogą się znajdować]
        # + dowolna ilosć powtórzeń (sprawdzenie każdego kolejnego znkau) $ - koniec linii
            if not re.compile(pattern).match(title):
                # invalid characters
                raise Exception("title not match")
            self.calendar.add_event(
                Event(title=title,
                      # convert na obj datetime.date
                      date=datetime.datetime.strptime(
                          input('Podaj datę wydarzenia(DD.MM.YYYY): '), '%d.%m.%Y').date(),
                      #  convert na obj datetime.time
                      time=datetime.datetime.strptime(
                          input('Podaj godzinę wydarzenia(HH:MM): '), '%H:%M').time()
                      )
            )
            # komunikat o poprawnym dodaniu wydarzenia oraz uśpienie programu
            print("\nWydarzenie zostało dodane\n")
            sleep_soft(.5)
        # wyjątek w przypadku błędnych danch
        # reaguje na tytuł, datę i godzinę
        except Exception as e:
            print("\nInvalid Input\n")
            # print(e)

# wywołanie wypisania wydarzeń


class ListCommand(MenuCommand):

    def __init__(self, calendar) -> None:
        self.strategy = SimpleListingStrategy()
        self.calendar = calendar

    def execute(self):
        list_calendar(self.strategy, self.calendar.events)

# wywołanie wypisania wydarzeń w formacie iCalendar


class ListICalendarCommand(MenuCommand):

    def __init__(self, calendar) -> None:
        self.strategy = ICalListingStrategy()
        self.calendar = calendar

    def execute(self):
        list_calendar(self.strategy, self.calendar.events)
