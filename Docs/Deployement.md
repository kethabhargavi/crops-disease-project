# BIOSCAN Deployment Guide

## 1. Project Overview

BIOSCAN is a Flask-based AI crop disease detection application. The application can be run locally using Python or Docker.

The GitHub Actions pipeline automatically:

1. Installs the Python dependencies.

2. Runs automated tests using Pytest.

3. Builds the Docker image.

4. Publishes the Docker image to GitHub Container Registry.

---

## 2. Run the Application Locally Using Python

### Step 1: Clone the repository

```
git clone https://github.com/kethabhargavi/crops-disease-project.git
cd crops-disease-project
```

### Step 2: Create a virtual environment

```
python -m venv venv
```

### Step 3: Activate the virtual environment on Windows

```
venv\Scripts\activate
```

### Step 4: Install dependencies

```
pip install -r requirements.txt
```

### Step 5: Start the Flask application

```
python app.py
```

Open the application in a browser:

```
http://localhost:5000
```

---

## 3. Run Automated Tests

Run the test suite using:

```
python -m pytest tests/test_app.py -v
```

The tests verify important application functionality such as:

* Login page

* Signup page

* User signup

* User login

* Protected route access

* Authentication redirects

---

## 4. Build the Docker Image

Build the Docker image from the project root:

```
docker build -t bioscan .
```

Verify that the image exists:

```
docker images
```

---

## 5. Run BIOSCAN Using Docker

Start a container:

```
docker run --name bioscan_app -p 5000:5000 bioscan
```

Open the application:

```
http://localhost:5000
```

Check running containers:

```
docker ps
```

Stop the container:

```
docker stop bioscan_app
```

Start the existing container again:

```
docker start bioscan_app
```

Remove the container:

```
docker rm bioscan_app
```

---

## 6. GitHub Actions CI/CD

The workflow is located at:

```
.github/workflows/ci-cd.yml
```

The pipeline is triggered when code is pushed to the `master` branch or when a pull request targets the `master` branch.

### Pipeline process

```
Developer
   ↓
GitHub Repository
   ↓
GitHub Actions
   ↓
Install Dependencies
   ↓
Run Pytest
   ↓
Build Docker Image
   ↓
Push Image to GHCR
```

The Docker image is published to GitHub Container Registry.

---

## 7. Pull the Docker Image from GHCR

The published image can be pulled using:

```
docker pull ghcr.io/kethabhargavi/crops-disease-project:latest
```

Run the downloaded image:

```
docker run --name bioscan_ghcr -p 5000:5000 ghcr.io/kethabhargavi/crops-disease-project:latest
```

Open:

```
http://localhost:5000
```

---

## 8. Deployment Status

| Component                 | Status    |
| ------------------------- | --------- |
| Flask application         | Completed |
| Local Python execution    | Completed |
| Automated tests           | Completed |
| Docker image build        | Completed |
| Local Docker deployment   | Completed |
| GitHub Actions CI/CD      | Completed |
| GitHub Container Registry | Completed |
| AWS deployment            | Planned   |

## 9. Future Deployment

The next deployment phase may include:

* Deploying the Docker container to AWS EC2

* Configuring AWS security groups

* Adding HTTPS

* Adding application monitoring with CloudWatch

* Managing infrastructure using Terraform

AWS deployment is not included in the current implementation.

## 2. Add and push the file

Open Command Prompt in your project folder and run:

Bash

```
cd C:\Users\ketha\crops-disease-project
git add Docs/deployment.md
git commit -m "Add deployment documentation"
git pull --rebase origin master
git push origin master
```

After pushing, GitHub Actions should automatically run again. Check that the latest BIOSCAN CI/CD workflow is green.
