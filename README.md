# Python Custom Tools 🐍

This repository is a collection of **custom Python functions and tools** that I develop for daily use, problem-solving, and simplifying common tasks.  

The goal is to share small but useful utilities that can help in different projects or workflows.  
New tools will be added progressively, and this README will serve as an index with short explanations for each one.  

---

## 📌 Tools Index

### 1. JSON Full Search

- **Description:** Recursively searches through a JSON file or nested Python dictionaries to extract the value of a given key.  
- **Status:** Working, with planned improvements (support for duplicate keys, list traversal).  
- **File:** `json_fsearch.py`  

---

## 🚀 Usage

Each tool is implemented as a standalone Python file.  
You can import the functions into your own projects or run them directly with sample data.  

Example (from `json_fsearch.py`):

```python
from json_fsearch import read_json_file

result = read_json_file("test_data.json", "city")
print(result)  # → Anytown

```

### License

***MIT License © 2024 Leoncio López***
