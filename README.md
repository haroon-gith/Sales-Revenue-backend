# 💰 Sales Revenue Prediction

A machine learning web API that predicts **sales revenue** for retail orders using a trained Random Forest model.

---

## 📌 Project Overview

This project is trained on the **Sample Superstore** dataset. Given an order's details (segment, category, region, discount, etc.), the model predicts the expected sales amount in dollars.

---

## 🧠 Model Details

| Property | Detail |
|----------|--------|
| Algorithm | Random Forest Regressor |
| Target | Sales (log1p transformed) |
| Features | Quantity, Discount, Profit, Order Month, Quarter, Shipping Delay, Segment, Ship Mode, Region, Category |
| Preprocessing | Yeo-Johnson transform, StandardScaler, One-Hot Encoding |

---

## 📁 Project Structure

```
├── main.py                   # FastAPI backend
├── Dockerfile                # HuggingFace deployment
├── requirements.txt          # Dependencies
├── Random_Forest_model.pkl   # Trained model
├── Scaler.pkl                # StandardScaler
├── feature_columns.pkl       # Training feature columns
└── .github/
    └── workflows/
        └── deploy.yml        # Auto deploy to HuggingFace
```

---

## 🚀 How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn main:app --reload
```

API will start at: `http://localhost:8000`

---

## 📬 API Usage

**Endpoint:** `POST /predict`

**Request Body:**
```json
{
  "quantity": 3,
  "discount": 0.2,
  "profit": 41.9,
  "order_month": 11,
  "order_quarter": 4,
  "shipping_delay": 4,
  "segment": "Consumer",
  "ship_mode": "Standard Class",
  "region": "East",
  "category": "Technology"
}
```

**Response:**
```json
{
  "predicted_sales": 285.50
}
```

---

## 👨‍💻 Author

**Haroon**  
Aspiring ML Engineer | Pakistan  
GitHub: [@haroon-ml](https://github.com/haroon-ml)
