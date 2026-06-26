import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Employee Income Prediction",
    page_icon="💼",
    layout="wide"
)

# ============================================
# LOAD MODEL
# ============================================

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# ============================================
# LOAD DATASET
# ============================================

df = pd.read_csv("income_evaluation.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove extra spaces from string columns
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

# ============================================
# CUSTOM CSS
# ============================================

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e3a8a,#312e81);
}

.main-title{
font-size:48px;
font-weight:bold;
text-align:center;
color:white;
}

.sub-title{
text-align:center;
color:#d1d5db;
font-size:20px;
margin-bottom:30px;
}

div[data-testid="stForm"]{
background:#1e293b;
padding:30px;
border-radius:20px;
box-shadow:0px 0px 20px rgba(0,0,0,.4);
}

.stButton>button{
width:100%;
height:70px;
font-size:24px;
font-weight:bold;
border:none;
border-radius:15px;
background:linear-gradient(90deg,#2563eb,#7c3aed);
color:white;
transition:0.3s;
}

.stButton>button:hover{
background:linear-gradient(90deg,#1d4ed8,#6d28d9);
transform:scale(1.02);
}

.metric-card{
background:#1e293b;
padding:20px;
border-radius:15px;
text-align:center;
}

.footer{
text-align:center;
color:gray;
font-size:15px;
padding-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# SIDEBAR
# ============================================

st.sidebar.title("💼 Income Predictor")

st.sidebar.markdown("---")

st.sidebar.success("✅ Algorithm : Random Forest")

st.sidebar.success("✅ Accuracy : ~86%")

st.sidebar.success("✅ Dataset : Adult Income")

st.sidebar.markdown("---")

st.sidebar.info(
"""
### 📌 Instructions

✔ Fill employee details

✔ Click **Predict Income**

✔ View prediction & confidence
"""
)

# ============================================
# HEADER
# ============================================

st.markdown(
"""
<h1 class="main-title">
💼 Employee Income Prediction
</h1>

<p class="sub-title">
Predict whether an employee earns
<b>Greater than $50K</b>
or
<b>Less than or Equal to $50K</b>
using Machine Learning.
</p>
""",
unsafe_allow_html=True
)

st.markdown("---")

# ============================================
# EDUCATION MAPPING
# ============================================

education_mapping = {
    "Preschool":1,
    "1st-4th":2,
    "5th-6th":3,
    "7th-8th":4,
    "9th":5,
    "10th":6,
    "11th":7,
    "12th":8,
    "HS-grad":9,
    "Some-college":10,
    "Assoc-voc":11,
    "Assoc-acdm":12,
    "Bachelors":13,
    "Masters":14,
    "Prof-school":15,
    "Doctorate":16
}

# ============================================
# EMPLOYEE INPUT FORM
# ============================================

with st.form("salary_prediction_form"):

    st.subheader("👤 Employee Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.slider(
            "Age",
            min_value=18,
            max_value=70,
            value=30
        )

        gender = st.selectbox(
            "Gender",
            sorted(df["sex"].unique())
        )

        education = st.selectbox(
            "Education",
            sorted(df["education"].unique())
        )

        workclass = st.selectbox(
            "Work Class",
            sorted(df["workclass"].unique())
        )

        occupation = st.selectbox(
            "Occupation",
            sorted(df["occupation"].unique())
        )

    with col2:

        marital = st.selectbox(
            "Marital Status",
            sorted(df["marital-status"].unique())
        )

        race = st.selectbox(
            "Race",
            sorted(df["race"].unique())
        )

        country = st.selectbox(
            "Native Country",
            sorted(df["native-country"].unique())
        )

        hours = st.slider(
            "Hours Per Week",
            min_value=1,
            max_value=100,
            value=40
        )

    st.markdown("---")

    st.subheader("💰 Financial Details")

    c1, c2 = st.columns(2)

    with c1:

        capital_gain = st.number_input(
            "Capital Gain",
            min_value=0,
            value=0
        )

    with c2:

        capital_loss = st.number_input(
            "Capital Loss",
            min_value=0,
            value=0
        )

    st.markdown("<br>", unsafe_allow_html=True)

    predict = st.form_submit_button(
        "🚀 Predict Salary"
    )

# ============================================
# HIDDEN FEATURES
# ============================================

education_num = education_mapping.get(
    education,
    13
)

# Automatically fill hidden dataset fields

fnlwgt = int(df["fnlwgt"].median())

relationship = df["relationship"].mode()[0]

# ============================================
# PREDICTION
# ============================================

if predict:

    # Create Input DataFrame
    input_df = pd.DataFrame({

        "age":[age],
        "workclass":[workclass],
        "fnlwgt":[fnlwgt],
        "education":[education],
        "education-num":[education_num],
        "marital-status":[marital],
        "occupation":[occupation],
        "relationship":[relationship],
        "race":[race],
        "sex":[gender],
        "capital-gain":[capital_gain],
        "capital-loss":[capital_loss],
        "hours-per-week":[hours],
        "native-country":[country]

    })

    # One Hot Encoding
    input_encoded = pd.get_dummies(input_df)

    # Match Training Features
    train_columns = pd.get_dummies(
        df.drop("income", axis=1)
    ).columns

    input_encoded = input_encoded.reindex(
        columns=train_columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(input_encoded)[0]

    probability = model.predict_proba(input_encoded)[0]

    confidence = probability.max() * 100

    st.markdown("<br>", unsafe_allow_html=True)

    # ============================================
    # RESULT CARD
    # ============================================

    if prediction == 1:

        st.balloons()

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#16a34a,#22c55e);
        padding:40px;
        border-radius:25px;
        text-align:center;
        color:white;
        box-shadow:0px 0px 30px rgba(34,197,94,.5);
        ">

        <h1>🎉 HIGH INCOME</h1>

        <h2>Predicted Salary : <b>> $50K</b></h2>

        <h1>{confidence:.2f}%</h1>

        <h3>Confidence Score</h3>

        </div>

        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#dc2626,#ef4444);
        padding:40px;
        border-radius:25px;
        text-align:center;
        color:white;
        box-shadow:0px 0px 30px rgba(239,68,68,.5);
        ">

        <h1>💰 LOWER INCOME</h1>

        <h2>Predicted Salary : <b>≤ $50K</b></h2>

        <h1>{confidence:.2f}%</h1>

        <h3>Confidence Score</h3>

        </div>

        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ============================================
    # CONFIDENCE
    # ============================================

    st.subheader("🎯 Model Confidence")

    st.progress(confidence/100)

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    # ============================================
    # PROBABILITY
    # ============================================

    less_prob = probability[0] * 100
    high_prob = probability[1] * 100

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Income ≤ $50K",
            f"{less_prob:.2f}%"
        )

        st.progress(less_prob/100)

    with col2:

        st.metric(
            "Income > $50K",
            f"{high_prob:.2f}%"
        )

        st.progress(high_prob/100)
        
     # ============================================
# VISUAL ANALYTICS
# ============================================

    st.markdown("---")

    st.subheader("📊 Prediction Probability")

    chart_df = pd.DataFrame({
        "Income Class": ["≤ $50K", "> $50K"],
        "Probability": [less_prob, high_prob]
    })

    st.bar_chart(
        chart_df.set_index("Income Class")
    )

    # ============================================
    # EMPLOYEE SUMMARY
    # ============================================

    st.markdown("---")

    st.subheader("👤 Employee Summary")

    summary = pd.DataFrame({

        "Feature":[
            "Age",
            "Gender",
            "Education",
            "Occupation",
            "Work Class",
            "Hours / Week",
            "Country"
        ],

        "Value":[
            age,
            gender,
            education,
            occupation,
            workclass,
            hours,
            country
        ]

    })

    st.table(summary)

    # ============================================
    # PREDICTION TIPS
    # ============================================

    st.markdown("---")

    st.info("""

### 💡 Prediction Tips

✔ Higher education generally improves salary prediction.

✔ Specialized occupations often have a higher probability of earning above $50K.

✔ Capital Gain may positively influence the prediction.

✔ Working more hours per week can affect the predicted income.

""")

    # ============================================
    # MODEL INFORMATION
    # ============================================

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Algorithm",
            "Random Forest"
        )

    with c2:
        st.metric(
            "Dataset",
            "Adult Income"
        )

    with c3:
        st.metric(
            "Model Accuracy",
            "86%"
        )

    # ============================================
    # FOOTER
    # ============================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <hr>

    <center>

    <h3>💼 Employee Salary Prediction System</h3>

    <p>
    Machine Learning • Random Forest • Streamlit
    </p>

    <p style="color:gray;">

    Developed by <b>Sanket More</b>

    </p>

    </center>

    """, unsafe_allow_html=True)   