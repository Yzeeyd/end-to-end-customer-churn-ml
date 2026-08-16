from fastapi import FastAPI
import pandas as pd
import gradio as gr


from src.inference import inference
from src.schemas import CustomerInput
from src.ui import create_ui


app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API is running"
    }


@app.post("/predict")
def predict(customer: CustomerInput):

    customer_dict = customer.model_dump(
        by_alias=True
    )

    customer_df = pd.DataFrame(
        [customer_dict]
    )

    result = inference(
        customer_df
    )

    return result

ui = create_ui()

app = gr.mount_gradio_app(
    app,
    ui,
    path="/ui"
)