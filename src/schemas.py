from typing import Literal
from pydantic import BaseModel, Field, ConfigDict


YesNo = Literal["Yes", "No"]

InternetService = Literal[
    "DSL",
    "Fiber optic",
    "No"
]

InternetFeature = Literal[
    "Yes",
    "No",
    "No internet service"
]

MultipleLines = Literal[
    "Yes",
    "No",
    "No phone service"
]

ContractType = Literal[
    "Month-to-month",
    "One year",
    "Two year"
]

PaymentMethod = Literal[
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
]


class CustomerInput(BaseModel):

    model_config = ConfigDict(
        populate_by_name=True,
        extra="forbid"
    )

    Gender: Literal["Male", "Female"]

    Senior_Citizen: YesNo = Field(
        alias="Senior Citizen"
    )

    Partner: YesNo
    Dependents: YesNo

    Tenure_Months: int = Field(
        alias="Tenure Months",
        ge=0,
        le=100
    )

    Phone_Service: YesNo = Field(
        alias="Phone Service"
    )

    Multiple_Lines: MultipleLines = Field(
        alias="Multiple Lines"
    )

    Internet_Service: InternetService = Field(
        alias="Internet Service"
    )

    Online_Security: InternetFeature = Field(
        alias="Online Security"
    )

    Online_Backup: InternetFeature = Field(
        alias="Online Backup"
    )

    Device_Protection: InternetFeature = Field(
        alias="Device Protection"
    )

    Tech_Support: InternetFeature = Field(
        alias="Tech Support"
    )

    Streaming_TV: InternetFeature = Field(
        alias="Streaming TV"
    )

    Streaming_Movies: InternetFeature = Field(
        alias="Streaming Movies"
    )

    Contract: ContractType

    Paperless_Billing: YesNo = Field(
        alias="Paperless Billing"
    )

    Payment_Method: PaymentMethod = Field(
        alias="Payment Method"
    )

    Monthly_Charges: float = Field(
        alias="Monthly Charges",
        ge=0
    )

    Total_Charges: float = Field(
        alias="Total Charges",
        ge=0
    )