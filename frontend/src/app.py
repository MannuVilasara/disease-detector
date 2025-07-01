import streamlit as st
from dotenv import load_dotenv
from utils.utils import load_css
from components import header, info, selection, result, footer

load_dotenv()
styles = load_css()

# Configure page
st.set_page_config(
    page_title="AI Disease Predictor",
    page_icon="🏥",
    layout="wide",
)


# Custom CSS for modern dark theme
st.markdown(f"""
<style>
    {styles}
</style>
""", unsafe_allow_html=True)



def main():

    # App header
    header()

    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Information section
        info()

        #selection section
        selected_symptoms = selection()
        
        #result section
        result(selected_symptoms)


    # Footer
    footer()


if __name__ == "__main__":
    main()
