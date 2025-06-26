# Python Emerging Issues Project

This project contains a collection of Python code examples that explore and demonstrate several emerging or commonly misunderstood issues in Python development. Each code snippet addresses a specific topic with a practical example and clear output.

## 🔍 Project Contents

### ✅ Code 1: Performance of Python Lists vs NumPy Arrays
Compares the performance of adding two large datasets using regular Python lists and NumPy arrays. This highlights how NumPy can significantly improve performance for numerical operations.

### ✅ Code 2: SSL Verification Errors in the Requests Library
Demonstrates how SSL errors can occur when accessing a website with an expired certificate using the `requests` library, and how to bypass them with `verify=False` (not recommended for production use).

### ✅ Code 3: Challenges With JSON Serialization of Custom Objects
Shows how trying to serialize a custom Python object with `json.dumps()` causes a `TypeError`, and the correct way to handle it using a custom `to_json()` method.

### ✅ Code 4: Security Risks Associated With Running Flask Applications in Debug Mode
Explains how running a Flask app in debug mode exposes potential security vulnerabilities. The script toggles `debug=True` or `False` based on the environment variable `FLASK_ENV`.

### ✅ Code 5: Mutable Default Arguments
Illustrates a classic Python gotcha where using mutable default arguments like lists can lead to unexpected behavior. Shows the incorrect and correct ways to define default values in functions.

---

## ⚙️ Installation

Before running the examples, make sure you have Python installed (Python 3.6 or higher recommended). Then install the required external libraries:

```bash
pip install numpy requests flask
