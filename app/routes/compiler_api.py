import requests
from fastapi import APIRouter
from pydantic import BaseModel

COMPILER_URL = "https://jahangir.pythonanywhere.com/run"

router = APIRouter()

class Code(BaseModel):
    code:str

@router.post("/run")
def execute_code(code: Code):
    response = requests.post(COMPILER_URL, json={"code": code.code})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to execute code", "details": response.text}
