# Notes REST API (Flask Enhancement Project)

## Project Overview
This project is an enhancement of an existing Flask-based Notes web application. The original system allows users to create and manage notes through a web interface. This enhancement introduces a RESTful API that enables programmatic access to notes using JSON-based communication.

The API implements full CRUD (Create, Read, Update, Delete) functionality.

---

## Technology Stack
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Pytest (for testing)

---

## Features Implemented

### REST API for Notes
The system now supports:

- Create a note
- Retrieve all notes
- Retrieve a single note
- Update a note
- Delete a note

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/notes` | Get all notes |
| GET | `/api/notes/<id>` | Get a specific note |
| POST | `/api/notes` | Create a new note |
| PUT | `/api/notes/<id>` | Update a note |
| DELETE | `/api/notes/<id>` | Delete a note |

---

## Example Request (POST)

```json
{
  "data": "My first API note"
}
