# _Dockerizing a Python Application_

## This guide walks you through containerizing a Python application with Docker and deploying it to Google Cloud Platform (GCP).

## _Prerequisites_ :

- Docker installed on your system
- Google Cloud CLI (gcloud) installed and authenticated
- Access to a GCP project with Artifact Registry and Cloud Run enabled

## 1. Create Dockerfile and requirements.txt

- Dockerfile: Define the container environment.

- Requirements.txt: List all required Python dependencies.

## 2. Build Docker Image

(IN WINDOWS)

```
docker build -t test-mainmodule2 .
```

(IN LINUX)

```
docker buildx build -t test-mainmodule3 --platform linux/amd64 .
```

## 3. Deploy Docker Images into artifact registry (GCP)

```
gcloud auth configure-docker
```

Format : gcp.io/<-gcp-id->/<-imagesName->

```
docker tag busybox gcr.io/angelic-hold-445702-s1/test-mainmodule3
```

```
docker push gcp.io/angelic-hold-445702-s1/test-mainmodule3
```

## 4. Run The Docker Images In Cloud Run

## **Testing**

docker run -p 8080:8080 test-mainmodule2
