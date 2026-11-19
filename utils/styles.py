
import streamlit as st


def apply_custom_styles():

    st.markdown(
        """
        <style>

        /* Main application background */
        .stApp {
            background-color: #080D19;
            color: #F1F5F9;
        }

        /* Main content area */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        /* Headings */
        h1, h2, h3 {
            color: #F8FAFC !important;
            font-weight: 700;
        }

        /* Paragraphs and labels */
        p, label, .stMarkdown {
            color: #CBD5E1;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #0D1729;
            border-right: 1px solid #1E3A5F;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2 {
            color: #60A5FA !important;
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(
                90deg,
                #087CF5,
                #2563EB
            );
            color: white;
            border: none;
            border-radius: 9px;
            padding: 0.55rem 1.2rem;
            font-weight: 600;
        }

        .stButton > button:hover {
            background: #1D4ED8;
            color: white;
            border: 1px solid #60A5FA;
        }

        /* Input fields */
        .stTextInput input,
        .stTextArea textarea {
            background-color: #111C30;
            color: white;
            border: 1px solid #334B6B;
            border-radius: 8px;
        }

        /* Select boxes */
        .stSelectbox div[data-baseweb="select"] > div {
            background-color: #111C30;
            color: white;
            border-color: #334B6B;
        }

        /* Cards and containers */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #101B2E;
            border-color: #243B5A;
            border-radius: 12px;
        }

        /* Metrics */
        div[data-testid="stMetric"] {
            background-color: #101B2E;
            padding: 15px;
            border: 1px solid #243B5A;
            border-radius: 12px;
        }

        /* Progress bar */
        .stProgress > div > div > div > div {
            background-color: #1685FF;
        }

        /* Divider */
        hr {
            border-color: #243B5A;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
