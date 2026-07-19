# Advanced Project 3: ML Model serving API (FastAPI)

## Project Objective
Develop a production-grade FastAPI microservice that exposes a trained machine learning model as a REST API endpoint.

## Problem Statement
A machine learning model saved as a serialized file (e.g. pickle) cannot be consumed by client-side web or mobile applications directly. This project implements a FastAPI wrapper to load models and serve predictions over HTTP.

## Technologies Used
- Python 3.10+
- Pandas & NumPy
- FastAPI & Pydantic (REST routing, request/response validation schemas)
- Uvicorn (ASGI web server)

## Architecture & Workflow
1. **Model Loading**: Initialize and load a prediction model class.
2. **Schema Validation**: Define Pydantic request models for features validation.
3. **Endpoint Routing**: Create POST `/predict` endpoints mapping inputs to prediction results.
4. **Service Launch**: Expose ASGI server bindings using uvicorn.

## How to Run
Run the deployment application from the repository root:
```bash
python 17_AI_ML_Projects/Advanced_Projects/ML_Model_Deployment_Project/app.py
```

## Results & Future Improvements
- **Results**: API parses JSON payloads and serves predictions under 5 milliseconds.
- **Future Improvements**:
  - Package the API inside a Docker container for cloud cluster deployments.
  - Implement Prometheus metrics logging to track model latency and query load rates.
