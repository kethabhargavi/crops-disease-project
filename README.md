# 🌱 BIOSCAN — AI Crop Disease Detection Platform

BIOSCAN is an AI-powered crop health platform designed to help identify crop diseases from uploaded images.

The application is built using Python and Flask and integrates a machine-learning model for crop disease prediction.

Along with the application, this project demonstrates a practical DevOps workflow using Git, GitHub, Docker, GitHub Actions, automated testing, and GitHub Container Registry.

---

## 🚀 Project Overview

BIOSCAN provides a web-based interface where users can:

- Create an account
- Login securely
- Access the BIOSCAN application
- Upload crop images
- Detect potential crop diseases
- View crop-health related information

The application is containerized using Docker and integrated with a CI/CD pipeline using GitHub Actions.

Every code push to the `master` branch triggers the CI/CD workflow.

---

# 🏗️ Architecture

```text
                         Developer
                             │
                             │ git push
                             ▼
                    ┌─────────────────┐
                    │     GitHub      │
                    │   Repository    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ GitHub Actions  │
                    │     CI/CD       │
                    └────────┬────────┘
                             │
                    ┌────────┴─────────┐
                    │                  │
                    ▼                  ▼
              ┌──────────┐      ┌──────────────┐
              │  Pytest  │      │ Docker Build │
              │   Tests  │      │              │
              └────┬─────┘      └──────┬───────┘
                   │                   │
                   │ PASS              ▼
                   │            ┌──────────────┐
                   │            │ Docker Image │
                   │            └──────┬───────┘
                   │                   │
                   │                   ▼
                   │          ┌──────────────────┐
                   │          │ GitHub Container │
                   │          │     Registry      │
                   │          └──────────────────┘
                   │
                   ▼
              CI Successful
````

---

# 🛠️ Technology Stack

## Application

* Python
* Flask
* OpenCV
* NumPy
* Scikit-learn
* HTML
* CSS
* JavaScript

## Testing

* Pytest

## DevOps

* Git
* GitHub
* GitHub Actions
* Docker
* GitHub Container Registry (GHCR)

## Planned Cloud Deployment

* AWS EC2
* AWS Security Groups
* AWS CloudWatch
* SSH

---

# 📂 Project Structure

```text
crops-disease-project/
│
├── app.py
├── README.md
├── requirements.txt
├── Dockerfile
│
├── model/
│   └── model.pkl
│
├── tests/
│   └── test_app.py
│
├── templates/
│   ├── ...
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── ...
│
├── images/
│   ├── homepage.png
│   ├── prediction1.png
│   └── ...
│
└── .github/
    └── workflows/
        └── ci-cd.yml
```

---

# 🔄 CI/CD Pipeline

The project uses GitHub Actions to automate testing and Docker image publishing.

The pipeline is triggered when code is pushed to the `master` branch or when a pull request targets the `master` branch.

```text
Developer
    │
    ▼
git push
    │
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ▼
Install Dependencies
    │
    ▼
Run Pytest
    │
    ├── FAIL ──► Pipeline stops
    │
    └── PASS
          │
          ▼
     Docker Build
          │
          ▼
      Docker Image
          │
          ▼
         GHCR
```

---

# 🧪 Automated Testing

The project contains automated tests using Pytest.

The CI pipeline executes:

```bash
python -m pytest tests/test_app.py -v
```

The tests verify application functionality such as:

* Login page
* Signup page
* Authentication behavior
* Protected routes
* Signup functionality
* Login functionality

The Docker stage depends on the test stage.

```yaml
needs: test
```

This means the Docker image will only be built and pushed if the tests pass successfully.

---

# 🐳 Docker

The Flask application is containerized using Docker.

## Build the Docker Image

```bash
docker build -t bioscan .
```

## Run the Container

```bash
docker run --name bioscan_app -p 5000:5000 bioscan
```

The application can then be accessed at:

```text
http://localhost:5000
```

## Check Running Containers

```bash
docker ps
```

## Stop the Container

```bash
docker stop bioscan_app
```

## Start the Container Again

```bash
docker start bioscan_app
```

---

# 📦 GitHub Container Registry

The Docker image is automatically published to GitHub Container Registry through GitHub Actions.

Container package:

```text
crops-disease-project
```

The workflow performs:

```text
Docker Login
     ↓
Docker Build
     ↓
Docker Push
     ↓
GitHub Container Registry
```

The image is tagged as:

```text
ghcr.io/kethabhargavi/crops-disease-project:latest
```

The image can be pulled using:

```bash
docker pull ghcr.io/kethabhargavi/crops-disease-project:latest
```

---

# ⚙️ GitHub Actions Workflow

The project uses the following CI/CD stages:

### Stage 1 — Testing

```text
Checkout Code
      ↓
Setup Python 3.10
      ↓
Install Dependencies
      ↓
Run Pytest
```

### Stage 2 — Docker

```text
Checkout Code
      ↓
Login to GHCR
      ↓
Build Docker Image
      ↓
