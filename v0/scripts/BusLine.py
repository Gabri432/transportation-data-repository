class Route:
    def __init__(self, start: str, destination: str, times: list[str]):
        self.start = start
        self.destination = destination
        self.times = times

    def __repr__(self):
        return f"From: {self.start}\nTo: {self.destination}\nTimes: {self.times}\n"


class Schedule:
    def __init__(self, period: str, routes: list[Route]):
        self.period = period
        self.routes = routes

    def __repr__(self):
        return f"Period: {self.period} \n Routes: {self.routes}\n"
    

class TimeTable:
    def __init__(self, type: str, schedules: list[Schedule]):
        self.type = type
        self.schedules = schedules

    def __repr__(self):
        return f"Table Type: {self.type}\n Table Schedule: {self.schedule}\n"


class Fare:
    def __init__(self, start: str, destination: str, price: list[str]):
        self.start = start
        self.destination = destination
        self.price = price

    def __repr__(self):
        return f"From: {self.start}\nTo: {self.destination}\nFares: {self.price}\n"


class BusLine:
    def __init__(self, number: str, cities: list[str], website: str, fares: list[Fare], time_table_types: list[TimeTable]):
        self.number = number
        self.cities = cities
        self.website = website
        self.fares = fares
        self.time_table_types = time_table_types

    def __repr__(self):
        return (
            f"Line number: {self.number}\nCities on the route: {self.cities}\n"
            f"Website: {self.website}\nFares: {self.fares}\n Time Tables: {self.time_table_types}\n")