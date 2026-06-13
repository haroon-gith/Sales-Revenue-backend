
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib
 
app = FastAPI()
 
# Load model files
model = joblib.load("Random_Forest_model.pkl")
scaler = joblib.load("Scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")
 
# Input data ka format
class SalesInput(BaseModel):
    quantity: int
    discount: float
    profit: float
    order_month: int
    order_quarter: int
    shipping_delay: int
    segment: str        # "Consumer", "Corporate", "Home Office"
    ship_mode: str      # "First Class", "Same Day", "Second Class", "Standard Class"
    region: str         # "Central", "East", "South", "West"
    category: str       # "Furniture", "Office Supplies", "Technology"
 
@app.get("/")
def home():
    return {"message": "API chal rahi hai!"}
 
@app.post("/predict")
def predict(data: SalesInput):
    # Step 1: Input ko DataFrame banao
    input_dict = {
        "Quantity": data.quantity,
        "Discount": data.discount,
        "Profit": data.profit,
        "Order_Month": data.order_month,
        "Order_Quarter": data.order_quarter,
        "Shipping_Delay": data.shipping_delay,
        "Segment": data.segment,
        "Ship Mode": data.ship_mode,
        "Region": data.region,
        "Category": data.category,
    }
    df = pd.DataFrame([input_dict])
 
    # Step 2: Encoding karo (bilkul notebook ki tarah)
    df_encoded = pd.get_dummies(df, drop_first=True)
 
    # Step 3: Training wale columns se match karo
    df_aligned = df_encoded.reindex(columns=feature_columns, fill_value=0)
 
    # Step 4: Scale karo
    scaled = scaler.transform(df_aligned)
 
    # Step 5: Predict karo
    log_prediction = model.predict(scaled)[0]
    actual_sales = float(np.expm1(log_prediction))  # log1p reverse karo
 
    return {"predicted_sales": round(actual_sales, 2)}