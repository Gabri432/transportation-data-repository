# Public Transportation Data Repository for Villanterio

This repository contains structured and versioned data about public transportation in Villanterio. The goal is to provide a reliable and well-documented resource for researchers, developers, and policymakers interested in transportation analysis and application development. 

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
---- star.json   # Transportation data for Company 2

-- v1/                 # First stable version of the data
---- company1.json
---- company2.json

-- v2/                 # Second stable version of the data
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

We welcome contributions to improve the quality and coverage of the data. Please refer to `CONTRIBUTING.md` for detailed guidelines.

## License

This repository is licensed under the MIT. See `LICENSE` for more details.

## Notes

When considering line 97, I have only considered buses from/to Milan, and back to Villanterio. Therefore those buses that goes to Inverno or Pieve Porto Morone. If you need more information check [Autoguidovie's website](https://pavia.autoguidovie.it/it/orario-invernale-scolastico-extraurbano-24-25).


