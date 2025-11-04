from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

# Bash: fastapi dev simple-api.py
# Command to run the application using Uvicorn