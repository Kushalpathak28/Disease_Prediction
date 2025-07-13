# Disease Prediction System

This is a simple web application that predicts possible diseases based on user-input symptoms using a machine learning model.

---

## 🔍 Project Description

Many diseases share overlapping symptoms, making it challenging for individuals to assess their health. This project demonstrates how machine learning can be used for **preliminary disease prediction** by analyzing symptoms like fever, cough, fatigue, headache, and nausea.

The goal is to provide users with a quick indication of potential illnesses based on their symptoms.  
**⚠️ Disclaimer: This tool is NOT intended for medical diagnosis and should not replace professional medical advice.**

---

## 🚀 Features

- ✅ Web-based user interface  
- ✅ Machine Learning model (Decision Tree Classifier)  
- ✅ Fast predictions based on symptom input  
- ✅ Special handling for “No symptoms” → *“You are fit!”*  
- ✅ Simple and clean HTML/CSS frontend

---

## 🛠️ Technologies Used

- Python 3.11  
- Flask  
- pandas  
- scikit-learn  
- HTML & CSS

---

## 📂 Project Structure

disease-prediction
├── app.py
├── templates/
│ └── index.html
└── README.md

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/disease-prediction.git
cd disease-prediction

## Install Required Libraris
pip install flask pandas scikit-learn

## Run the App
python app.py

## Open in Browser
http://127.0.0.1:5000/
