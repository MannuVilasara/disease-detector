import streamlit as st
from dotenv import load_dotenv
import os
import requests
import time

# Load CSS from external file
try:
    css_file_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    with open(css_file_path, 'r') as f:
        styles = f.read()
except FileNotFoundError:
    # Fallback if CSS file is not found
    styles = ""
    st.warning("CSS file not found. Using default styling.")

load_dotenv()

# Modern Dark Color Palette (for Python usage)
COLORS = {
    'primary': '#6366f1',        # Indigo
    'primary_dark': '#4f46e5',   # Darker indigo
    'secondary': '#8b5cf6',      # Purple
    'accent': '#06b6d4',         # Cyan
    'success': '#10b981',        # Emerald
    'warning': '#f59e0b',        # Amber
    'error': '#ef4444',          # Red
    'dark_bg': '#0f172a',        # Slate 900
    'card_bg': '#1e293b',        # Slate 800
    'card_light': '#334155',     # Slate 700
    'text_primary': '#f8fafc',   # Slate 50
    'text_secondary': '#cbd5e1', # Slate 300
    'text_muted': '#94a3b8',     # Slate 400
    'border': '#475569',         # Slate 600
}


# Configure page
st.set_page_config(
    page_title="AI Disease Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

symptoms = [
    "Itching",
    "Skin Rash",
    "Nodal Skin Eruptions",
    "Continuous Sneezing",
    "Shivering",
    "Chills",
    "Joint Pain",
    "Stomach Pain",
    "Acidity",
    "Ulcers On Tongue",
    "Muscle Wasting",
    "Vomiting",
    "Burning Micturition",
    "Spotting  Urination",
    "Fatigue",
    "Weight Gain",
    "Anxiety",
    "Cold Hands And Feets",
    "Mood Swings",
    "Weight Loss",
    "Restlessness",
    "Lethargy",
    "Patches In Throat",
    "Irregular Sugar Level",
    "Cough",
    "High Fever",
    "Sunken Eyes",
    "Breathlessness",
    "Sweating",
    "Dehydration",
    "Indigestion",
    "Headache",
    "Yellowish Skin",
    "Dark Urine",
    "Nausea",
    "Loss Of Appetite",
    "Pain Behind The Eyes",
    "Back Pain",
    "Constipation",
    "Abdominal Pain",
    "Diarrhoea",
    "Mild Fever",
    "Yellow Urine",
    "Yellowing Of Eyes",
    "Acute Liver Failure",
    "Fluid Overload",
    "Swelling Of Stomach",
    "Swelled Lymph Nodes",
    "Malaise",
    "Blurred And Distorted Vision",
    "Phlegm",
    "Throat Irritation",
    "Redness Of Eyes",
    "Sinus Pressure",
    "Runny Nose",
    "Congestion",
    "Chest Pain",
    "Weakness In Limbs",
    "Fast Heart Rate",
    "Pain During Bowel Movements",
    "Pain In Anal Region",
    "Bloody Stool",
    "Irritation In Anus",
    "Neck Pain",
    "Dizziness",
    "Cramps",
    "Bruising",
    "Obesity",
    "Swollen Legs",
    "Swollen Blood Vessels",
    "Puffy Face And Eyes",
    "Enlarged Thyroid",
    "Brittle Nails",
    "Swollen Extremeties",
    "Excessive Hunger",
    "Extra Marital Contacts",
    "Drying And Tingling Lips",
    "Slurred Speech",
    "Knee Pain",
    "Hip Joint Pain",
    "Muscle Weakness",
    "Stiff Neck",
    "Swelling Joints",
    "Movement Stiffness",
    "Spinning Movements",
    "Loss Of Balance",
    "Unsteadiness",
    "Weakness Of One Body Side",
    "Loss Of Smell",
    "Bladder Discomfort",
    "Foul Smell Of Urine",
    "Continuous Feel Of Urine",
    "Passage Of Gases",
    "Internal Itching",
    "Toxic Look (Typhos)",
    "Depression",
    "Irritability",
    "Muscle Pain",
    "Altered Sensorium",
    "Red Spots Over Body",
    "Belly Pain",
    "Abnormal Menstruation",
    "Dischromic  Patches",
    "Watering From Eyes",
    "Increased Appetite",
    "Polyuria",
    "Family History",
    "Mucoid Sputum",
    "Rusty Sputum",
    "Lack Of Concentration",
    "Visual Disturbances",
    "Receiving Blood Transfusion",
    "Receiving Unsterile Injections",
    "Coma",
    "Stomach Bleeding",
    "Distention Of Abdomen",
    "History Of Alcohol Consumption",
    "Fluid Overload",
    "Blood In Sputum",
    "Prominent Veins On Calf",
    "Palpitations",
    "Painful Walking",
    "Pus Filled Pimples",
    "Blackheads",
    "Scurring",
    "Skin Peeling",
    "Silver Like Dusting",
    "Small Dents In Nails",
    "Inflammatory Nails",
    "Blister",
    "Red Sore Around Nose",
    "Yellow Crust Ooze"
]

# Custom CSS for modern dark theme
st.markdown(f"""
<style>
    {styles}
</style>
""", unsafe_allow_html=True)

# App header
st.markdown("""
<div class="main-header">
    <h1>🏥 AI Disease Prediction System</h1>
    <p>Advanced AI-powered disease prediction based on symptoms</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with additional information
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <h2 style="color: white; margin: 0; font-size: 1.5rem; font-weight: 700;">🏥 AI Disease Predictor</h2>
        <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0; font-size: 0.9rem;">Advanced Medical AI Assistant</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📋 About This App")
    st.markdown("""
    <div class="sidebar-card">
        <p>This AI-powered disease prediction system uses machine learning to analyze symptoms 
        and predict possible diseases or conditions.</p>
        
        <p><strong>Features:</strong></p>
        <ul>
            <li>🤖 AI-powered predictions</li>
            <li>📊 Multi-symptom analysis</li>
            <li>🎯 Accurate disease matching</li>
            <li>📱 Modern user interface</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📞 Emergency Help")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 1.5rem; border-radius: 12px; margin: 1rem 0; color: white;">
        <p style="margin: 0; font-weight: 700; color: white;">⚠️ Medical Emergency?</p>
        <p style="margin: 0.5rem 0 0 0; color: rgba(255,255,255,0.9);">
            If you're experiencing a medical emergency, 
            please contact emergency services immediately.
        </p>
    </div>
    
    **Emergency Numbers:**
    - 🚨 Emergency: 911
    - ☎️ Poison Control: 1-800-222-1222
    """)
    
    st.markdown("### 💡 Pro Tips")
    st.markdown("""
    <div class="sidebar-card">
        <ul style="margin: 0; padding-left: 1.2rem;">
            <li>Be specific about your symptoms</li>
            <li>Select all relevant symptoms</li>
            <li>Don't select symptoms you're unsure about</li>
            <li>Consider symptom severity and duration</li>
            <li>Consult a doctor for serious concerns</li>
        </ul>
    </div>
    """)

def main():
    # Create columns for better layout
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Information section
        st.markdown("""
        <div class="info-box">
            <h4>🧠 How Our AI Works</h4>
            <p><strong>Select the symptoms you're experiencing from the comprehensive list below.</strong> Our advanced AI model will analyze your symptom patterns and predict the most likely medical conditions.</p>
            <p style="margin-top: 1rem; font-style: italic; color: #94a3b8;">
                💡 <strong>Pro Tip:</strong> The more accurate and complete your symptom selection, the better our AI prediction will be.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Symptoms selection section
        st.markdown("""
        <div class="symptom-section">
            <h3>🔍 Select Your Symptoms</h3>
            <p style="color: #cbd5e1; margin: 0; font-size: 1rem;">Choose all symptoms that apply to your current condition</p>
        </div>
        """, unsafe_allow_html=True)
        
        # st.markdown('<div class="symptom-input-section">', unsafe_allow_html=True)
        
        selected_symptoms = st.multiselect(
            "Choose all symptoms that apply to you:",
            symptoms,
            default=None,
            help="💡 Select multiple symptoms for more accurate predictions. Our AI analyzes symptom combinations to provide better results."
        )
        
        # st.markdown('</div>', unsafe_allow_html=True)
        
        # Display selected symptoms count with modern styling
        if selected_symptoms:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {COLORS['success']} 0%, #059669 100%); 
                        padding: 1rem; border-radius: 12px; margin: 1rem 0; color: white; text-align: center;">
                <strong>✅ {len(selected_symptoms)} symptom(s) selected</strong>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">
                    Great! Our AI has enough data to make a prediction.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {COLORS['warning']} 0%, #d97706 100%); 
                        padding: 1rem; border-radius: 12px; margin: 1rem 0; color: white; text-align: center;">
                <strong>⚠️ No symptoms selected</strong>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">
                    Please select at least one symptom to get an AI prediction.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
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
                        f"{os.getenv('BACKEND_URI')}/predict",
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

def display_result(disease, symptoms):
    """Display the prediction result with enhanced styling"""
    if disease and disease.lower() != 'unknown':
        st.markdown(f"""
        <div class="result-success">
            <h2>🎯 Prediction Result</h2>
            <h3>Possible Disease: {disease}</h3>
            <p>Based on the {len(symptoms)} symptoms you selected</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional information
        with st.expander("📊 Selected Symptoms Summary"):
            st.write("You reported the following symptoms:")
            for i, symptom in enumerate(symptoms, 1):
                st.write(f"{i}. {symptom}")
                
        # Disclaimer
        st.markdown("""
        <div class="info-box">
            <h4>⚠️ Important Disclaimer</h4>
            <p>This prediction is for informational purposes only and should not replace professional medical advice. 
            Please consult with a healthcare professional for proper diagnosis and treatment.</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div class="result-warning">
            <h2>🤔 No Clear Prediction</h2>
            <p>Our AI model couldn't determine a specific disease based on the selected symptoms.</p>
            <p>This could mean the symptoms are too general or don't match known patterns.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <h4>💡 Suggestions</h4>
            <ul>
                <li>Try selecting more specific symptoms</li>
                <li>Review your symptom selection for accuracy</li>
                <li>Consider consulting a healthcare professional</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="footer">
        <p style="font-size: 1.1rem; font-weight: 600; color: #495057;">
            🏥 AI Disease Prediction System | Made with ❤️ using Streamlit
        </p>
        <p style="font-size: 0.95rem; color: #6c757d;">
            Remember: This tool is for informational purposes only. Always consult healthcare professionals for medical advice.
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
