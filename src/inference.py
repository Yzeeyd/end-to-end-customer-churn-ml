import joblib
import pandas as pd
import json

from src.config import ARTIFACT_PATH


# load Model once so not load on each call inference function
artifact = joblib.load(ARTIFACT_PATH)

loaded_model = artifact["model"]
loaded_threshold = artifact["threshold"]

def inference(customer_data: pd.DataFrame):

    probability = loaded_model.predict_proba(customer_data)[:, 1]

    prediction = (
        probability >= loaded_threshold
    ).astype(int)


    probability = float(probability[0])
    prediction = int(prediction[0])


    Output = {
        "churn_probability": probability,
        "prediction": prediction,
        "label": "Churn" if prediction == 1 else "No Churn"
    }
    return Output





customer = pd.DataFrame([{
    "Gender": "Male",
    "Senior Citizen": "No",
    "Partner": "No",
    "Dependents": "No",
    "Tenure Months": 2,
    "Phone Service": "Yes",
    "Multiple Lines": "No",
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
    "Monthly Charges": 95.5,
    "Total Charges": 191.0
}])

if __name__ =="__main__" :
    result = inference(customer)

    json_output = json.dumps(
        result,
        indent=4
    )

    print(json_output)