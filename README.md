# API Data Fetching and Search Project

## Description

This project fetches user data from a REST API using Python
and the Requests module. The JSON response is parsed and
displayed in a clean format.

The project also provides search and filter functionality
to find users by name, email, or city.

## Technologies Used

- Python
- Requests
- REST API
- JSON
- VS Code

## API Used

JSONPlaceholder Users API

## Features

- Fetch user data from API
- Parse JSON response
- Display user information
- Search users by name
- Search users by email
- Search users by city
- Handle API errors
- Exit option

## How to Run

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

## Search Example

Users can be searched using:

- Name
- Email
- City

Example:

```text
Enter your choice: 2
Enter name, email, or city to search: Leanne
```

## Output

The application displays user ID, name, email, and city.

## Author

Bobbili Venkata Hari Varun