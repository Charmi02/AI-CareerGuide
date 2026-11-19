
import streamlit as st

from controllers.job_controller import analyze_job_match


def render_job_view():

    st.title("💼 Job Description Matcher")

    st.write(
        "Compare your skills with a job description "
        "to understand how closely your profile matches."
    )

    st.divider()

    st.subheader("Your Skills")

    saved_skills = ""

    if "profile" in st.session_state:
        saved_skills = st.session_state.profile.get(
            "skills", ""
        )

    skills = st.text_area(
        "Enter your skills",
        value=saved_skills,
        placeholder="Python, Linux, AWS, Networking"
    )

    st.subheader("Job Description")

    job_description = st.text_area(
        "Paste the job description",
        placeholder="Paste the complete job description here...",
        height=220
    )

    if st.button("Match My Profile", type="primary"):

        try:

            result = analyze_job_match(
                skills,
                job_description
            )

            score = result["similarity_score"]

            st.divider()

            st.subheader("📊 Job Match Results")

            st.metric(
                "Profile Similarity",
                str(score) + "%"
            )

            st.progress(score / 100)

            st.caption(
                "This score measures text similarity between "
                "your skills and the job description. "
                "It is not a probability of getting hired."
            )

            if score >= 60:
                st.success(
                    "Your skills show a relatively strong text match."
                )

            elif score >= 30:
                st.info(
                    "There is a partial match. Review the job requirements."
                )

            else:
                st.warning(
                    "Your profile has a low text similarity. "
                    "Consider developing relevant skills."
                )

        except ValueError as error:
            st.warning(str(error))

        except Exception as error:
            st.error("Job matching failed: " + str(error))
