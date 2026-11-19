
import streamlit as st


def render_about():

    st.title("ℹ️ About AI CareerGuide")

    st.markdown(
        """
        ### Your Personal Career Development Platform

        AI CareerGuide is a Python-based career guidance
        application designed to help users explore career
        opportunities and identify the skills they need
        to develop.

        ---
        """
    )

    st.subheader("🚀 What This Project Does")

    st.markdown(
        """
        - **Career Discovery:** Recommends career paths
          based on skills and interests.

        - **Skill Gap Analysis:** Identifies existing
          skills and skills to improve.

        - **Learning Roadmap:** Organizes missing skills
          into a learning sequence.

        - **Job Matcher:** Compares user skills with
          job descriptions.
        """
    )

    st.divider()

    st.subheader("🛠️ Technology Stack")

    col1, col2 = st.columns(2)

    with col1:
        st.info("Python")
        st.info("Streamlit")
        st.info("Scikit-learn")

    with col2:
        st.info("Pandas")
        st.info("TF-IDF")
        st.info("Cosine Similarity")

    st.divider()

    st.subheader("🏗️ Project Architecture")

    st.code(
        """
AI-CareerGuide/
│
├── models/
│   ├── career_model.py
│   ├── skill_gap.py
│   └── job_match.py
│
├── controllers/
│   ├── career_controller.py
│   └── job_controller.py
│
├── views/
│   ├── dashboard.py
│   ├── career_view.py
│   ├── job_view.py
│   └── about.py
│
├── utils/
│
└── streamlit_app.py
        """,
        language="text"
    )

    st.divider()

    st.caption(
        "AI CareerGuide | A Personal IT Portfolio Project"
    )
