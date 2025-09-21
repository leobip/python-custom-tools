# JSON Full Search

A simple Python utility to recursively search for a specific key inside a JSON file (or nested dictionaries) and return its value.  

This tool is useful when working with deeply nested JSON structures where keys may not be at the root level.

---

## Features

- 🔍 Search for a given key inside **nested JSON objects**.  
- ✅ Returns the first occurrence of the key.  
- ⚡ Lightweight and easy to use.  
- 🐍 Pure Python implementation.  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/leobip/python-custom-tools.git
cd python-custom-tools
```

## Usage

Example JSON file (test_data.json)

```json
{
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "country": {
      "name": "United States",
      "code": "US"
    }
  }
}
```

### Example Python code

```python
from json_fsearch import read_json_file

file_path = "test_data.json"
search_key = "city"

result = read_json_file(file_path, search_key)

if result is not None:
    print(f"The value of '{search_key}' is: {result}")
else:
    print(f"Key '{search_key}' not found.")
```

### Output

```bash
The value of 'city' is: Anytown
```

---

### Functions

json_full_search(obj, search_key)

- Recursively searches a dictionary (obj) for the given key.
- Returns the value if found, otherwise None.

read_json_file(file_path, search_key)

- Opens and parses the JSON file at file_path.
- Calls json_full_search to locate the search_key.
- Handles invalid JSON with error messages.

---

### Pending Improvements

- Add support for duplicate keys (returning multiple results).
- Add list traversal support (currently only works for nested dictionaries).
- Add unit tests for more reliability.

### License

***MIT License © 2024 Leoncio López***
