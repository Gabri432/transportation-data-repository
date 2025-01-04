import json

from BusLine import BusLine

class Getters:
    @staticmethod
    def get_autoguidovie_lines_data() -> list[BusLine]:
        """
        Returns a list of bus lines, related to Autoguidovie company, that serve Villanterio (currently just one).
        """
        with open('v0/autoguidovie.json', 'r') as autog:
            autoguidovie_data = json.load(autog)
            autoguidovie_bus_lines = [BusLine(**bus_line) for bus_line in autoguidovie_data["lines"]]
            return autoguidovie_bus_lines
    
    @staticmethod    
    def get_starmobility_lines_data() -> list[BusLine]:
        """
        Returns a list of bus lines, related to Star Mobility company, that serve Villanterio (currently just one).
        """
        with open('v0/starmobility.json', 'r') as star:
            starmobility_data = json.load(star)
            starmobility_bus_lines = [BusLine(**bus_line) for bus_line in starmobility_data["lines"]]
            return starmobility_bus_lines