from TransportLine import TransportLine, Route, Schedule
from Getters import Getters

class Filter:
    """
    Provide a series of filters to apply to each transportation line
    """
    company_1_transportation_lines: list[TransportLine] = Getters.get_company_1_lines_data()
    company_2_transportation_lines: list[TransportLine] = Getters.get_company_2_lines_data()


    @staticmethod
    def filter_transportation_line_by_period(transport_line=company_1_transportation_lines[0], period="weekdays") -> list[Route]:
        """
        Returns a list of (regular) transport times during the specified period.

        More specifically, returns a list of Route objects, each having a list of times in format dd:dd, the names of 
        the starting and destination cities per each route.
        
        Parameters
        ----------

        ### `transport_line`: TransportationLine 
            either company_2_transport_lines[0] or company_1_transport_lines[0] (default) (NOTE: there is currenlty one line per company)
        ### `period`: str
            either "holidays", "saturdays" or "weekdays" (default)
        """
        regular_schedules: list[Schedule] = [time_table for time_table in transport_line.time_table_types if time_table["type"] == "regular"][0]["schedules"]
        specific_period_regular_schedules = [schedule for schedule in regular_schedules if schedule["period"] == period] 
        return specific_period_regular_schedules[0]["routes"]
    
    @staticmethod
    def filter_route_times_by_time_after(transportation_route=company_1_transportation_lines[0].time_table_types[0]["schedules"][0]["routes"][0], time="15:30") -> list[str]:
        """
        Returns a list of the existing (regular) transport times later than the one specified by the user. Each transportation time represents the time 
        where the transport vehicle starts the route. That is, if the starting city is, let's say, City_1, then all the transportation times the function will return 
        are the starting times from City_1.

        More specifically, it returns a list of strings in format dd:dd (d, decimal), each representing a time when a transportation is present.

        Parameters
        ----------

        ### `transportation_route`: Route
            object of type Route having a list of times, `start` as the starting city and `destination` as the destination city.
        ### `time`: str
            any string in format dd:dd, ideally between 05:00 and 21:00 (15:30 is default).
        """
        return [transportation_time for transportation_time in transportation_route["times"] if transportation_time > time]
    
    @staticmethod
    def filter_transportation_line_by_time_after(transportation_line=company_1_transportation_lines[0], time="15:30", period="weekdays") -> list[Route]:
        """
        Returns a list of (regular) transportation times of the specified transportation line (company 1 or company 2) available later than the specified time, 
        at the specified period, between all routes.

        More specifically, returns a list of Route objects, each having a list of times in format dd:dd later than, the names of 
        the starting and destination cities per each route.
        
        Parameters
        ----------

        ### `transportation_line`: TransportationLine 
            either company_1_transportation_lines[0] (default) or company_2_transportation_lines[0] (NOTE: there is currenlty one line per company)
        ### `time`: str
            any string in format dd:dd, ideally between 05:00 and 21:00 (15:30 is default)
        """
        specific_period_routes = Filter.filter_transportation_line_by_period(transportation_line, period)
        filtered_routes: list[Route] = []
        for route in specific_period_routes:
            times = Filter.filter_route_times_by_time_after(route, time)
            filtered_routes.append(Route(route["start"], route["destination"], times))
        return filtered_routes
    
    @staticmethod
    def filter_transportation_line_by_city(transportation_line=company_2_transportation_lines[0], city="City_1") -> list[Route]:
        """
        Returns a list of (regular) routes, where each route has the specified city as either starting or destination city.

        More specifically, returns a list of Route objects, each having a list of times in format dd:dd later than, the names of 
        the starting and destination cities per each route.

        Parameters
        ----------

        ### `transportation_line`: TransportLine 
            either company_1_transportation_lines[0] or company_2_transportation_lines[0] (default) (NOTE: there is currenlty one line per company)
        ### `city`: str
            either "City_3", "City_2", or "City_1" (default)
        """
        regular_schedules: list[Schedule] = [time_table for time_table in transportation_line.time_table_types if time_table["type"] == "regular"][0]["schedules"]
        return [route for route in regular_schedules[0]["routes"] if route["start"] == city or route["destination"] == city]