from enum import Enum

class PeriodEnum(Enum):
    WEEKDAYS = "weekdays"
    SATURDAYS = "saturdays"
    HOLIDAYS = "holidays"


class CityEnum(Enum):
    CITY_1 = "City_1"
    CITY_2 = "City_2"
    CITY_3 = "City_3"
    CITY_4 = "City_4"

class VehicleEnum(Enum):
    BUS = "bus"
    TRAM = "tram"
    TRAIN = "train"
    AIRPLANE = "airplane"
    SHIP = "ship"
    TAXI = "taxi"