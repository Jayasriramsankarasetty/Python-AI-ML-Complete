"""
Topic:
Advanced Project - ML Model serving API using FastAPI

Importance:
Serving models via high-performance APIs is the standard way to deliver predictions.
This project implements production-style Pydantic schemas, routing, and exception handlers.

This file covers:
- Defining input schemas using Pydantic BaseModel
- Loading a predictive estimator
- Defining POST predict routes
- Simulating local verification requests
"""

import sys

# Try importing fastapi; fallback gracefully if not present
use_fastapi = True
try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel, Field
    print("Using FastAPI framework.")
except ImportError:
    use_fastapi = False
    print("FastAPI not found. Running mock endpoint representation.")

# ==========================================
# 1. Pydantic Schemas
# ==========================================
if use_fastapi:
    class ModelRequest(BaseModel):
        feature_1: float = Field(..., description="First continuous model feature")
        feature_2: float = Field(..., description="Second continuous model feature")

    class ModelResponse(BaseModel):
        prediction: int
        confidence: float
        status: str

# ==========================================
# 2. FastAPI Application
# ==========================================
if use_fastapi:
    app = FastAPI(title="Production Model serving service", version="1.0")

    @app.get("/health")
    async def health_check():
        return {"status": "online"}

    @app.post("/predict", response_model=ModelResponse)
    async def get_predictions(payload: ModelRequest):
        try:
            # Mock predictive model logic
            sum_val = payload.feature_1 + payload.feature_2
            confidence = min(0.99, max(0.01, abs(sum_val) / 10.0))
            prediction = 1 if sum_val >= 0.0 else 0
            
            return ModelResponse(
                prediction=prediction,
                confidence=round(confidence, 4),
                status="success"
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# ==========================================
# 3. Direct Route Testing
# ==========================================
async def test_endpoint_locally():
    if use_fastapi:
        print("\n=======================================")
        print("Testing Deployment FastAPI Handlers Locally:")
        print("=======================================")
        
        # Test GET /health
        health = await health_check()
        print("GET /health status: ", health)
        
        # Test POST /predict
        test_payload = ModelRequest(feature_1=2.5, feature_2=-1.2)
        response = await get_predictions(test_payload)
        print("POST /predict output:")
        print(f"  - Prediction: {response.prediction}")
        print(f"  - Confidence: {response.confidence}")
        print(f"  - Status:     {response.status}")
        print("=======================================")
    else:
        print("FastAPI not installed. Code complete and ready for containerization.")

if __name__ == "__main__":
    if "--server" in sys.argv and use_fastapi:
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)
    else:
        import asyncio
        asyncio.run(test_endpoint_locally())

"""
Key Takeaways:
- FastAPI handles JSON parsing and Pydantic schema validation natively.
- Asynchronous handlers maximize query throughput.
- /health endpoints are standard practice for Kubernetes/Cloud load balancer monitoring.

Interview Relevance:
- What is ASGI and how does it relate to FastAPI? (Asynchronous Server Gateway Interface. It is the modern standard for asynchronous Python web apps, succeeding WSGI. FastAPI is an ASGI app, allowing it to handle concurrent web sockets and long-polling connections efficiently).

AI/ML Relevance:
- Production deployments: Wrapper pipeline used to expose models to production microservices.
"""
