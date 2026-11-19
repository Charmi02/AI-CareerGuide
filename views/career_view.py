
import streamlit as st

from controllers.career_controller import analyze_career_profile


def render_career_view():

    st.title("🎯 Career Discovery")

    st.write(
        "Tell us about yourself to discover suitable career paths."
    )

    st.divider()

    st.subheader("👤 Your Profile")

    name = st.text_input("Your Name")

    education = st.selectbox(
        "Education",
        [
            "High School",
            "Diploma",
            "Bachelor's Degree",
            "Master's Degree",
            "Other"
        ]
    )

    experience = st.selectbox(
        "Work Experience",
        [
            "No experience",
            "Less than 1 year",
            "1–3 years",
            "3–5 years",
            "5+ years"
        ]
    )

    skills = st.text_input(
        "Your Skills",
        placeholder="Python, Linux, AWS, Networking"
    )

    interests = st.text_input(
        "Career Interests",
        placeholder="Cloud Computing, DevOps"
    )

    if st.button("Analyze My Career", type="primary"):

        if not name.strip():
            st.warning("Please enter your name.")

        elif not skills.strip() or not interests.strip():
            st.warning("Please enter your skills and interests.")

        else:

            try:

                result = analyze_career_profile(
                    skills,
                    interests
                )

                st.session_state.profile = {
                    "name": name,
                    "education": education,
                    "experience": experience,
                    "skills": skills,
                    "interests": interests
                }

                st.session_state.career_result = result

                st.success(
                    "Career analysis completed for " + name + "!"
                )

                st.divider()

                st.subheader("🚀 Recommended Careers")

                for career in result["recommendations"]:

                    st.markdown("### " + career["career"])

                    st.write(
                        "Profile similarity: "
                        + str(career["score"]) + "%"
                    )

                    st.progress(career["score"] / 100)

                st.divider()

                st.subheader("📊 Skill Gap Analysis")

                st.write(
                    "Target Career: " + result["target_career"]
                )

                left, right = st.columns(2)

                with left:

                    st.markdown("### ✅ Skills You Have")

                    for skill in result["existing_skills"]:
                        st.write("• " + skill)

                    if not result["existing_skills"]:
                        st.write("No matching skills found.")

                with right:

                    st.markdown("### 📚 Skills to Learn")

                    for skill in result["missing_skills"]:
                        st.write("• " + skill)

                    if not result["missing_skills"]:
                        st.success("All listed skills matched!")

                st.divider()

                st.subheader("🗺️ Your Learning Roadmap")

                for number, skill in enumerate(
                    result["roadmap"], 1
                ):
                    st.write(
                        str(number) + ". Learn " + skill
                    )

                if not result["roadmap"]:
                    st.info("Continue developing your existing skills.")

            except ValueError as error:

                st.warning(str(error))

            except Exception as error:

                st.error("Career analysis failed: " + str(error))
