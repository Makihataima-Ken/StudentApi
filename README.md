# StudentApi (Django)

This is a minimal Django application with a single endpoint: `/get/students`. It returns a static list of student data **without using a database**.

## Features

- ✅ One GET endpoint: `/get/students`
- ✅ Returns a JSON list of students
- ❌ No database required
- ✅ Fast and lightweight

## How To Install
1. clone the repo
2. install Django
3. run the server 'python manage.py runserver'
4. go in your browser to 'http://127.0.0.1:8000/get/students'

## Endpoint

### GET `/get/students`

**Response:**
```json
{
  "students": [
    {"id": 1, "name": "Alice", "age": 21},
    {"id": 2, "name": "Bob", "age": 22},
    {"id": 3, "name": "Charlie", "age": 20},
    {"id": 4, "name": "Mani" , "age": 19}
  ]
}

