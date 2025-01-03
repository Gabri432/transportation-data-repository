# Public Transportation Data Repository for Villanterio

This repository contains structured and versioned data about public transportation in Villanterio. The goal is to provide utility information for citizens of the town and application development. 

## Intended use

1. The idea behind this project is to allow to search at what times there were buses to and from Villanterio.

2. There are (currently) two bus lines, one that goes to Milan and back, the other that goes from Lodi to Pavia, and back.

3. You can search at what times there is a bus from Pavia, from Lodi, or from Milan, that takes to Villanterio. Conversely, you can also seach at what times a bus from Villanterio goes to Pavia, Lodi or Milan.

4. There are also extra details about the cities crossed, the number of the line, the website of the (two) companies. 

5. This project may be still a valid starting point if you intended to use for your own city.

## Project Structure

The repository is organized into multiple folders based on data versions. Each version represents a stable snapshot of the transportation data, with improvements and changes documented over time.

```
root
-- LICENSE             # Repository licensing information (MIT)
-- README.md           # Overview and instructions for using the repository
-- CONTRIBUTING.md     # Guidelines for contributing to the project
-- .gitignore          # Specifies files and folders to exclude from version control

-- v0/                 # Unstable data, subject to breaking changes
---- autoguidovie.json   # Transportation data for Company 1
---- star.json         # Transportation data for Company 2

-- v1/                 # First stable version of the data
---- company1.json
---- company2.json

-- v2/                 # Second stable version of the data (not currently existing, just to give you the idea)
---- company1.json
---- company2.json

-- scripts/              # Utility scripts for managing and validating data
---- validate_schema.py
---- update_version.py
```

### File Structure

Each version folder (e.g., `v1`, `v2`) contains:
- JSON files: Structured data for individual transportation companies.
- Consistent formatting and adherence to a predefined schema (if applicable).
```json
{}
```

### Schema

The data in this repository adheres to a standardized schema to ensure consistency and interoperability. You can find the schema definition in the `schema/` folder (if applicable).

## How to Use the Data

1. **Download the Repository**
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Gabri432/transportation-data-villanterio.git
   ```

2. **Select a Data Version**
   Navigate to the desired version folder (e.g., `v1/`) to access stable data.

3. **Load and Use JSON Files**
   Use your preferred programming language or tools to parse the JSON data. For example, in Python:
   ```python
   import json

   with open('v1/company1.json', 'r') as file:
       data = json.load(file)
       print(data)
   ```

4. **Validate Data (Optional)**
   Run the provided validation script to ensure data integrity:
   ```bash
   python scripts/validate_schema.py
   ```

## Contributing

In `CONTRIBUTING.md` you will know how you can contribute to the project.

## License

This repository is licensed under the MIT. See `LICENSE` for more details.

## Notes

1. When considering line 97, I have only considered buses from Villanterio to Milan, and back. Therefore I have ignored those buses that goes to Inverno or Pieve Porto Morone. If you need more information check [Autoguidovie's website](https://pavia.autoguidovie.it/it/orario-invernale-scolastico-extraurbano-24-25).

2. This project is intended for learning porpuses, and utility, not for profit.
