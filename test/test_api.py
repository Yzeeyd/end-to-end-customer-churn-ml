from fastapi.testclient import TestClient

from src.api import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_predict():

    customer = {
        "Gender": "Male",
        "Senior Citizen": "Yes",
        "Partner": "No",
        "Dependents": "No",
        "Tenure Months": 2,
        "Phone Service": "Yes",
        "Multiple Lines": "Yes",
        "Internet Service": "Fiber optic",
        "Online Security": "No",
        "Online Backup": "No",
        "Device Protection": "No",
        "Tech Support": "No",
        "Streaming TV": "Yes",
        "Streaming Movies": "Yes",
        "Contract": "Month-to-month",
        "Paperless Billing": "Yes",
        "Payment Method": "Electronic check",
        "Monthly Charges": 105.5,
        "Total Charges": 211.0
    }

    response = client.post(
        "/predict",
        json=customer
    )

    assert response.status_code == 200

    result = response.json()

    assert "churn_probability" in result
    assert "prediction" in result
    assert "label" in result

def test_invalid_tenure():

    customer = {
        "Gender": "Male",
        "Senior Citizen": "Yes",
        "Partner": "No",
        "Dependents": "No",
        "Tenure Months": -10,
        "Phone Service": "Yes",
        "Multiple Lines": "Yes",
        "Internet Service": "Fiber optic",
        "Online Security": "No",
        "Online Backup": "No",
        "Device Protection": "No",
        "Tech Support": "No",
        "Streaming TV": "Yes",
        "Streaming Movies": "Yes",
        "Contract": "Month-to-month",
        "Paperless Billing": "Yes",
        "Payment Method": "Electronic check",
        "Monthly Charges": 105.5,
        "Total Charges": 211.0
    }

    response = client.post(
        "/predict",
        json=customer
    )

    assert response.status_code == 422

