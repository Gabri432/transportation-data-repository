import datetime

from BusLine import BusLine, Route, Schedule, TimeTable
from Filter import Filter
from Getters import Getters
from enums import PeriodEnum


class Run:
    """
    Class printing a series of available bus times after the current time, or after 15:30 if current time isn't available.
    """
    company_1_bus_lines: list[BusLine] = Getters.get_autoguidovie_lines_data()
    company_2_bus_lines: list[BusLine] = Getters.get_starmobility_lines_data()
    current_time: str = "15:30"
    current_period: str = "weekdays"

    def __set_current_time(self):
        """
        Sets the current time to use for filtering bus times
        """
        today = datetime.datetime.now()
        hours = today.hour
        minutes = today.minute
        self.current_time = f"{hours}:{minutes}"

    def __set_current_period_of_the_week(self):
        """
        Sets the current period of the week to use for filtering bus times
        """
        today = datetime.datetime.now()
        day_of_week = today.isoweekday()
        if (day_of_week < 6):
            self.current_period = PeriodEnum.WEEKDAYS.value
        elif (day_of_week == 6):
            self.current_period = PeriodEnum.SATURDAYS.value
        else:
            self.current_period = PeriodEnum.HOLIDAYS.value
    
    def __get_company_1_regular_routes(self) -> list[Route]:
        """
        Gets regular routes for company 1.
        """
        return self.__get_regular_routes(self.company_1_bus_lines[0].time_table_types[0])

    def __get_company_2_regular_routes(self) -> list[Route]:
        """
        Gets regular routes for company 2.
        """
        return self.__get_regular_routes(self.company_2_bus_lines[0].time_table_types[0])
    
    def __get_regular_routes(self, regular_timetable: TimeTable):
        """
        Gets regular routes for any regular timetable.
        """
        specific_period_schedules: list[Schedule] = [schedule for schedule in regular_timetable["schedules"] if schedule["period"] == self.current_period]
        specific_period_all_regular_routes = specific_period_schedules[0]["routes"]
        specific_period_filtered_routes: list[Route] = []
        for route in specific_period_all_regular_routes:
            available_bus_times = Filter.filter_route_times_by_time_after(route, self.current_time)
            filtered_route = Route(route["start"], route["destination"], available_bus_times)
            specific_period_filtered_routes.append(filtered_route)

        return specific_period_filtered_routes

    def print_routes(self):
        self.__set_current_period_of_the_week()
        self.__set_current_time()
        company_1_routes: list[Route] = self.__get_company_1_regular_routes()
        company_2_routes: list[Route] = self.__get_company_2_regular_routes()
        print(f"Printing all the next bus times for today, after {self.current_time}, using the '{self.current_period}' schedule\n")
        print("List of all bus times of Company 1:\n")
        for route in company_1_routes:
            print(route)
        print("List of all bus times of Company 2:\n")
        for route in company_2_routes:
            print(route)



x = Run()
x.print_routes()

