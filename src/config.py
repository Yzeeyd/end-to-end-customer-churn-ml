FILE_PATH = "data/raw/Telco_customer_churn.csv"

ARTIFACT_PATH = "models/churn_model.joblib"

THRESHOLD = 0.46

TARGET = "Churn Value"


COL_DROP = [
    "CustomerID",
    "Count",
    "Country",
    "State",
    "City",
    "Zip Code",
    "Lat Long",
    "Latitude",
    "Longitude",
    "Churn Label",
    "Churn Score",
    "CLTV",
    "Churn Reason"
]


CATEGORICAL = [
    "Gender",
    "Senior Citizen",
    "Partner",
    "Dependents",
    "Phone Service",
    "Multiple Lines",
    "Internet Service",
    "Online Security",
    "Online Backup",
    "Device Protection",
    "Tech Support",
    "Streaming TV",
    "Streaming Movies",
    "Contract",
    "Paperless Billing",
    "Payment Method"
]


NUMERICAL = [
    "Tenure Months",
    "Monthly Charges",
    "Total Charges"
]