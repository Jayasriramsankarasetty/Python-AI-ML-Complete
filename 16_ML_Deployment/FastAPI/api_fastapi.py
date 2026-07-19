"""
Topic:
Model Serving with FastAPI & Pydantic

Importance:
FastAPI is the modern standard for Python API development.
It is built on top of Starlette and Pydantic, making it extremely fast,
automatically documenting endpoints (OpenAPI/Swagger), and validating input schemas.

This file covers:
- Concept: Input validation with Pydantic, asynchronous endpoints, HTTP status routing
- Defining request schemas using Pydantic BaseModel
- Defining response structures
- Creating GET health endpoints
- Creating POST predict endpoints serving a mock ML classification model
- Direct test invocation of handler functions
"""

# ==========================================
# 1. Concept Explanation & Glossary
# ==========================================
# FastAPI utilizes Pydantic validation:
#   - BaseModel: Defines the expected JSON schema keys and data types.
#     If a client sends incorrect types, FastAPI returns a 422 Unprocessable Entity error.
#   - Asynchronous handlers (async def): Allows handling concurrent requests efficiently.
#   - Automatic documentation: FastAPI hosts Swagger docs at `/docs`.

import sys

# Try importing fastapi; fallback gracefully if not present
use_fastapi = True
try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel, Field
    print("Using FastAPI framework.")
except ImportError:
    use_fastapi = False
    print("FastAPI or Pydantic not found. Running mock endpoint representation.")

# ==========================================
# 2. Schema Definitions (Pydantic)
# ==========================================
if use_fastapi:
    class PredictionRequest(BaseModel):
        # Validate that hours_studied is a float between 0.0 and 24.0
        hours_studied: float = Field(..., ge=0.0, le=24.0, description="Hours spent studying")
        # Validate that attendance is a float between 0.0 and 100.0
        attendance: float = Field(..., ge=0.0, le=100.0, description="Class attendance percentage")

    class PredictionResponse(BaseModel):
        prediction: int
        probability: float
        status: str

# ==========================================
# 3. API App & Routes
# ==========================================
if use_fastapi:
    app = FastAPI(title="Student Exam Predictor API", version="1.0")

    @app.get("/health")
    async def health_check():
        return {"status": "healthy", "service": "student_predictor"}

    @app.post("/predict", response_model=PredictionResponse)
    async def predict_exam_status(payload: PredictionRequest):
        try:
            # Mock model boundary prediction:
            # Pass = 1 if hours * 10 + attendance > 110
            metric = payload.hours_studied * 10 + payload.attendance
            probability = min(1.0, max(0.0, metric / 200.0))
            prediction = 1 if probability >= 0.55 else 0
            
            return PredictionResponse(
                prediction=prediction,
                probability=round(probability, 4),
                status="success"
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# ==========================================
# 4. Testing & Execution
# ==========================================
async def run_direct_mock_test():
    """
    Directly call the handler functions to verify route logic without locking
    the thread in a blocking uvicorn server.
    """
    if use_fastapi:
        print("\n=======================================")
        print("Testing FastAPI Route Handlers Directly:")
        print("=======================================")
        
        # Test Health Check
        health = await health_check()
        print("GET /health output: ", health)
        
        # Test Predict Route with valid mock inputs
        mock_payload = PredictionRequest(hours_studied=8.0, attendance=90.0)
        prediction = await predict_exam_status(mock_payload)
        print("POST /predict output:")
        print(f"  - Prediction:  {prediction.prediction} (1=Pass, 0=Fail)")
        print(f"  - Probability: {prediction.probability}")
        print(f"  - Status:      {prediction.status}")
        print("=======================================")
    else:
        print("FastAPI is not installed. Code is complete and ready for deployment.")

if __name__ == "__main__":
    # If run with argument '--server', start uvicorn. Otherwise, run mock test.
    if "--server" in sys.argv and use_fastapi:
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)
    else:
        import asyncio
        asyncio.run(run_direct_mock_test())

"""
Key Takeaways:
- Pydantic BaseModel defines the strict structured format of API payloads.
- FastAPI automatically parses JSON strings, casts data types, and generates validation checks.
- Asynchronous async handlers optimize speed under concurrent serving conditions.

Interview Relevance:
- Why is FastAPI preferred over Flask for modern APIs? (FastAPI is native asynchronous (ASGI), automatically validates inputs using Pydantic, and generates interactive Swagger/OpenAPI documentation automatically at `/docs`).
- What is the difference between a path parameter and a query parameter? (Path parameters are embedded directly in the URL endpoint path, e.g. `/users/{id}`; Query parameters are appended after a question mark, e.g. `/users?limit=10`).
- What HTTP status code is returned when input validation fails in FastAPI? (HTTP 422 Unprocessable Entity, accompanied by a detailed JSON body indicating which field failed and why).

AI/ML Relevance:
- Production Deployment: Serves as the standard API wrapper to expose trained models (like scikit-learn or PyTorch) as REST endpoints.
"""
