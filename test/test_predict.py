import pandas as pd

from src.inference import inference


def test_inference_output():

    customer = pd.DataFrame([{
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
    }])

    result = inference(customer)

    assert "churn_probability" in result
    assert "prediction" in result
    assert "label" in result

    assert 0 <= result["churn_probability"] <= 1

    assert result["prediction"] in [0, 1]

    assert result["label"] in ["Churn", "No Churn"]

def test_prediction_label():

    customer = pd.DataFrame([{
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
    }])

    result = inference(customer)

    if result["prediction"] == 1:
        assert result["label"] == "Churn"
    else:
        assert result["label"] == "No Churn"
