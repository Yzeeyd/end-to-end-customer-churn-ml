import gradio as gr
import pandas as pd

from src.inference import inference


def predict_ui(
    gender,
    senior_citizen,
    partner,
    dependents,
    tenure_months,
    phone_service,
    multiple_lines,
    internet_service,
    online_security,
    online_backup,
    device_protection,
    tech_support,
    streaming_tv,
    streaming_movies,
    contract,
    paperless_billing,
    payment_method,
    monthly_charges,
    total_charges
):

    customer = pd.DataFrame([{
        "Gender": gender,
        "Senior Citizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure Months": tenure_months,
        "Phone Service": phone_service,
        "Multiple Lines": multiple_lines,
        "Internet Service": internet_service,
        "Online Security": online_security,
        "Online Backup": online_backup,
        "Device Protection": device_protection,
        "Tech Support": tech_support,
        "Streaming TV": streaming_tv,
        "Streaming Movies": streaming_movies,
        "Contract": contract,
        "Paperless Billing": paperless_billing,
        "Payment Method": payment_method,
        "Monthly Charges": monthly_charges,
        "Total Charges": total_charges
    }])

    result = inference(customer)

    return (
        result["churn_probability"],
        result["label"]
    )


def create_ui():

    with gr.Blocks() as demo:

        gr.Markdown(
            "# Customer Churn Prediction"
        )

        gr.Markdown(
            "Enter customer information to predict churn risk."
        )

        with gr.Row():

            gender = gr.Dropdown(
                ["Male", "Female"],
                label="Gender"
            )

            senior_citizen = gr.Dropdown(
                ["Yes", "No"],
                label="Senior Citizen"
            )

            partner = gr.Dropdown(
                ["Yes", "No"],
                label="Partner"
            )

            dependents = gr.Dropdown(
                ["Yes", "No"],
                label="Dependents"
            )

        tenure_months = gr.Number(
            label="Tenure Months"
        )

        phone_service = gr.Dropdown(
            ["Yes", "No"],
            label="Phone Service"
        )

        multiple_lines = gr.Dropdown(
            ["Yes", "No", "No phone service"],
            label="Multiple Lines"
        )

        internet_service = gr.Dropdown(
            ["DSL", "Fiber optic", "No"],
            label="Internet Service"
        )

        online_security = gr.Dropdown(
            ["Yes", "No", "No internet service"],
            label="Online Security"
        )

        online_backup = gr.Dropdown(
            ["Yes", "No", "No internet service"],
            label="Online Backup"
        )

        device_protection = gr.Dropdown(
            ["Yes", "No", "No internet service"],
            label="Device Protection"
        )

        tech_support = gr.Dropdown(
            ["Yes", "No", "No internet service"],
            label="Tech Support"
        )

        streaming_tv = gr.Dropdown(
            ["Yes", "No", "No internet service"],
            label="Streaming TV"
        )

        streaming_movies = gr.Dropdown(
            ["Yes", "No", "No internet service"],
            label="Streaming Movies"
        )

        contract = gr.Dropdown(
            [
                "Month-to-month",
                "One year",
                "Two year"
            ],
            label="Contract"
        )

        paperless_billing = gr.Dropdown(
            ["Yes", "No"],
            label="Paperless Billing"
        )

        payment_method = gr.Dropdown(
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ],
            label="Payment Method"
        )

        monthly_charges = gr.Number(
            label="Monthly Charges"
        )

        total_charges = gr.Number(
            label="Total Charges"
        )

        predict_button = gr.Button(
            "Predict Churn"
        )

        probability = gr.Number(
            label="Churn Probability"
        )

        prediction = gr.Textbox(
            label="Prediction"
        )

        predict_button.click(
            fn=predict_ui,
            inputs=[
                gender,
                senior_citizen,
                partner,
                dependents,
                tenure_months,
                phone_service,
                multiple_lines,
                internet_service,
                online_security,
                online_backup,
                device_protection,
                tech_support,
                streaming_tv,
                streaming_movies,
                contract,
                paperless_billing,
                payment_method,
                monthly_charges,
                total_charges
            ],
            outputs=[
                probability,
                prediction
            ]
        )

    return demo