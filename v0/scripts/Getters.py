import json

from BusLine import BusLine

class Getters:
    @staticmethod
    def get_json_data(path_to_json: str) -> list[BusLine]:
        with open(path_to_json, 'r') as autog:
            data = json.load(autog)
            return [BusLine(**bus_line) for bus_line in data["lines"]]

    @staticmethod
    def get_company_1_lines_data() -> list[BusLine]:
        """
        Returns a list of transportation lines related to company 1 (currently just one).
        """
        return Getters.get_json_data('v0/company_1.json')
    
    @staticmethod    
    def get_company_2_lines_data() -> list[BusLine]:
        """
        Returns a list of transportation lines related to company 2 (currently just one).
        """
        return Getters.get_json_data('v0/company_2.json')