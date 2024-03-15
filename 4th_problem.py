from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Memo(BaseModel):
    id: int
    content: str
    completed: bool

# 메모 데이터를 저장할 임시 데이터베이스 역할을 하는 딕셔너리
memos = {}

@app.post("/memos/", response_model=Memo)
async def create_memo(memo: Memo):
    if memo.id in memos:
        raise HTTPException(status_code=400, detail="Memo with this ID already exists.")
    memos[memo.id] = memo
    return memo

@app.get("/memos/", response_model=List[Memo])
async def read_memos():
    return list(memos.values())

@app.get("/memos/{memo_id}", response_model=Memo)
async def read_memo(memo_id: int):
    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found.")
    return memos[memo_id]

@app.put("/memos/{memo_id}", response_model=Memo)
async def update_memo(memo_id: int, updated_memo: Memo):
    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found.")
    memos[memo_id] = updated_memo
    return updated_memo

@app.delete("/memos/{memo_id}", response_model=Memo)
async def delete_memo(memo_id: int):
    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found.")
    deleted_memo = memos.pop(memo_id)
    return deleted_memo
