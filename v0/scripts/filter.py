from BusLine import BusLine, Route, Schedule
from Getters import Getters

class Filter:
    """
    Provide a series of filters to apply to each bus line
    """
    autoguidovie_bus_lines: list[BusLine] = Getters.get_autoguidovie_lines_data()
    starmobility_bus_lines: list[BusLine] = Getters.get_starmobility_lines_data()


    @staticmethod
    def filter_bus_line_by_period(bus_line=autoguidovie_bus_lines[0], period="weekdays") -> list[Route]:
        """
        Returns a list of (regular) bus times during the specified period.

        More specifically, returns a list of Route objects, each having a list of times in format dd:dd, the names of 
        the starting and destination cities per each route.
        
        Parameters
        ----------

        ### `bus_line`: BusLine 
            either starmobility_bus_lines[0] or autoguidovie_bus_lines[0] (default) (NOTE: there is currenlty one line per company)
        ### `period`: str
            either "holidays", "saturdays" or "weekdays" (default)
        """
        regular_schedules: list[Schedule] = [time_table for time_table in bus_line.time_table_types if time_table["type"] == "regular"][0]["schedules"]
        specific_period_regular_schedules = [schedule for schedule in regular_schedules if schedule["period"] == period] 
        return specific_period_regular_schedules[0]["routes"]
    
    @staticmethod
    def filter_route_times_by_time_after(bus_route=autoguidovie_bus_lines[0].time_table_types[0]["schedules"][0]["routes"][0], time="15:30") -> list[str]:
        """
        Returns a list of the existing (regular) bus times later than the one specified by the user. Each bus time represents the time 
        where the bus starts the route. That is, if the starting city is, let's say, Pavia, then all the bus times the function will return 
        are the starting times from Pavia.

        More specifically, it returns a list of strings in format dd:dd (d, decimal), each representing a time when a bus is present.

        Parameters
        ----------

        ### `bus_route`: Route
            object of type Route having a list of times, `start` as the starting city and `destination` as the destination city.
        ### `time`: str
            any string in format dd:dd, ideally between 05:00 and 21:00 (15:30 is default).
        """
        return [bus_time for bus_time in bus_route["times"] if bus_time > time]
    
    @staticmethod
    def filter_bus_line_by_time_after(bus_line=autoguidovie_bus_lines[0], time="15:30", period="weekdays") -> list[Route]:
        """
        Returns a list of (regular) bus times of the specified bus line (Autoguidovie or Starmobility) available later than the specified time, 
        at the specified period, between all routes (from and to Villanterio).

        More specifically, returns a list of Route objects, each having a list of times in format dd:dd later than, the names of 
        the starting and destination cities per each route.
        
        Parameters
        ----------

        ### `bus_line`: BusLine 
            either autoguidovie_bus_lines[0] (default) or starmobility_bus_lines[0] (NOTE: there is currenlty one line per company)
        ### `time`: str
            any string in format dd:dd, ideally between 05:00 and 21:00 (15:30 is default)
        """
        specific_period_routes = Filter.filter_bus_line_by_period(bus_line, period)
        filtered_routes: list[Route] = []
        for route in specific_period_routes:
            times = Filter.filter_route_times_by_time_after(route, time)
            filtered_routes.append(Route(route["start"], route["destination"], times))
        return filtered_routes
    
    @staticmethod
    def filter_bus_line_by_city(bus_line=starmobility_bus_lines[0], city="Pavia") -> list[Route]:
        """
        Returns a list of (regular) routes, where each route has the specified city as either starting or destination city.

        More specifically, returns a list of Route objects, each having a list of times in format dd:dd later than, the names of 
        the starting and destination cities per each route.

        Parameters
        ----------

        ### `bus_line`: BusLine 
            either autoguidovie_bus_lines[0] or starmobility_bus_lines[0] (default) (NOTE: there is currenlty one line per company)
        ### `city`: str
            either "Milan", "Lodi", or "Pavia" (default)
        """
        regular_schedules: list[Schedule] = [time_table for time_table in bus_line.time_table_types if time_table["type"] == "regular"][0]["schedules"]
        return [route for route in regular_schedules[0]["routes"] if route["start"] == city or route["destination"] == city]


print(Filter.filter_route_times_by_time_after())