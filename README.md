---
title: Sales Revenue Prediction
emoji: 💰
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "3.10"
app_file: main.py
pinned: false
---

##Sales Revenue Prediction API
This is a sales revenue prediction model deployed on Hugging Face Spaces.

##How to use:
Send a POST request to /predict with order features.

##Model Info:
Trained with scikit-learn Random Forest
Uses Yeo-Johnson transform + One-Hot Encoding
Returns predicted sales amount in USD
