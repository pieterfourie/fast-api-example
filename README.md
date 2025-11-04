# FastAPI Example

A minimal FastAPI project demonstrating how to create and run a simple web API endpoint.

## 🚀 Overview

This example defines a basic FastAPI application with a single `GET` route (`/`) that returns a JSON message.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


🧰 Requirements

Before running the app, ensure you have Python 3.9+ installed.

Install dependencies:

pip install fastapi uvicorn



▶️ Running the Application

You can start the FastAPI development server using Uvicorn:

uvicorn simple-api:app --reload


Alternatively, if you have the FastAPI CLI:

fastapi dev simple-api.py


Then open your browser at:
👉 http://127.0.0.1:8000

You should see:

{"message": "Hello, World!"}

🧪 API Endpoints
Method	Endpoint	Description
GET	/	Returns a welcome message