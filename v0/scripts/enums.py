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

class VehicleEnum(Enum):
    BUS = "bus"
    TRAM = "tram"
    TRAIN = "train"
    AIRPLANE = "airplane"