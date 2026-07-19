# Automated MLOps CI/CD Pipelines with GitHub Actions

Continuous Integration and Continuous Deployment (CI/CD) automates testing and deployment steps. When a developer pushes code updates to GitHub:
1. **CI**: Automated tests (using `pytest`) verify model performance and API schemas are functional.
2. **CD**: The container is automatically built, uploaded to GCP Artifact Registry, and deployed live to GCP Cloud Run.

---

## GitHub Actions CI/CD Pipeline Template

Create a file named `.github/workflows/deploy.yml` at the root of the repository:

```yaml
name: ML Model serving CI/CD Pipeline

on:
  push:
    branches:
      - main  # Trigger pipeline when pushes land on main branch

env:
  PROJECT_ID: my-gcp-project
  REGION: us-central1
  REPOSITORY: ml-repo
  IMAGE_NAME: student-api
  SERVICE_NAME: student-service

jobs:
  # Job 1: Continuous Integration (Test the code)
  continuous_integration:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-size: '3.10'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest fastapi pydantic uvicorn numpy scikit-learn

      - name: Run Tests
        run: |
          # Runs test routines to verify endpoint schemas and math matrices
          pytest

  # Job 2: Continuous Deployment (Build container & deploy to GCP)
  continuous_deployment:
    needs: continuous_integration  # Only run CD if tests pass
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Authenticate with Google Cloud
        uses: google-github-actions/auth@v1
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }} # Secure Service Account key stored in GitHub secrets

      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v1

      - name: Configure Docker Auth
        run: |
          gcloud auth configure-docker ${{ env.REGION }}-docker.pkg.dev

      - name: Build and Push Docker Image
        run: |
          IMAGE_PATH="${{ env.REGION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPOSITORY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}"
          docker build -t $IMAGE_PATH -f 16_ML_Deployment/Docker/Dockerfile .
          docker push $IMAGE_PATH

      - name: Deploy to Google Cloud Run
        run: |
          IMAGE_PATH="${{ env.REGION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPOSITORY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}"
          gcloud run deploy ${{ env.SERVICE_NAME }} \
            --image $IMAGE_PATH \
            --region ${{ env.REGION }} \
            --platform managed \
            --allow-unauthenticated
```
