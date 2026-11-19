
import streamlit as st



def render_dashboard():

    st.markdown(
        """
        <p style="color:#60A5FA;font-weight:bold;
        letter-spacing:2px;">
        YOUR PERSONAL AI CAREER ASSISTANT
        </p>
        """,
        unsafe_allow_html=True
    )

    st.title("Design Your Future. 🚀")

    st.markdown(
        "### Discover your potential. Build your career."
    )

    # Hero banner
    st.markdown(
        """
        <div style="
            background:linear-gradient(110deg,#102B55,#087CF5);
            padding:35px;
            border-radius:18px;
            margin:20px 0;
            border:1px solid #348FFF;
        ">
            <h1 style="color:white;">
                Your Career. Your Future.
            </h1>
            <p style="color:#E5F0FF;font-size:17px;">
                Discover suitable career paths, identify skill gaps
                and create a personalized learning journey
                with AI-powered career guidance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Dashboard metrics
    st.subheader("Your Career Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Career Paths", "6")
    col2.metric("AI Features", "3")
    col3.metric("Platform", "AI Powered")

    st.divider()

    # Feature cards
    st.subheader("Explore Your Career Toolkit")

    left, right = st.columns(2)

    with left:
        with st.container(border=True):
            st.markdown("## 🎯")
            st.subheader("Career Discovery")
            st.write(
                "Explore career opportunities that match "
                "your skills and interests."
            )

        with st.container(border=True):
            st.markdown("## 🗺️")
            st.subheader("Learning Roadmap")
            st.write(
                "Build a step-by-step plan for your target career."
            )

    with right:
        with st.container(border=True):
            st.markdown("## 📊")
            st.subheader("Skill Gap Analysis")
            st.write(
                "Identify your existing skills and areas "
                "for improvement."
            )

        with st.container(border=True):
            st.markdown("## 💼")
            st.subheader("Job Matcher")
            st.write(
                "Compare your skills with job descriptions."
            )

    # Get Started section
    st.divider()

    st.markdown(
        """
        <div style="
            background:linear-gradient(110deg,#102B55,#142D50);
            padding:30px;
            border-radius:16px;
            border:1px solid #348FFF;
            margin-top:20px;
            margin-bottom:15px;
        ">
            <h2 style="color:white;">
                Ready to Build Your Future?
            </h2>
            <p style="color:#DCEBFF;font-size:16px;">
                Start your career journey today. Enter your
                education, experience, skills and interests.
                AI CareerGuide will help you explore career paths
                and identify your next learning goals.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.button(
    "🚀 Get Started",
    type="primary",
    on_click=lambda: st.session_state.update(
        {"selected_page": "Career Analysis"}
    )
)
    st.divider()

    st.caption(
        "AI CareerGuide | Built with Python, Streamlit "
        "and Scikit-learn"
    )
