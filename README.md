# Library Management System

## Overview

A Python Command-Line Interface (CLI) application for managing a library's books, members, and loans.

The system demonstrates Object-Oriented Programming (OOP), file persistence using JSON, command-line interaction with argparse, unit testing with pytest, and Git-based version control.

---

## Features

### Book Management

* Add books
* View all books
* Track availability status

### Member Management

* Add members
* View all members
* Email validation using property setters

### Loan Management

* Borrow books
* Return books
* View loan records

### Persistence

* Save data to JSON files
* Load data from JSON files
* Data persists between program executions

### Testing

* Unit tests using pytest

---

## Project Structure

```text
library-management/
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── loans.json
│
├── models/
│   ├── person.py
│   ├── member.py
│   ├── book.py
│   └── loan.py
│
├── services/
│   └── library_manager.py
│
├── tests/
│   └── test_library.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Object-Oriented Design

### Classes

* Person
* Member
* Book
* Loan
*
## Object-Oriented Design

### Classes

* **Person** – Base class containing shared attributes such as name and email.
* **Member** – Inherits from Person and represents a library member.
* **Book** – Represents a book in the library and tracks availability.
* **Loan** – Represents a borrowing transaction between a member and a book.

### OOP Concepts Used

* Inheritance (`Member` inherits from `Person`)
* Encapsulation (`@property` and setter validation for email addresses)
* Class Attributes (`id_counter` for automatic ID generation)
* Instance Methods (`borrow_book`, `return_book`, etc.)
* Class Methods (`from_dict()` for recreating objects from JSON data)

---

## Command Line Usage

### Add a Book

```bash
python3 main.py add-book "Harry Potter" "J.K. Rowling"
```

### List Books

```bash
python3 main.py list-books
```

### Add a Member

```bash
python3 main.py add-member "John" "john@gmail.com"
```

### List Members

```bash
python3 main.py list-members
```

### Borrow a Book

```bash
python3 main.py borrow-book 1 1
```

### Return a Book

```bash
python3 main.py return-book 1
```

### View Loans

```bash
python3 main.py view-loans
```

---

## File Persistence

Data is stored locally in JSON files:

* `data/books.json`
* `data/members.json`
* `data/loans.json`

The application automatically loads data from these files and saves changes after operations are performed.

---

## Running Tests

Run all tests using:

```bash
python3 -m pytest
```

---

## Dependencies

Install dependencies using:

```bash
pip install -r requirements.txt
```

Packages used:

* pytest
* rich (if installed)

---

## Author

ALVIN MUTHEE
