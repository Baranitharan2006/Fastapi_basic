from fastapi import FastAPI, Body, Form
from pydantic import BaseModel

app = FastAPI()


class UserInput(BaseModel):
    name: str
    price: float
    in_stock: bool


@app.post("/json")
def receive_json(user_input: UserInput):
    return {
        "name": user_input.name,
        "price": user_input.price,
        "in_stock": user_input.in_stock
    }


@app.post("/text")
def receive_text(content: str = Body(..., media_type="text/plain")):
    return {
        "type": "plain text",
        "content": content
    }


@app.post("/form")
def receive_form(user_input: str = Form(...), password: str = Form(...)):
    return {
        "type": "form data",
        "user_input": user_input,
        "password": password
    }
