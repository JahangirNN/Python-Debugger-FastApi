from fastapi import FastAPI
from app.routes import users, compiler_api, testCode, code, runCode
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI(title="AI Python Learner Platform")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify your Next.js URL instead of "*"
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Include routes
app.include_router(users.router, prefix="/users", tags=["Users"])
# app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(compiler_api.router, prefix="/compiler", tags=["Code Evaluation"])
app.include_router(testCode.router, prefix="/test", tags=["Code"])
app.include_router(code.router, prefix="/code", tags=["Code"])
app.include_router(runCode.router, prefix="/run", tags=["Run"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Python Learner Platform!"}