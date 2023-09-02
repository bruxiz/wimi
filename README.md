# WIMI - What Is My IP

## WIMI is a web app built using Python and Flask that displays user's IP address.

### CI/CD process visualized below:

![img.png](img.png)

[dockerhub image](https://hub.docker.com/r/bruxiz/wimi)

## Prerequisites

- Python3 (https://www.python.org/downloads/)
- Docker (https://docs.docker.com/engine/install/)
- Helm (https://helm.sh/docs/intro/install/)
- Task (https://taskfile.dev/installation/)

## Installation

### Clone the Repository

```bash
git clone https://github.com/your_username/wimi.git
cd wimi
```

#### Install Python Dependencies
```bash
pip3 install -r requirements.txt
```

## Using Taskfile

The `Taskfile` can automate various tasks like building the Docker image, publishing it, and running tests. Below are some example usages:

#### Build Docker Image

```bash
task build VERSION=$your_verison
```

#### Publish Docker Image

```bash
task publish VERSION=$your_verison REGISTRY=$your_registry_url DOCKER_USERNAME=$your_username DOCKER_PASSWORD=$your_password
```

#### Run Tests

```bash
task test
```

#### Helm Deployment

The `helm` directory contains Helm charts for deploying this application to a Kubernetes cluster. To deploy the application, run:

```bash
helm install wimi ./helm
```
