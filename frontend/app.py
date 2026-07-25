import streamlit as st
import requests

st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Matcher")

st.write(
    "Upload your resume and paste a job description to see how well your profile matches the role."
)

st.divider()

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the complete job description here..."
)

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

analyze = st.button(
    "Analyze Resume",
    use_container_width=True
)

if analyze:

    if not job_description.strip():
        st.error("Please paste a job description.")
        st.stop()

    if resume is None:
        st.error("Please upload a resume.")
        st.stop()

    with st.spinner("Analyzing Resume..."):

        files = {
            "resume": (
                resume.name,
                resume,
                resume.type
            )
        }

        data = {
            "job_description": job_description
        }

        try:

            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                files=files,
                data=data
            )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to the FastAPI server.\n\n"
                "Make sure FastAPI is running."
            )
            st.stop()

        if response.status_code != 200:

            st.error("Backend returned an error.")

            st.code(response.text)

            st.stop()

        result = response.json()

    st.divider()

    st.header("Resume Analysis")

    st.metric(
        label="Match Score",
        value=f"{result['score']}%"
    )

    st.subheader("Verdict")

    st.write(result["verdict"])

    st.subheader("✅ Matching Skills")

    if result["matching_skills"]:

        for skill in result["matching_skills"]:
            st.success(skill)

    else:
        st.write("No matching skills found.")

    st.subheader("❌ Missing Skills")

    if result["missing_skills"]:

        for skill in result["missing_skills"]:
            st.error(skill)

    else:
        st.write("No missing skills.")

    st.subheader("💡 Improvement Tips")

    if result["tips"]:

        for tip in result["tips"]:
            st.info(tip)

    else:
        st.write("No suggestions available.")