import streamlit as st
from src.main import main

st.title("Smart Parking Dashboard")

if st.button("Run Detection"):
    main()
