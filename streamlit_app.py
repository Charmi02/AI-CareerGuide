
import streamlit as st

from views.dashboard import render_dashboard
from views.career_view import render_career_view
from views.job_view import render_job_view
from views.about import render_about

from utils.styles import apply_custom_styles



# Page configuration
st.set_page_config(
    page_title="AI CareerGuide",
    page_icon="🚀",
    layout="wide"
)


# Apply application styling
apply_custom_styles()


# Initialize session state
if "profile" not in st.session_state:
    st.session_state.profile = {}


# Sidebar navigation
st.sidebar.title("◈ AI CareerGuide")

st.sidebar.caption(
    "Your Personal Career Assistant"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "MAIN MENU",
    [
        "Dashboard",
        "Career Analysis",
        "Job Matcher",
        "About"
    ],
    key="selected_page"
)


# Page routing
if page == "Dashboard":

    render_dashboard()

elif page == "Career Analysis":

    render_career_view()

elif page == "Job Matcher":

    render_job_view()

elif page == "About":

    render_about()
