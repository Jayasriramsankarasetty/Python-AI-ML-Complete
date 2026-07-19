"""
Topic:
Model Serving with Flask Microframework

Importance:
Flask is a highly lightweight WSGI microframework.
Many legacy ML deployment systems utilize Flask wrapper endpoints.
Knowing how to parse JSON requests and return structured JSON responses using Flask
is key for legacy support and fast prototyping.

This file covers:
- Concept: WSGI applications, routing decorator syntax, request parsing
- Creating GET health endpoints
- Creating POST predict endpoints with error validation
- Verifying code output using Flask's built-in test_client
"""

# ==========================================
# 1. Concept Explanation & Glossary
# ==========================================
# Flask is a synchronous (WSGI) web microframework:
#   - Routing: Uses @app.route() decorator blocks to bind URLs to handler functions.
#   - JSON Parsing: request.get_json() extracts payload bodies.
#   - JSON Responses: jsonify() converts dictionaries to HTTP JSON responses.
#   - Errors: Return custom status codes (e.g. 400 for bad input, 500 for runtime issues)
#     to provide clean API debugging indicators.

import sys

# Try importing flask; fallback gracefully if not present
use_flask = True
try:
    from flask import Flask, request, jsonify
    print("Using Flask framework.")
except ImportError:
    use_flask = False
    print("Flask not found. Running mock endpoint representation.")

# ==========================================
# 2. Flask App & Routing
# ==========================================
if use_flask:
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({
            "status": "healthy",
            "service": "student_predictor_flask"
        }), 200

    @app.route("/predict", methods=["POST"])
    def predict_exam_status():
        try:
            # Step A: Parse JSON request body
            data = request.get_json()
            if not data:
                return jsonify({"error": "Missing request payload"}), 400
                
            # Step B: Manual validation check
            hours_studied = data.get("hours_studied")
            attendance = data.get("attendance")
            
            if hours_studied is None or attendance is None:
                return jsonify({"error": "Missing hours_studied or attendance keys"}), 400
                
            # Perform value checks
            if not (0.0 <= float(hours_studied) <= 24.0) or not (0.0 <= float(attendance) <= 100.0):
                return jsonify({"error": "Inputs out of boundary bounds"}), 400
                
            # Step C: Mock model prediction
            metric = float(hours_studied) * 10 + float(attendance)
            probability = min(1.0, max(0.0, metric / 200.0))
            prediction = 1 if probability >= 0.55 else 0
            
            # Step D: Return structured JSON
            return jsonify({
                "prediction": prediction,
                "probability": round(probability, 4),
                "status": "success"
            }), 200
            
        except ValueError:
            return jsonify({"error": "Invalid numerical data types"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# ==========================================
# 3. Testing & Execution
# ==========================================
def run_direct_mock_test():
    """
    Use Flask's test_client to verify route logic without locking
    the thread in a blocking server process.
    """
    if use_flask:
        print("\n=======================================")
        print("Testing Flask Route Handlers via test_client:")
        print("=======================================")
        
        # Instantiate test client
        client = app.test_client()
        
        # Test GET /health
        health_resp = client.get("/health")
        print("GET /health output: ", health_resp.get_json())
        print(f"Status Code:        {health_resp.status_code}")
        
        # Test POST /predict with valid payload
        valid_payload = {"hours_studied": 8.0, "attendance": 90.0}
        pred_resp = client.post("/predict", json=valid_payload)
        print("\nPOST /predict (Valid) output: ", pred_resp.get_json())
        print(f"Status Code:                  {pred_resp.status_code}")
        
        # Test POST /predict with invalid payload (trigger validation error)
        invalid_payload = {"hours_studied": 30.0, "attendance": 90.0}
        err_resp = client.post("/predict", json=invalid_payload)
        print("\nPOST /predict (Invalid Input) output: ", err_resp.get_json())
        print(f"Status Code:                          {err_resp.status_code}")
        print("=======================================")
    else:
        print("Flask is not installed. Code is complete and ready for deployment.")

if __name__ == "__main__":
    if "--server" in sys.argv and use_flask:
        app.run(host="127.0.0.1", port=5000)
    else:
        run_direct_mock_test()

"""
Key Takeaways:
- Flask routes HTTP endpoints using decorator syntax binding handler functions.
- Input validation in Flask must be handled manually (checking keys, ranges, and types) unlike FastAPI.
- test_client allows quick validation of API responses without running live networks.

Interview Relevance:
- Contrast Flask and FastAPI validation styles. (FastAPI does validation automatically via Pydantic; Flask requires manual parsing and checking of keys, throwing explicit 400 Bad Request responses for bad input).
- What does WSGI stand for and how does it relate to Flask? (Web Server Gateway Interface. It is the Python standard interface for web applications. Flask is a WSGI application, meaning it runs behind WSGI servers like Gunicorn or uWSGI in production).
- How do you parse JSON payloads in Flask? (By calling `request.get_json()`, which automatically decodes the incoming JSON payload into a Python dictionary).

AI/ML Relevance:
- Microservices: Exposing trained classifiers as microservice endpoints allows non-Python systems (Java, Go, Node.js) to query predictions.
"""
