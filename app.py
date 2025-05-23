import streamlit as st
import random
import time

st.set_page_config(page_title="Sheikhy Baii Aviator Predictor", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3, h4, h5 {
        color: #f39c12;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Sheikhy Baii Aviator Prediction Model")
st.write("**Live Crash History & Prediction Demo**")

@st.cache_data(ttl=10)
def get_crash_history():
    return [round(random.uniform(1.0, 10.0), 2) for _ in range(20)]

def predict_next_crash(history):
    avg = sum(history[-5:]) / 5
    prediction = round(avg + random.uniform(-1.0, 1.0), 2)
    return max(1.0, prediction)

while True:
    history = get_crash_history()
    st.subheader("Crash History (Last 20 rounds)")
    st.write(history)

    pred = predict_next_crash(history)
    st.subheader("Next Crash Multiplier Prediction")
    st.write(f"**{pred}x**")

    st.write("Prediction updates every 10 seconds automatically.")

    countdown = st.empty()
    for i in range(10, 0, -1):
        countdown.text(f"Next update in {i} seconds...")
        time.sleep(1)

    st.rerun()
