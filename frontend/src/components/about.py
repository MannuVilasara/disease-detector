import streamlit as st

def about():
    html_content = """
<div class="info-box">
    <h2>🏥 About AI Disease Predictor</h2>
    <p>A machine learning-powered application that predicts potential diseases based on user-selected symptoms. 
    This project leverages advanced AI algorithms to provide quick health insights for educational purposes.</p>   
    <h4>👥 Development Team</h4>
    <div style="margin: 1.5rem 0;">
        <div style="background: rgba(100, 181, 246, 0.1); padding: 1.5rem; border-radius: 12px; margin: 1rem 0; border-left: 4px solid #64b5f6;">
            <h5 style="color: #64b5f6; margin: 0 0 0.5rem 0;"><a href="github/MannuVilasara" target="_blank">🧑‍💻 Manpreet Singh</a></h5>
            <p style="margin: 0; color: #cbd5e1;"><strong>Department:</strong> CSE</p>
            <p style="margin: 0.5rem 0 0 0; color: #94a3b8;"><strong>UID:</strong> 2472013</p>
        </div>
        <div style="background: rgba(139, 92, 246, 0.1); padding: 1.5rem; border-radius: 12px; margin: 1rem 0; border-left: 4px solid #8b5cf6;">
            <h5 style="color: #8b5cf6; margin: 0 0 0.5rem 0;"><a href="github/GurmanDhami05" target="_blank">🧑‍💻 Gurman Singh Dhami</a></h5>
            <p style="margin: 0; color: #cbd5e1;"><strong>Department:</strong> CSE</p>
            <p style="margin: 0.5rem 0 0 0; color: #94a3b8;"><strong>UID:</strong> 2472054</p>
        </div>
        <div style="background: rgba(6, 182, 212, 0.1); padding: 1.5rem; border-radius: 12px; margin: 1rem 0; border-left: 4px solid #06b6d4;">
            <h5 style="color: #06b6d4; margin: 0 0 0.5rem 0;"><a href="github/ikeshav26" target="_blank">🧑‍💻 Keshav Gilhotra </a></h5>
            <p style="margin: 0; color: #cbd5e1;"><strong>Department:</strong> CSE</p>
            <p style="margin: 0.5rem 0 0 0; color: #94a3b8;"><strong>UID:</strong> 2472125</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.1); padding: 1.5rem; border-radius: 12px; margin: 1rem 0; border-left: 4px solid #10b981;">
            <h5 style="color: #10b981; margin: 0 0 0.5rem 0;"><a href="github/Ikrish21" target="_blank">🧑‍💻 Krish Puri</a></h5>
            <p style="margin: 0; color: #cbd5e1;"><strong>Department:</strong> CSE</p>
            <p style="margin: 0.5rem 0 0 0; color: #94a3b8;"><strong>UID:</strong> 2472064</p>
        </div>
        <div style="background: rgba(245, 158, 11, 0.1); padding: 1.5rem; border-radius: 12px; margin: 1rem 0; border-left: 4px solid #f59e0b;">
            <h5 style="color: #f59e0b; margin: 0 0 0.5rem 0;"><a href="github/iakshra22" target="_blank">🧑‍💻 Akshra</a></h5>
            <p style="margin: 0; color: #cbd5e1;"><strong>Department:</strong> CSE</p>
            <p style="margin: 0.5rem 0 0 0; color: #94a3b8;"><strong>UID:</strong> 2472068</p>
        </div>
        <div style="background: rgba(239, 68, 68, 0.1); padding: 1.5rem; border-radius: 12px; margin: 1rem 0; border-left: 4px solid #ef4444;">
            <h5 style="color: #ef4444; margin: 0 0 0.5rem 0;"><a href="github/bhavukahuja" target="_blank">🧑‍💻 Bhavuk Ahuja</a></h5>
            <p style="margin: 0; color: #cbd5e1;"><strong>Department:</strong> CSE</p>
            <p style="margin: 0.5rem 0 0 0; color: #94a3b8;"><strong>UID:</strong> 2472086</p>
        </div>
    </div>
    <h4>🔧 Tech Stack</h4>
    <ul style="color: #cbd5e1;">
        <li><strong>Frontend:</strong> Streamlit</li>
        <li><strong>Backend:</strong> Flask</li>
        <li><strong>ML:</strong> Scikit-learn</li>
        <li><strong>Deployment:</strong> Nginx</li>
    </ul>
    <h4>⚠️ Disclaimer</h4>
    <p style="color: #f59e0b; background-color: rgba(245, 158, 11, 0.1); padding: 1rem; border-radius: 8px; border-left: 4px solid #f59e0b; margin: 1rem 0;">
        <strong>For educational purposes only.</strong> This tool should not replace professional medical advice. 
        Always consult healthcare providers for medical concerns.
    </p>
</div>
"""
    
    st.markdown(html_content, unsafe_allow_html=True)
