


import streamlit as st
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


st.image("C:\\Users\\Lenovo\\Downloads\\test-images.jpg", width=300)
st.title('My-Dashboard:zap:')

st.metric(label="My Profile Viewers", value=+999, delta=-1)

option = st.sidebar.radio("Login/SignUp", ("Login", "SignUp"))
if option == "Login":
    with st.sidebar.form("login"):
        st.write("Login Dashboard")
        username = st.text_input("Enter your Username")
        password = st.text_input("Enter your Password", type="password")

        submitted = st.form_submit_button("Login")
        if submitted:
            st.write("Login Successful")
else:
    with st.sidebar.form("signup"):
        st.write("SignUp Dashboard")
        username = st.text_input("Enter your Username")
        password = st.text_input("Enter your Password", type="password")
        email = st.text_input("Enter your Email")

        submitted = st.form_submit_button("SignUp")
        if submitted:
            st.write("Signup Successful")

with st.expander("Upload your JSON file"):
    uploaded_file = st.file_uploader("Upload your JSON file", type=["json"])
    if uploaded_file is not None:
        try:
            data = json.load(uploaded_file)
            st.success("File successfully read ✅")
            st.write("Current file content:")
            st.json(data)
        except json.JSONDecodeError:
            st.error("The uploaded file is not a valid JSON ❌")
            st.stop()

with st.expander("Statistic"):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(1000), ax=ax)
    st.pyplot(fig)

with st.expander("User Profile"):
    col1, col2 = st.columns(2)
    col1.text_input("Enter your NAME:")
    col2.text_input("Enter your LOCATION:")
    st.camera_input("Take a picture", key="camera_input")








