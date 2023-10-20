# API Data Exporter

This project involves working with APIs to fetch and export data. It includes Python scripts to interact with an external REST API, retrieve specific data, and export it in various formats.

## Project Overview

- **Employee TODO List Data**: The project focuses on retrieving and exporting employee TODO list data.

- **Data Formats**: It supports both JSON and CSV data formats for export.

- **Scripts**:
  - `employee_todo.py`: Exports TODO list data for a single employee.
  - `export_all_employees.py`: Exports TODO list data for all employees.

## Usage

- To export data for a single employee:
  ```bash
  python 1-export_to_CSV.py <employee_id> [--csv]

python 3-dictionary_of_list_of_dictionaries.py

Requirements
Python 3.x
requests library (for making HTTP requests)
csv library (for CSV export)
json library (for JSON export)

