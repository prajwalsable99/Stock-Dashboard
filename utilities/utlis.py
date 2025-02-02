
import streamlit as st

def set_page(title: str, icon: str = "📈"):
        """Sets the Streamlit page configuration and hides the default sidebar navigation."""
        st.set_page_config(
            page_title=f'stocks.io - {title}',
            page_icon=icon,
            layout="wide"
        )
        
        # CSS to hide the default Streamlit sidebar navigation
        hide_streamlit_style = """
            <style>
                [data-testid="stSidebarNav"] {display: none;}  /* Hide default sidebar nav */
                .css-1l02z1v {visibility: hidden;}  /* Hide sidebar toggle button */
            </style>
        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)