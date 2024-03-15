from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SumRequest(BaseModel):
    number1: float
    number2: float

@app.post("/add")
async def add_numbers(request: SumRequest):
    total = request.number1 + request.number2
    return {"total": total}
