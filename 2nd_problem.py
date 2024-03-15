from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}