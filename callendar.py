# wypisanie danych
from asyncio import events


text_entry = """
BEGIN: VCALENDAR
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Warsaw
X-LIC-LOCATION: Europe/Warsaw
END:TIMEZONE"""
text_end = """END:VCALENDAR"""



def list_calendar(strategy, events):
    formated_data = strategy.format(events)
    print(formated_data)

#abstractClass - https://docs.python.org/3/library/abc.html
class ListingStrategy:
    def format(self, calendar_data):
        pass

# formatowanie wydarzeń do klasycznego formatu

#okropne formatowanie - mozna uzyc fstringa, nie mieszamy
class SimpleListingStrategy(ListingStrategy):
    def format(self, calendar_data):
        data = "".join([self.format_event(event) for event in calendar_data])
        return "    --wydarzenia:-- {}".format(data)

    def format_event(self, event):
        return"""
Tytuł: {}
Date: {}, {}""".format(event.title,
                       event.date.strftime('%d.%m.%Y'),
                       event.time.strftime('%H:%M'))


# formatowanie wydarzeń do formatu iCalendar


#stringi jako constant albo na gore pliku, albo do innego pliku - nie mieszaj bo wyglada zle
#anotowanie typow - brak w calej apce 
class ICalListingStrategy(ListingStrategy):
    def format(self, calendar_data):
        data = "".join([self.format_event(event) for event in calendar_data])
        return "    --iCalendar format-- {}".format(data)

    def format_event(self, event):
        dt = "{}T{}00".format(
            # convert z obj date na string
            event.date.strftime("%Y%m%d"),
            # convert z obj time na string
            event.time.strftime("%H%M")
        )
        return """{}
BEGIN:VEVENT
DTSTART:{}
DTEND:{}
SUMMARY:{}
END:VEVENT
{}""".format(text_entry, dt, dt, event.title, text_end)
