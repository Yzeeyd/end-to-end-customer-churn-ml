import pandas as pd
import numpy as np

def CleanData(
        FilePath:str ,
        col_drop:list[str],
        col_num:list[str],
        col_target:str
        )  -> tuple[pd.DataFrame, pd.Series]:

    # Read Data 
    df = pd.read_csv(FilePath)

    # 1) Data Cleaning 
        # a) Drop Columns 
    df.drop(columns=col_drop, inplace=True, errors='ignore')
    df = df.replace(" ",np.nan)

        # b) Make Sure all numerical data is numerical and fill the null value
    for col in col_num:
        df[col] = pd.to_numeric(df[col])
    
    mask = df["Total Charges"].isna()
    df.loc[mask, "Total Charges"] = ( df.loc[mask, "Tenure Months"] * df.loc[mask, "Monthly Charges"] )

    
    x = df.drop(col_target,axis=1)
    y = df[col_target]
    return x,y


