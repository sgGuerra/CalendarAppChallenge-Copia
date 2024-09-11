from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here
@dataclass
class Reminder:
    EMAIL = 'email'
    SYSTEM = 'system'
    date_time: datetime
    type: str = EMAIL

    def __str__(self) -> str:
        return f"Reminder on {self.date_time} of type {self.type}"


# TODO: Implement Event class here
@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    reminders: list[Reminder] = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_reminder(self, date_time: datetime, type: str):
        new_reminder = Reminder(date_time, type)
        self.reminders.append(new_reminder)

    def delete_reminder(self, reminder_index: int):
        if 0 <= reminder_index < len(self.reminders):
            del self.reminders[reminder_index]
        else:
            reminder_not_found_error()

    def __str__(self) -> str:
        return (f"ID: {self.id}"
                f"\nEvent title: {self.title} "
                f"\nDescription: {self.description} "
                f"\nTime: {self.start_at} - {self.end_at}")

# TODO: Implement Day class here


# TODO: Implement Calendar class here
