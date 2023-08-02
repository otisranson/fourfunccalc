from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/add/{x}/{y}")
def add(x, y):
    """Add function"""
    return {"answer: ": x + y}

@app.get("/subtract/{x}/{y}")
def subtract(x, y):
    """Subtract function"""
    return {"answer: ": x + y}

@app.get("/multiply/{x}/{y}")
def multiply(x, y):
    """Multiply function"""
    return {"answer: ": x + y}

@app.get("/divide/{x}/{y}")
def divide(x, y):
    """Division function"""
    return "Stub stub stub."
    """if y == 0:
        return "Cannot divide by 0. I'm not that smart!"
    else:
        return {"answer: ": x / y}"""
