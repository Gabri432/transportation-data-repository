# Public Transportation Data Repository for Villanterio

This repository contains structured and versioned data about public transportation in the town of Villanterio. The idea is to create a convenient structure/template for possible/futre applications with real transportation data.

## Expected Features

1. Allows a user to search for incoming and outgoing buses for a city. In this specific case, I have used 2 transportation lines and four (real name) cities.

2. You can search at what times there is a bus from Pavia, from Lodi, or from Milan, that takes to Villanterio. Conversely, you can also seach at what times a bus from Villanterio goes to Pavia, Lodi or Milan.

3. There are also extra details about the cities crossed, the line name, the website of the companies. 

4. This project may be a good starting point if you intend to use it for your own city.

## Project Structure

The project is organized in folders, each representing a version of the entire project.

Each folder contains its own set of json data and scripts.

```python
root
-- start.py            # Script to explain more in detail the project
-- LICENSE             # Repository licensing information (Apache License Version 2.0)
-- README.md           # Overview and instructions for using the repository
-- CONTRIBUTING.md     # Guidelines for contributing to the project
-- .gitignore          # Specifies files and folders to exclude from version control

-- v0/                 # Unstable data, subject to breaking changes
---- company1.json     # Transportation data for Company 1
---- company2.json     # Transportation data for Company 2
---- scripts/
------ Filter.py       # Utility class for filtering data
------ Getters.py      # Utility class for getting data
------ enums.py        # List of various Enums
------ BusLine.py      # List of various classes used to represent data
------ print_json.py   # Utility functions for printing data
------ run.py          # Simple program to show an example of usage


-- v1/                 # First stable version of the data (not currently existing, just to give you an idea)
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
            "line_code":"Bus Line Name or Code 0123", // The name or code of the line
            "cities":["Villanterio", "..."], // The list of cities crossed by this line
            "vehicle":"bus", // Vehicle used for the line
            "website": "https://link_to_the_company_website", // Link to the website
            "fares": [ // List of fares
                {
                    "start":"Villanterio", // Starting city related to the fare 
                    "destination":"Milan", // Destination city related to the fare
                    "price":"9.99" // Cost of the travel between start and destination (in Euros)
                    
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

   To run the program and getting the next bus times:
   ```
   python v0/scripts/run.py
   ```

4. **Just get the data**
   If you just need the data you can access the rawgithubusercontent:
   ```
   https://raw.githubusercontent.com/Gabri432/transportation-data-villanterio/refs/heads/main/v0/company1.json
   ```

## Contributing

In `CONTRIBUTING.md` you will know how you can contribute to the project.

## License

This repository is licensed under the Apache License, Version 2.0. See `LICENSE` for more details.

## NOTES

1. This project is intended for learning porpuses, and utility, not for profit.

2. Python version used: 3.12.4

3. The schedule data is sourced from publicly available PDFs provided by transportation companies. The data used in this project has been manually transcribed into JSON format. Below are the sources of the schedules:

Autoguidovie: https://pavia.autoguidovie.it/it/orario-invernale-scolastico-extraurbano-24-25

Star Mobility: https://starmobility.it/star/pdf.php?line=S001

### Disclaimers

1. Independence Disclaimer: This project is an independent initiative and is not affiliated with, sponsored by, or endorsed by any transportation company mentioned herein.

2. Accuracy Disclaimer: The data provided in this project is for informational purposes only. Users are encouraged to verify the schedules directly with the official sources as linked in this document and the tool itself. This project is not liable for any discrepancies or inaccuracies in the data.

3. Non-commercial Disclaimer: This project is strictly non-commercial and intended solely for public utility and personal learning purposes. No tickets are sold, and no revenue is generated from this project.

