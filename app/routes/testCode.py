from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any
import sys
import io

router = APIRouter()

# Request body model
class TestCase(BaseModel):
    input: str
    expected: Any

class TestRequest(BaseModel):
    code: str
    test_cases: List[TestCase]

# Helper function to execute code and capture output
# Helper function to execute code and capture output
# Helper function to execute code and capture output
def execute_code(code: str, test_cases: List[TestCase]) -> Dict[str, Any]:
    # Shared namespace for exec and eval
    namespace = {}
    try:
        # Execute the user-provided code
        exec(code, namespace)
    except Exception as e:
        return {"error": f"Error executing code: {str(e)}"}

    # Verify the presence of callable functions
    function_names = [name for name, obj in namespace.items() if callable(obj)]
    if not function_names:
        return {"error": "No callable function found in the provided code."}

    results = []

    for idx, test_case in enumerate(test_cases):
        input_str = test_case.input
        expected_result = test_case.expected

        try:
            # Evaluate the input within the shared namespace
            result = eval(input_str, namespace)
            if result == expected_result:
                results.append({
                    "test_case": idx + 1,
                    "status": "Passed",
                    "result": result
                })
            else:
                results.append({
                    "test_case": idx + 1,
                    "status": "Failed",
                    "expected": expected_result,
                    "got": result
                })
        except Exception as e:
            results.append({
                "test_case": idx + 1,
                "status": "Error",
                "message": str(e)
            })

    return {"results": results}

# POST endpoint to test Python code
@router.post("/test_code")
async def test_code(test_request: TestRequest):
    try:
        code = test_request.code
        test_cases = test_request.test_cases

        if not code or not test_cases:
            raise HTTPException(status_code=400, detail="Missing 'code' or 'test_cases' in request.")

        result = execute_code(code, test_cases)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

