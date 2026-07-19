# ==========================================
# 1. Base Image selection
# ==========================================
# Use a lightweight python base image to minimize container size
FROM python:3.10-slim

# ==========================================
# 2. Set Working Directory
# ==========================================
# Set working directory inside the container
WORKDIR /app

# ==========================================
# 3. Environment Variables
# ==========================================
# Prevent Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# ==========================================
# 4. Install Dependencies
# ==========================================
# We copy requirements first to leverage Docker's layer caching.
# If requirements.txt doesn't change, Docker will skip installing dependencies.
# (We install directly inside the container since it is already isolated).
RUN pip install --no-cache-dir fastapi uvicorn pydantic scikit-learn numpy

# ==========================================
# 5. Copy Application Code
# ==========================================
# Copy the FastAPI directory contents into the container /app directory
COPY ../FastAPI/api_fastapi.py /app/main.py

# ==========================================
# 6. Port Binding
# ==========================================
# Inform Docker that the container listens on port 8000 at runtime
EXPOSE 8000

# ==========================================
# 7. Start Command
# ==========================================
# Start uvicorn server binding to 0.0.0.0 (necessary to expose it outside the container)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
