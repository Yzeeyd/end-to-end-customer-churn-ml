# End-to-End Customer Churn Prediction

An end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn.

The project turns a trained ML model into a complete application with an API, web UI, automated tests, Docker containerization, CI, and AWS serverless deployment.

## Live Demo

**Web UI:**  
https://cfglgiwl5xr6rr2dx7h26ibf4q0gvtau.lambda-url.us-east-1.on.aws/ui/

**API Docs:**  
https://cfglgiwl5xr6rr2dx7h26ibf4q0gvtau.lambda-url.us-east-1.on.aws/docs

> The application runs on AWS Lambda, so the first request after inactivity may take 2-4 minutes because of a cold start.

---

## Architecture

```text
Raw Data
   ↓
Data Cleaning
   ↓
Train / Test Split
   ↓
Scikit-learn Pipeline
   ├── StandardScaler
   └── OneHotEncoder
   ↓
Random Forest
   ↓
Joblib Model Artifact
   ↓
Inference Layer
   ↓
FastAPI
   ├── REST API
   └── Gradio UI
   ↓
Docker
   ↓
Amazon ECR
   ↓
AWS Lambda
   ↓
Public HTTPS URL
```

---

## Machine Learning

The final model is a `RandomForestClassifier` inside a Scikit-learn `Pipeline`.

```python
RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_leaf=2,
    min_samples_split=5,
    class_weight="balanced_subsample",
    random_state=42
)
```

Numerical features are processed with `StandardScaler`.

Categorical features are processed with:

```python
OneHotEncoder(handle_unknown="ignore")
```

The application uses a custom churn probability threshold:

```text
0.46
```

The trained preprocessing pipeline, classifier, and threshold are stored together in:

```text
models/churn_model.joblib
```

---

## API

The backend is built with FastAPI.

### Health Check

```http
GET /
```

### Prediction

```http
POST /predict
```

Example response:

```json
{
  "churn_probability": 0.90,
  "prediction": 1,
  "label": "Churn"
}
```

Pydantic validates incoming customer data before inference.

Interactive Swagger documentation is available at:

```text
/docs
```

---

## Web Interface

A Gradio interface is mounted inside the FastAPI application at:

```text
/ui
```

Users can enter customer information and receive:

- Churn probability
- Prediction
- Churn / No Churn label

---

## Project Structure

```text
end-to-end-customer-churn-ml/
│
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   └── raw/
├── models/
│   └── churn_model.joblib
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── config.py
│   ├── data.py
│   ├── inference.py
│   ├── schemas.py
│   ├── training.py
│   └── ui.py
├── test/
│   ├── test_api.py
│   └── test_predict.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn src.api:app --reload
```

Open:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/ui
```

---

## Train the Model

Training is separated from inference.

```bash
python -m src.training
```

The training flow is:

```text
Load Data
   ↓
Clean Data
   ↓
Split Data
   ↓
Preprocess
   ↓
Train Random Forest
   ↓
Evaluate
   ↓
Save Joblib Artifact
```

The API does not retrain the model when it starts. It loads the saved model artifact for inference.

---

## Docker

Build the image:

```bash
docker build -t churn-api .
```

Run locally:

```bash
docker run --rm -p 8000:8000 churn-api
```

---

## Continuous Integration

GitHub Actions runs automatically when code is pushed to `main`.

```text
Git Push
   ↓
Install Dependencies
   ↓
Run Pytest
   ↓
Build Docker Image
   ↓
Pass / Fail
```

This project currently uses **CI**, not automatic CD deployment.

---

## AWS Deployment

The application is deployed using:

```text
Docker
   ↓
Amazon ECR
   ↓
AWS Lambda
   ↓
Lambda Function URL
```

AWS Lambda allows the application to run on demand instead of keeping a server running continuously.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- FastAPI
- Pydantic
- Gradio
- Pytest
- HTTPX
- Docker
- GitHub Actions
- Amazon ECR
- AWS Lambda

---

## What This Project Demonstrates

- Reproducible ML training pipeline
- Model serialization and inference
- REST API development
- Input validation
- Interactive ML web interface
- Automated testing
- Docker containerization
- Continuous Integration
- AWS container registry
- Serverless cloud deployment
