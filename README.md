##🥗 Nutritionist AI – Smart Meal Analysis App

📌 Overview

Nutritionist AI is an AI-powered web application that analyzes food images and provides detailed nutritional insights.
By uploading a meal image, users receive:

 -> Meal identification

 -> Nutritional values in tabular format

 -> Health benefits

 -> Macronutrient breakdown (carbs, fats, protein, fiber, sugar)

 -> Healthy alternatives

##🚀 Features

✅ Upload food images (JPG / PNG)

✅ AI-based meal recognition

✅ Nutritional value breakdown in table format

✅ Health insights and dietary suggestions

✅ Clean and simple Streamlit UI

✅ Secure API key handling using .env or Streamlit secrets
## 🧠 Tech Stack

Component Technology

Frontend Streamlit

AI Model Google Gemini (gemini-2.5-flash)

Backend	Python

Image Processing Pillow (PIL)

Environment Management	python-dotenv

Deployment	Streamlit Cloud
## 📂 Project Structure

nutritionist/

├── app.py                   # Main Streamlit application

├── requirements.txt         # Python dependencies

├── .env                     # API key (local only, NOT pushed)

└── README.md

## ▶️ Run the App Locally

streamlit run app.py

## 🧪 How the App Works

User uploads a meal image

Image is processed using Gemini Vision

AI analyzes:

    Food type

    Nutritional values

    Health benefits

    Results are displayed in a structured table format

    Suggestions for healthier alternatives are included

📊 Sample Output

Item	Calories	Protein
Rice	200 kcal	4g
Chicken	250 kcal	25g

Additional Info:

    Carbohydrates: 55%

    Protein: 30%

    Fats: 10%

    Fiber: 5%

## 🔐 Security Notes

API keys are never hardcoded

.env and .streamlit/secrets.toml are excluded from GitHub

Safe for public deployment