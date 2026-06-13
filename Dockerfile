# Base image
FROM python:3.10-slim

# Working directory set karo
WORKDIR /app

# Requirements pehle copy karo (caching ke liye)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki files copy karo
COPY main.py .
COPY Random_Forest_model.pkl .
COPY Scaler.pkl .
COPY feature_columns.pkl .

# Port open karo
EXPOSE 7860

# API run karo
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
