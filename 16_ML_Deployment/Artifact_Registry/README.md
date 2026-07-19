# Google Cloud Artifact Registry Configuration

Google Cloud Artifact Registry is the next-generation container storage registry on GCP, replacing the deprecated Google Container Registry (GCR). It stores, manages, and secures Docker container images.

---

## Configuration Steps Roadmap

### Step 1: Enable the Artifact Registry API
Ensure the registry api is activated on your project:
```bash
gcloud services enable artifactregistry.googleapis.com
```

### Step 2: Create a Docker Repository
Create a secure repository to store container images:
* `--repository-format=docker`: Sets format target.
* `--location=us-central1`: Defines physical region storage.
```bash
gcloud artifacts repositories create ml-repo \
    --repository-format=docker \
    --location=us-central1 \
    --description="Repository for ML model containers"
```

### Step 3: Configure Docker Authentication
Configure your local Docker daemon terminal client to authenticate securely with GCP repositories:
* This command updates your local `config.json` helper settings.
```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```

### Step 4: Tag and Push (Summary)
Once authenticated, you tag your local image to the repository format structure and push it:
```bash
# Tag locally
docker tag student-api:v1 us-central1-docker.pkg.dev/my-gcp-project/ml-repo/student-api:v1

# Push to Artifact Registry
docker push us-central1-docker.pkg.dev/my-gcp-project/ml-repo/student-api:v1
```
