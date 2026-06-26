# 💼 Employee Salary Prediction Using Random Forest

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">

<img src="https://img.shields.io/badge/Scikit--Learn-Random_Forest-orange?style=for-the-badge&logo=scikitlearn">

<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">

</p>

---

# 📖 Project Overview

Employee Salary Prediction is a Machine Learning web application that predicts whether an employee's annual income is:

* 💰 **Less than or Equal to $50K**
* 🎉 **Greater than $50K**

The application is developed using **Python**, **Scikit-learn**, and **Streamlit**. A **Random Forest Classifier** is trained on the Adult Income Dataset and deployed through a modern web interface.

This project demonstrates the complete Machine Learning workflow—from data preprocessing and model training to deployment in an interactive web application.

---

# 🚀 Features

* Modern Streamlit User Interface
* Employee Salary Prediction
* Random Forest Machine Learning Model
* Confidence Score
* Prediction Probability
* Automatic Feature Encoding
* Interactive Employee Input Form
* Responsive Layout
* Clean and Attractive Design

---

# 🧠 Machine Learning Workflow

### 1. Data Collection

* Adult Income Dataset

### 2. Data Cleaning

* Removed unwanted spaces
* Cleaned column names
* Checked missing values

### 3. Feature Engineering

* Converted categorical columns using One-Hot Encoding
* Converted target variable into numerical format

### 4. Data Splitting

* Training Data : 80%
* Testing Data : 20%

### 5. Model Building

Algorithm Used:

**Random Forest Classifier**

### 6. Model Evaluation

Metrics Used:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report
* ROC-AUC Score

### 7. Model Deployment

The trained model was saved as a **Pickle (.pkl)** file and deployed using Streamlit.

---

# 📊 Model Performance

| Metric    | Value         |
| --------- | ------------- |
| Algorithm | Random Forest |
| Accuracy  | ~86%          |
| Precision | Good          |
| Recall    | Good          |
| F1 Score  | Good          |

---

# 🛠 Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Plotly
* Pickle

### Development Tools

* Google Colab
* Visual Studio Code
* Git
* GitHub

---

# 📂 Project Structure

```text
Salary-Prediction-Using-Random-Forest/

│

├── app.py

├── model.pkl

├── income_evaluation.csv

├── requirements.txt

├── README.md

├── .gitignore

└── screenshots/

    ├── home.png

    ├── prediction.png

    └── result.png
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Salary-Prediction-Using-Random-Forest.git
```

---

## Move to Project Folder

```bash
cd Salary-Prediction-Using-Random-Forest
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Streamlit App

```bash
streamlit run app.py
```

---

# 🖥 Application Workflow

1. Open the Streamlit application.
2. Enter employee details.
3. Click **Predict Salary**.
4. The application processes the input.
5. Random Forest predicts the salary category.
6. View prediction, confidence score, and probability.

---

# 📷 Screenshots

## Home Page

(Add Home Page Screenshot Here)

---

## Employee Details

(Add Input Form Screenshot Here)

---

## Prediction Result

(Add Prediction Screenshot Here)

---

## Probability Visualization

(Add Probability Screenshot Here)

---

# 📊 Input Features

The application accepts the following employee details:

* Age
* Gender
* Education
* Work Class
* Occupation
* Marital Status
* Race
* Native Country
* Hours Per Week
* Capital Gain
* Capital Loss

Some technical dataset fields are automatically handled by the application.

---

# 🤖 Model Details

### Model Name

Random Forest Classifier

### Saved Model

```text
model.pkl
```

The trained model is loaded directly inside the Streamlit application for making predictions.

---

# 📈 Future Improvements

* Hyperparameter Tuning
* Cross Validation
* Feature Importance Visualization
* Model Comparison (Random Forest vs XGBoost)
* Docker Deployment
* Cloud Deployment
* Prediction History
* User Authentication

---

# 🎯 Learning Outcomes

This project helped me learn:

* Data Preprocessing
* Feature Engineering
* One-Hot Encoding
* Random Forest Classification
* Model Evaluation
* Pickle Serialization
* Streamlit Development
* Machine Learning Deployment
* Git & GitHub

---

# 👨‍💻 Author

## Sanket More

Machine Learning | Data Engineering | AI Enthusiast

---


## Thank You ❤️

Thank you for visiting this project.

Happy Coding! 🚀
