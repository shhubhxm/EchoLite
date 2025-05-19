# EchoLite — Scalable Real-Time Model Inference System

EchoLite is an open-source ML inference platform developed as part of a volunteer initiative at the **Frugal Innovation Hub**, aimed at supporting low-resource and humanitarian technology solutions. Built with **Ray Serve**, **PyTorch**, and **Kubernetes on GCP**, EchoLite delivers fast, reliable, and scalable model serving for speech and language understanding models (e.g., DistilBERT, Whisper), tailored for deployment in bandwidth-constrained or mission-critical environments.

---

## Features

- **Ray Serve + FastAPI**: Distributed model serving using async APIs
- **PyTorch + Transformers**: Run optimized NLP models like DistilBERT
- **TorchScript/ONNX Ready**: Inference-ready PyTorch optimizations
- **Autoscaling on GKE**: Kubernetes-based HPA via custom Ray metrics
- **CI/CD with GitHub Actions**: Auto-deploy to GCP via Terraform & Helm

---

## Architecture

```mermaid
graph TD
    Client -->|HTTP POST| FastAPI
    FastAPI --> RayServe
    RayServe --> PyTorchModel
    PyTorchModel -->|Predictions| FastAPI
    FastAPI -->|Response| Client

    subgraph GCP Infrastructure
        FastAPI
        RayServe
        Prometheus
    end
````

---

## Tech Stack

* **Language & Frameworks**: Python, FastAPI, PyTorch, Transformers
* **Inference Orchestration**: Ray Serve
* **Infrastructure**: GCP GKE, Docker, Terraform, Helm
* **Monitoring**: Prometheus + Grafana
* **CI/CD**: GitHub Actions

---

## How to Run Locally

```bash
# Clone repo
git clone https://github.com/shhubhxm/EchoLite && cd echolite

# Create virtual env
python -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Ray Serve locally
ray start --head

# Launch FastAPI app via Ray
python app/ray_serve_deployment.py
```

---

## GCP Deployment

1. Configure `terraform/` with your GCP credentials and project.
2. Use Helm to deploy your Docker image to GKE.
3. CI/CD workflow in `.github/workflows/deploy.yml` handles build and rollout.

---

## Example Request

```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "I love this project!"}'
```

---

## Future Improvements

* Add Whisper-based speech inference
* Integrate ONNX + quantization for smaller models
* Advanced load testing with Locust or Vegeta

---

## Inspiration

This project is inspired by industrial-scale AI systems and serves as a learning sandbox to implement:

* Real-time model serving
* Scalable autoscaling strategies
* End-to-end MLOps deployment pipelines

