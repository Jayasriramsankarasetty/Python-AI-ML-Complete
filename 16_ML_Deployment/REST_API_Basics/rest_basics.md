# REST API Basics for Machine Learning Serving

To deploy models, you must wrap prediction functions inside an HTTP endpoint (API) so external clients can request predictions.

---

## 1. Core HTTP Methods (Verbs)

* **GET**: Requests data from the server. Used for health checks, model information, or status checks. (Has no request payload body).
* **POST**: Sends new data payloads to the server. Used for model serving predictions, where we send a JSON feature payload to `/predict` and receive predicted outputs.
* **PUT/PATCH**: Updates existing data on the server. Used to update active model endpoints or parameters.
* **DELETE**: Deletes resource data. Used to offload/de-register active models from serving memories.

---

## 2. Request Components

1. **URL & Endpoints**: The routing address (e.g. `http://api.company.com/v1/predict`).
2. **Headers**: Key-value pairs containing request metadata (e.g. `Content-Type: application/json` or auth headers `Authorization: Bearer <TOKEN>`).
3. **Query Parameters**: Key-values appended directly to the URL (e.g. `/predict?version=2.1`).
4. **Path Parameters**: Variables embedded in the URL path itself (e.g. `/models/{model_id}/status`).
5. **Request Body**: The data payload sent with POST requests, usually structured in JSON format:
   ```json
   {
       "hours_studied": 8.5,
       "attendance": 90.0
   }
   ```

---

## 3. HTTP Status Codes

* **2xx (Success)**:
  * `200 OK`: Request succeeded (standard response for predictions).
  * `201 Created`: Resource successfully created.
* **4xx (Client Error)**:
  * `400 Bad Request`: Invalid request data (e.g. missing keys or invalid input values).
  * `401 Unauthorized`: Missing or invalid authentication token.
  * `404 Not Found`: Endpoint or resource does not exist.
  * `422 Unprocessable Entity`: Validation failure (FastAPI standard for incorrect schema types).
* **5xx (Server Error)**:
  * `500 Internal Server Error`: The server encountered a crash or python code error during execution.
