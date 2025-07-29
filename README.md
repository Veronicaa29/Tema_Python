
# Tema_Python

## Description
This repository contains two related projects:

### 1. Tema Python CLI
This is a Command Line Interface (CLI) application for performing basic mathematical operations and saving the results in a SQLite database.

#### Main Features (CLI)
- Calculates the factorial of a number
- Calculates the n-th number in the Fibonacci sequence
- Calculates the power of a number
- Saves each operation performed (input, result, operation type, timestamp) in a SQLite database
- Allows you to view all performed operations

#### How to run the CLI project

1. Install dependencies (Python 3.8+):
   ```
   pip install -r requirements.txt
   ```
2. Run CLI commands from the `Tema Python` directory:
   - Factorial:
     ```
     python cli.py factorial-cmd --number 5
     ```
   - Fibonacci:
     ```
     python cli.py fib --number 7
     ```
   - Power:
     ```
     python cli.py pow --base 2 --exp 8
     ```
3. View the operation history:
   ```
   python show_db.py
   ```

---

### 2. Tema Python API
This is a RESTful API implementation of the same mathematical operations, using FastAPI. The operations are saved in a SQLite database.

#### Main Features (API)
- Exposes endpoints for factorial, Fibonacci, and power operations
- Each operation is logged in the database with input, result, operation type, and timestamp
- Provides an endpoint to view the latest operation history
- Input validation is handled with Pydantic models

#### How to run the API project

1. Install dependencies (Python 3.8+):
   ```
   pip install -r requirements.txt
   ```
3. Start the API server:
   ```
   uvicorn app.main:app --reload
   ```
4. Access the interactive API documentation at:
   - [http://localhost:8000/docs](http://localhost:8000/docs)

#### Example API Endpoints
- `POST /math/factorial` — Calculate factorial
- `POST /math/fibonacci` — Calculate Fibonacci number
- `POST /math/power` — Calculate power
- `GET /math/history` — Get the latest 20 operations

---

## Other details
- All CLI operations are executed in separate threads so the CLI interface is not blocked.
- Input and output structure is validated with Pydantic.
- The database used is `operations.db` (SQLite).
- The API project is designed for extensibility and follows microservice best practices.