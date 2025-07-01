import streamlit as st
import os
import requests
import time
from components.displayResult import display_result
from utils.constants import BACKEND_URL


def result(selected_symptoms):
    # Prediction section with improved styling
        st.markdown("""
        <div class="prediction-button-container">
            <div class="prediction-button-wrapper">
        """, unsafe_allow_html=True)
        
        predict_button = st.button(
            "🔮 Analyze Symptoms", 
            disabled=len(selected_symptoms) == 0,
            help="Click to analyze your symptoms with our AI model",
            use_container_width=True
        )
        
        st.markdown("""
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Results section
        if predict_button and selected_symptoms:
            with st.spinner("🤖 Analyzing your symptoms..."):
                time.sleep(1)  # Add a brief delay for better UX
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/predict",
                        json=selected_symptoms,
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        disease = response.json()['disease']
                        display_result(disease, selected_symptoms)
                    else:
                        st.error("❌ Error connecting to the prediction service. Please try again.")
                        
                except requests.exceptions.Timeout:
                    st.error("⏱️ Request timed out. Please check your connection and try again.")
                except requests.exceptions.ConnectionError:
                    st.error("🔌 Could not connect to the prediction service. Please ensure the backend is running.")
                except Exception as e:
                    st.error(f"❌ An unexpected error occurred: {str(e)}")