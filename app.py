# ==========================================
# APLIKASI PREDIKSI HARGA DIAMOND
# STREAMLIT + XGBOOST
# ==========================================

import streamlit as st
import pandas as pd
import pickle


# ==========================================
# LOAD MODEL
# ==========================================

with open("model_xgboost_diamond.pkl", "rb") as file:
    model = pickle.load(file)


# ==========================================
# JUDUL APLIKASI
# ==========================================

st.title("💎 Prediksi Harga Diamond")
st.write("Aplikasi ini memprediksi harga diamond menggunakan model Machine Learning XGBoost.")


# ==========================================
# INPUT USER
# ==========================================

st.header("Masukkan Karakteristik Diamond")

carat = st.number_input("Carat", min_value=0.0, value=0.5)

cut = st.selectbox(
    "Cut",
    ["Fair", "Good", "Very Good", "Premium", "Ideal"]
)

color = st.selectbox(
    "Color",
    ["D","E","F","G","H","I","J"]
)

clarity = st.selectbox(
    "Clarity",
    ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
)

depth = st.number_input("Depth", value=60.0)
table = st.number_input("Table", value=55.0)

x = st.number_input("Length (x)", value=5.0)
y = st.number_input("Width (y)", value=5.0)
z = st.number_input("Depth (z)", value=3.0)


# ==========================================
# ENCODING INPUT
# ==========================================

cut_dict = {
    "Fair":0,
    "Good":1,
    "Very Good":2,
    "Premium":3,
    "Ideal":4
}

color_dict = {
    "D":0,"E":1,"F":2,"G":3,"H":4,"I":5,"J":6
}

clarity_dict = {
    "I1":0,"SI2":1,"SI1":2,"VS2":3,"VS1":4,"VVS2":5,"VVS1":6,"IF":7
}


cut = cut_dict[cut]
color = color_dict[color]
clarity = clarity_dict[clarity]


# ==========================================
# PREDIKSI
# ==========================================

if st.button("Prediksi Harga"):

    data = pd.DataFrame({
        "carat":[carat],
        "cut":[cut],
        "color":[color],
        "clarity":[clarity],
        "depth":[depth],
        "table":[table],
        "x":[x],
        "y":[y],
        "z":[z]
    })

    prediction = model.predict(data)

    st.success(f"💰 Prediksi Harga Diamond: ${prediction[0]:,.2f}")