Push Docker Image
```

The Docker stage uses:

```yaml
needs: test
```

Therefore, Docker publishing only occurs after successful testing.

---

# 🔐 GitHub Actions Permissions

The workflow uses:

```yaml
permissions:
  contents: read
  packages: write
```

These permissions allow GitHub Actions to:

* Read the repository source code
* Publish the Docker image to GitHub Container Registry

The workflow authenticates to GHCR using:

```yaml
password: ${{ secrets.GITHUB_TOKEN }}
```

No personal access token is hard-coded into the repository.

---

# 💻 Local Development

## Clone the Repository

```bash
git clone https://github.com/kethabhargavi/crops-disease-project.git
```

Move into the project:

```bash
cd crops-disease-project
```

## Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Flask Application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

# 🧪 Run Tests Locally

Run:

```bash
python -m pytest tests/test_app.py -v
```

The same test command is used by GitHub Actions.

This ensures that the code tested locally is also tested automatically in CI.

---

# 🔁 Git Workflow

The development workflow used in this project is:

```text
Modify Code
    ↓
Run Tests Locally
    ↓
git add .
    ↓
git commit
    ↓
git push
    ↓
GitHub Actions
    ↓
Automated Tests
    ↓
Docker Build
    ↓
Docker Push
```

Common commands:

```bash
git status
git add .
git commit -m "Update BIOSCAN application"
git push origin master
```

---

# 📊 Current DevOps Implementation

| Component                   | Status       |
| --------------------------- | ------------ |
| Flask Application           | ✅ Completed  |
| Machine Learning Model      | ✅ Integrated |
| Git Repository              | ✅ Completed  |
| GitHub Repository           | ✅ Completed  |
| Automated Tests             | ✅ Completed  |
| Pytest CI                   | ✅ Completed  |
| Dockerfile                  | ✅ Completed  |
| Docker Image                | ✅ Completed  |
| Local Docker Deployment     | ✅ Completed  |
| GitHub Actions              | ✅ Completed  |
| Docker Build in CI          | ✅ Completed  |
| GitHub Container Registry   | ✅ Completed  |
| Automatic Docker Image Push | ✅ Completed  |
| AWS EC2 Deployment          | 🔄 Planned   |
| CloudWatch Monitoring       | 🔄 Planned   |
| Terraform Infrastructure    | 🔄 Planned   |

---

# 🎯 DevOps Skills Demonstrated

This project demonstrates practical experience with:

### Linux / Command Line

* Application execution
* Environment management
* Docker CLI
* Git CLI

### Git & GitHub

* Repository management
* Commits
* Pushes
* Branches
* GitHub Actions

### CI/CD

* Automated testing
* Pipeline stages
* Job dependencies
* Automated Docker builds
* Automated image publishing

### Docker

* Dockerfile
* Image creation
* Container execution
* Port mapping
* Container lifecycle
* Container Registry

### Testing

* Pytest
* Automated application testing
* CI test execution

---

# 🚀 Future Deployment Architecture

The next phase of the project is cloud deployment.

The planned architecture is:

```text
                    GitHub
                       │
                       ▼
                GitHub Actions
                  │         │
                  ▼         ▼
               Pytest    Docker Build
                            │
                            ▼
                           GHCR
                            │
                            ▼
                        AWS EC2
                            │
                       Docker Run
                            │
                            ▼
                     BIOSCAN Flask
                            │
                            ▼
                         Users
```

Planned AWS components:

* EC2
* Security Groups
* IAM
* SSH
* CloudWatch

Infrastructure automation can later be added using Terraform.

---

# 🔒 Security Considerations

The project follows basic security practices:

* GitHub Actions uses `GITHUB_TOKEN`
* Secrets are not hard-coded in source code
* Dependencies are installed from `requirements.txt`
* Docker isolates the application environment
* Authentication is implemented for protected application routes

For production deployment, additional security measures will be added, including:

* HTTPS
* Secure environment variables
* Production secret management
* Restricted security-group rules
* Application logging
* Monitoring

---

# 📸 Project Evidence

The repository contains evidence of the DevOps implementation, including:

* BIOSCAN application
* Docker deployment
* GitHub Actions successful runs
* Automated test execution
* Docker image build
* GitHub Container Registry package

---

# 👩‍💻 Developer

**Bhargavi Ketha**

AWS DevOps / Cloud & DevOps Fresher

Skills demonstrated through this project:

```text
Python
Flask
Git
GitHub
Linux
Docker
GitHub Actions
CI/CD
Pytest
AWS
```

---

# 📌 Key Project Outcome

BIOSCAN demonstrates how a Python Flask application can be transformed from a local application into a containerized application with an automated CI/CD workflow.

The implemented pipeline automatically:

1. Retrieves the latest source code
2. Installs Python dependencies
3. Runs automated tests
4. Builds a Docker image
5. Authenticates with GitHub Container Registry
6. Publishes the Docker image

This creates a repeatable and automated software delivery process.

