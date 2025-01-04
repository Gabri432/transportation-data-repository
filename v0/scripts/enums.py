from enum import Enum

class PeriodEnum(Enum):
    WEEKDAYS = "weekdays"
    SATURDAYS = "saturdays"
    HOLIDAYS = "holidays"


class CityEnum(Enum):
    MILAN = "Milan"
    VILLANTERIO = "Villanterio"
    LODI = "Lodi"
    PAVIA = "Pavia"