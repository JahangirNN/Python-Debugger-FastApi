# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from app.langchain_utils import generate_initial_quiz  # Update import path based on your structure

# router = APIRouter()

# # Define the User model (if not already defined in a shared models file)
# class User(BaseModel):
#     name: str

# @router.post("/get_quiz")
# def get_quiz(user: User):
#     try:
#         # Generate quiz using LangChain utility
#         output = generate_initial_quiz(user.name)
#         return {"quiz": output}
#     except Exception as e:
#         # Handle any errors during quiz generation
#         raise HTTPException(status_code=500, detail=f"Error generating quiz: {str(e)}")



