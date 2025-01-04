class Route(object):
    def __init__(self, start: str, destination: str, times: list[str]):
        self.start = start
        self.destination = destination
        self.times = times

    def __str__(self):
        strings = ", ".join(self.times)
        return f"Route: {self.start} --> {self.destination}\nBus times departing from {self.start}: \t{strings}\n\n"

    def __repr__(self):
        return f"Route start: {self.start}\nRoute destination: {self.destination}\nRoute bus times: {self.times}\n\n"


class Schedule(object):
    def __init__(self, period: str, routes: list[Route]):
        self.period = period
        self.routes = routes
    
    def __str__(self):
        strings = "".join(str(Route(obj["start"], obj["destination"], obj["times"])) for obj in self.routes)
        return f"Period: {self.period}\nRoutes: {strings}"

    def __repr__(self):
        return f"Period: {self.period} \n Routes: {self.routes}\n"
    

class TimeTable:
    def __init__(self, type: str, schedules: list[Schedule]):
        self.type = type
        self.schedules = schedules
    
    def __str__(self):
        strings = "".join(str(Schedule(obj["period"], obj["routes"])) for obj in self.schedules)
        return f"Type: {self.type}\nSchedules: {strings}\n"

    def __repr__(self):
        return f"Table Type: {self.type}\n Table Schedule: {self.schedules}\n"


class Fare:
    def __init__(self, start: str, destination: str, price: str):
        self.start = start
        self.destination = destination
        self.price = price

    def __str__(self):
        return f"Bus line: {self.start} --> {self.destination}\nPrice: {self.price}\n"

    def __repr__(self):
        return f"Start: {self.start}\nDestination: {self.destination}\nPrice: {self.price}\n"


class BusLine:
    def __init__(self, number: str, cities: list[str], website: str, fares: list[Fare], time_table_types: list[TimeTable]):
        self.number = number
        self.cities = cities
        self.website = website
        self.fares = fares
        self.time_table_types = time_table_types

    def __str__(self):
        strings = "".join(str(TimeTable(obj["type"], obj["schedules"])) for obj in self.time_table_types)
        string_fares = "".join(str(Fare(obj["start"], obj["destination"], obj["price"])) for obj in self.fares)
        string_cities = ", ".join(self.cities)
        return (
            f"Line Code: {self.number}\n\nCities on the route: {string_cities}\n\n"
            f"Website: {self.website}\n\nFares: {string_fares}\n\nRegular time table:\n{strings}\nSpecial time table: {self.time_table_types[1]}")

    def __repr__(self):
        return (
            f"Line number: {self.number}\nCities on the route: {self.cities}\n"
            f"Website: {self.website}\nFares: {self.fares}\n Time Tables: {self.time_table_types[0]}\n")