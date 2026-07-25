import streamlit as st
import joblib
import pandas as pd

# ==========================
# Load Model
# ==========================
stroke_model = joblib.load("stroke_model.pkl")

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Stroke Prediction",
    page_icon="🩺",
    layout="wide"
)

# ==========================
# Custom CSS
# ==========================
st.markdown("""
<style>

/* Background */
.stApp{
background:linear-gradient(-45deg,#0f172a,#1e3a8a,#2563eb,#06b6d4);
background-size:400% 400%;
animation:gradient 15s ease infinite;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* Hide Streamlit Menu */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Glass Card */
.block-container{
background:rgba(255,255,255,0.10);
backdrop-filter:blur(18px);
padding:2rem;
border-radius:25px;
box-shadow:0px 8px 30px rgba(0,0,0,0.25);
}

/* Title */
.title{
text-align:center;
font-size:48px;
font-weight:bold;
color:white;
animation:heartbeat 1.8s infinite;
}

@keyframes heartbeat{
0%{transform:scale(1);}
25%{transform:scale(1.04);}
50%{transform:scale(1);}
75%{transform:scale(1.04);}
100%{transform:scale(1);}
}

.subtitle{
text-align:center;
color:white;
font-size:20px;
margin-bottom:30px;
}

/* Labels */
label{
color:white !important;
font-weight:bold !important;
}

/* Inputs */
div[data-baseweb="select"]{
background:white;
border-radius:12px;
}

.stNumberInput input{
background:white;
border-radius:12px;
}

/* Button */
.stButton>button{
width:100%;
height:60px;
font-size:22px;
font-weight:bold;
border:none;
border-radius:15px;
background:linear-gradient(90deg,#00c6ff,#0072ff);
color:white;
transition:0.4s;
}

.stButton>button:hover{
transform:scale(1.03);
box-shadow:0px 0px 25px cyan;
}

/* Result Card */
.result{
padding:25px;
border-radius:20px;
text-align:center;
font-size:26px;
font-weight:bold;
color:white;
margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Heading
# ==========================
st.markdown("<div class='title'>🩺 Stroke Prediction System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI Powered Healthcare Risk Prediction</div>", unsafe_allow_html=True)

st.divider()

# ==========================
# Manual Encoding
# ==========================

gender_dict = {
    "Female":0,
    "Male":1,
    "Other":2
}

ever_married_dict = {
    "No":0,
    "Yes":1
}

work_type_dict = {
    "Govt_job":0,
    "Never_worked":1,
    "Private":2,
    "Self-employed":3,
    "children":4
}

Residence_dict = {
    "Rural":0,
    "Urban":1
}

smoking_dict = {
    "Unknown":0,
    "formerly smoked":1,
    "never smoked":2,
    "smokes":3
}

# ==========================
# Input Section
# ==========================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "👤 Gender",
        list(gender_dict.keys())
    )

    age = st.number_input(
        "🎂 Age",
        min_value=1,
        max_value=120,
        value=30
    )

    hypertension = st.selectbox(
        "🩸 Hypertension",
        ["No","Yes"]
    )

    heart_disease = st.selectbox(
        "❤️ Heart Disease",
        ["No","Yes"]
    )

    ever_married = st.selectbox(
        "💍 Ever Married",
        list(ever_married_dict.keys())
    )

with col2:

    work_type = st.selectbox(
        "💼 Work Type",
        list(work_type_dict.keys())
    )

    Residence_type = st.selectbox(
        "🏠 Residence Type",
        list(Residence_dict.keys())
    )

    avg_glucose_level = st.number_input(
        "🍬 Average Glucose Level",
        min_value=50.0,
        max_value=300.0,
        value=100.0
    )

    bmi = st.number_input(
        "⚖ BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )

    smoking_status = st.selectbox(
        "🚬 Smoking Status",
        list(smoking_dict.keys())
    )

st.divider()

# ==========================
# Prediction
# ==========================

if st.button("🔍 Predict Stroke Risk"):

    input_data = pd.DataFrame({

        "gender":[gender_dict[gender]],
        "age":[age],
        "hypertension":[1 if hypertension=="Yes" else 0],
        "heart_disease":[1 if heart_disease=="Yes" else 0],
        "ever_married":[ever_married_dict[ever_married]],
        "work_type":[work_type_dict[work_type]],
        "Residence_type":[Residence_dict[Residence_type]],
        "avg_glucose_level":[avg_glucose_level],
        "bmi":[bmi],
        "smoking_status":[smoking_dict[smoking_status]]

    })

    prediction = stroke_model.predict(input_data)

    if prediction[0] == 1:

        st.markdown("""
        <div class="result" style="background:#dc2626;">
        ⚠️ HIGH RISK OF STROKE
        <br><br>
        Please consult a healthcare professional immediately.
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result" style="background:#16a34a;">
        ✅ LOW RISK OF STROKE
        <br><br>
        Your prediction indicates a lower stroke risk.
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("🩺 Developed using Streamlit & Machine Learning")