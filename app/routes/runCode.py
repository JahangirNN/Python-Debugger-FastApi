from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import sys
import io

router = APIRouter()

# Request model
class CodeRequest(BaseModel):
    code: str

# Helper function to execute user-provided code
def run_code(code: str) -> dict:
    # Create a shared namespace for exec
    namespace = {}

    # Capture standard output
    stdout = io.StringIO()
    stderr = io.StringIO()

    try:
        # Redirect standard output and error
        sys.stdout = stdout
        sys.stderr = stderr

        # Execute the provided code
        exec(code, namespace)

        # Restore standard output and error
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        # Capture output
        output = stdout.getvalue()
        error = stderr.getvalue()

        # Return results
        if error:
            return {"error": error.strip()}
        return {"output": output.strip()}
    except Exception as e:
        # Restore standard output and error in case of an exception
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        return {"error": str(e)}
    finally:
        # Ensure streams are closed
        stdout.close()
        stderr.close()

# POST endpoint to execute code
@router.post("/run_code")
async def execute_code(code_request: CodeRequest):
    try:
        code = code_request.code

        if not code:
            raise HTTPException(status_code=400, detail="No code provided.")

        # Run the code and get the result
        result = run_code(code)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


