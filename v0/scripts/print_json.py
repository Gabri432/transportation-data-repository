import json

from BusLine import BusLine

def print_autoguidovie_data():
    with open('v0/autoguidovie.json', 'r') as autog:
        autoguidovie_data = json.load(autog)
        autoguidovie_busLines = [BusLine(**busLine) for busLine in autoguidovie_data["lines"]]
        print(autoguidovie_busLines[0])

def print_starmobility_data():
    with open('v0/starmobility.json', 'r') as star:
        starmobility_data = json.load(star)
        starmobility_busLines = [BusLine(**busLine) for busLine in starmobility_data["lines"]]
        print(starmobility_busLines[0])

print("AUTOGUIDOVIE ================= =================")
print_autoguidovie_data()
print("END =================")
print("STARMOBILITY ================= =================")
print_starmobility_data()
print("END =================")
