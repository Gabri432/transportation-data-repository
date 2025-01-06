# Public Transportation Data Repository Structure

This repository was made with idea is to create a convenient structure/template for possible/futre applications with real transportation data.

## Expected Features

1. Allows a user to search for incoming and outgoing buses (or any transportation vehicle) for a city. 

2. You can search at what times there is a bus from City_1 to City_2 or to City_3 and viceversa.

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
---- company_1.json     # Transportation data for Company 1
---- company_2.json     # Transportation data for Company 2
---- scripts/
------ Filter.py       # Utility class for filtering data
------ Getters.py      # Utility class for getting data
------ enums.py        # List of various Enums
------ TransportLine.py# List of various classes used to represent data
------ print_json.py   # Utility functions for printing data
------ run.py          # Simple program to show an example of usage


-- v1/                 # First stable version of the data (not currently existing, just to give you an idea)
---- company_1.json
---- company_2.json
---- scripts/
------ Filter.py       # Each version will have its own set of scripts to ensure backward compatibility
------ [...]

-- v2/                 # Second stable version of the data (not currently existing, just to give you the idea)
---- company_1.json
---- company_2.json
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
            "cities":["City_1", "..."], // The list of cities crossed by this line
            "vehicle":"bus", // Vehicle used for the line
            "website": "https://link_to_the_company_website", // Link to the website
            "fares": [ // List of fares
                {
                    "start":"City_1", // Starting city related to the fare 
                    "destination":"City_2", // Destination city related to the fare
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
                                    "start":"City_1", // Starting city of the specific route
                                    "destination":"City_2", // Destination city of the specific route
                                    "times":["05:40", "..."] // List of bus times when they start from the starting city
                                },
                                {
                                    "start":"City_1", // Starting city of the specific route
                                    "destination":"City_2", // Destination city of the specific route
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
   git clone https://github.com/Gabri432/transportation-data-repository.git
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
   https://raw.githubusercontent.com/Gabri432/transportation-data-repository/refs/heads/main/v0/company_1.json
   ```

## Contributing

In `CONTRIBUTING.md` you will know how you can contribute to the project.

## License

This repository is licensed under the Apache License, Version 2.0. See `LICENSE` for more details.

## NOTES

1. This project is intended for learning porpuses, and utility, not for profit.

2. Python version used: 3.12.4

3. The schedule data is purely fictional, for illustrative porpuses.

