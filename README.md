# SaaS Core Microservice Gateway ☁️

![Docker](https://img.shields.io/badge/container-docker-blue.svg)
![FastAPI](https://img.shields.io/badge/fastapi-high_performance-green.svg)

## 🌐 Project Scope
This is the central **API Gateway** for the SaaS platform. It handles authentication routing, rate limiting, and subscription verification for downstream microservices.

## ⚡ Features
* **Asynchronous Processing**: Built on Starlette/FastAPI for high concurrency.
* **Auto-Documentation**: Integrated Swagger UI and ReDoc.
* **Type Safety**: Full Pydantic integration for data validation.

## 🐳 Containerization
The service is fully containerized. To deploy:
```bash
docker build -t saas-gateway .
docker run -p 8000:8000 saas-gateway
