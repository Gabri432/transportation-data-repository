# Public Transportation Data Repository for Villanterio

This repository contains structured and versioned data about public transportation in Villanterio. The goal is to provide utility information for citizens of the town and application development. 

## Intended use

1. The idea behind this project is to allow to search at what times there were buses to and from Villanterio.

2. There are (currently) two bus lines, one that goes to Milan and back, the other that goes from Lodi to Pavia, and back.

3. You can search at what times there is a bus from Pavia, from Lodi, or from Milan, that takes to Villanterio. Conversely, you can also seach at what times a bus from Villanterio goes to Pavia, Lodi or Milan.

4. There are also extra details about the cities crossed, the number of the line, the website of the (two) companies. 

5. This project may be still a valid starting point if you intended to use for your own city.

## Project Structure

The project is organized in folders, each representing a version of the entire project.

Each folder contains its own set of json data and scripts.

```python
root
-- LICENSE             # Repository licensing information (MIT)
-- README.md           # Overview and instructions for using the repository
-- CONTRIBUTING.md     # Guidelines for contributing to the project
-- .gitignore          # Specifies files and folders to exclude from version control

-- v0/                 # Unstable data, subject to breaking changes
---- autoguidovie.json # Transportation data for Company 1
---- star.json         # Transportation data for Company 2
---- scripts/
------ Filter.py       # Utility class for filtering data
------ Getters.py      # Utility class for getting data
------ enums.py        # List of various Enums
------ BusLine.py      # List of various classes used to represent data
------ print_json.py   # Utility functions for printing data
------ help.py         # Simple program helping how to use each component


-- v1/                 # First stable version of the data
---- company1.json
---- company2.json
---- scripts/
------ Filter.py       # Each version will have its own set of scripts to ensure backward compatibility
------ [...]

-- v2/                 # Second stable version of the data (not currently existing, just to give you the idea)
---- company1.json
---- company2.json
---- scripts/
------ Filter.py
------ [...]
```

#### Json structure part 1
```json
{
   "lines":[ // Set of lines (currently one per company)
        {
            "number":"97", // The number or name of the line
            "cities":["Villanterio", "..."], // The list of cities crossed by this line
            "website": "https://pavia.autoguidovie.it/it/orario-invernale-scolastico-extraurbano-24-25", // Link to the website
            "fares": [ // List of fares
                {
                    "start":"Villanterio", // Starting city related to the fare 
                    "destination":"Milan", // Destination city related to the fare
                    "price":"4.80" // Cost of the travel between start and destination (in Euros)
                    
                }
            ],
            "time_table_types":[...] // List of Time Table (see next box)
        }
   ]
}
```
#### Json structure part 2
```json
{
   ...
   "time_table_types":[
                {
                    "type": "regular", // Type of time table ("regular" or "special")
                    "schedules": [     // List of schedules
                        {
                            "period":"weekdays", // Period ("weekdays", "saturdays" or "holidays")
                            "routes":[
                                {
                                    "start":"Villanterio", // Starting city of the specific route
                                    "destination":"Milan", // Destination city of the specific route
                                    "times":["05:43", "..."] // List of bus times when they start from the starting city
                                },
                                {
                                    "start":"Milan", // Starting city of the specific route
                                    "destination":"Villanterio", // Destination city of the specific route
                                    "times":["07:50", "..."] // List of bus times when they start from the starting city
                                }
                            ]
                        },
                        ... // Next schedules
                    ]
                },
                {
                    "type": "special",
                    "schedules": []
                },
                ... // Next time table types
            ]
}
```

## How to Use the Data

1. **Download the Repository**
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Gabri432/transportation-data-villanterio.git
   ```

2. **Select a Data Version**
   Navigate to the desired version folder (e.g., `v1/`) to access stable data.

3. **Load and Use JSON Files**
   To view data in a human readable format:
   ```
   python v0/scripts/print_json.py
   ```

   To ask for help about how to use the code:
   ```
   python v0/scripts/help.py
   ```

## Contributing

In `CONTRIBUTING.md` you will know how you can contribute to the project.

## License

This repository is licensed under the MIT. See `LICENSE` for more details.

## Notes

1. When considering line 97, I have only considered buses from Villanterio to Milan, and back. Therefore I have ignored those buses that goes to Inverno or Pieve Porto Morone. If you need more information check [Autoguidovie's website](https://pavia.autoguidovie.it/it/orario-invernale-scolastico-extraurbano-24-25).

2. This project is intended for learning porpuses, and utility, not for profit.

3. Python version used: Python 3.12.4
