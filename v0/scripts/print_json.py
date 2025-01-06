from Getters import Getters
from TransportLine import TransportLine

def print_output():
    company_1_lines: list[TransportLine] = Getters.get_company_1_lines_data()
    for line in company_1_lines:
        print(line) 

print_output()

