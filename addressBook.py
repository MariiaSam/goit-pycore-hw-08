from collections import UserDict
from datetime import datetime, timedelta
# import calendar // if use Saturday and Sunday

from record import Record


class AddressBook(UserDict):

    def __str__(self):
        lines = [str(record) for record in self.data.values()]
        return '\n'.join(lines)

    def add_record(self, record: Record):
        if record.name.value in self.data:
            raise KeyError(
                f"Record with name {record.name.value} already exists")
        else:
            self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name not in self.data:
            raise KeyError(f"Record with name {name} not found")
        else:
            del self.data[name]

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        current_day = datetime.today().date()

        for name, record in self.data.items():
            if record.birthday:
                birthday = record.birthday.value.date()
                birthday_current_year = birthday.replace(year=current_day.year)

                next_week = current_day + timedelta(days=7)
                if current_day <= birthday_current_year <= next_week:

                    # calendar
                    # if birthday_current_year.weekday() in (calendar.SATURDAY, calendar.SUNDAY):
                    #      while birthday_current_year.weekday() != calendar.MONDAY:

                    if birthday_current_year.weekday() == 5:
                        birthday_current_year += timedelta(days=2)
                    elif birthday_current_year.weekday() == 6:
                        birthday_current_year += timedelta(days=1)

                    upcoming_birthdays.append(
                        {"name": name, "birthday_date":  birthday_current_year.strftime('%d.%m.%Y')})

        return upcoming_birthdays
