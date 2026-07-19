# Serverless Deployment on GCP Cloud Run

Google Cloud Run is a managed serverless compute platform that runs containerized applications. It automatically scales containers up and down (down to zero when idle), ensuring cost efficiency for model deployment.

---

## Deployment Steps Roadmap

### Prerequisite: Authenticate Google Cloud CLI
Initialize configurations and login to your Google Cloud Account:
```bash
gcloud init
gcloud auth login
```

### Step 1: Tag the Docker Container
Tag your built local Docker image to point to Google's Artifact Registry server path:
* Format: `[REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY]/[IMAGE_NAME]:[TAG]`
```bash
docker tag student-api:v1 us-central1-docker.pkg.dev/my-gcp-project/ml-repo/student-api:v1
```

### Step 2: Push Image to Artifact Registry
Upload the tagged container image to the cloud:
```bash
docker push us-central1-docker.pkg.dev/my-gcp-project/ml-repo/student-api:v1
```

### Step 3: Deploy to Cloud Run
Run the deployment command:
* `--image`: Specifies the image path in Artifact Registry.
* `--platform managed`: Tells gcloud to host it fully managed.
* `--allow-unauthenticated`: Exposes the endpoint to the public internet (necessary for public client access).
```bash
gcloud run deploy student-service \
    --image us-central1-docker.pkg.dev/my-gcp-project/ml-repo/student-api:v1 \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```

### Step 4: Verification
Once deployment completes, the gcloud CLI outputs the live HTTPS endpoint URL (e.g. `https://student-service-xyz.run.app`).
Verify the deployment by triggering a POST request using `curl`:
```bash
curl -X POST https://student-service-xyz.run.app/predict \
     -H "Content-Type: application/json" \
     -d '{"hours_studied": 8.0, "attendance": 90.0}'
```
