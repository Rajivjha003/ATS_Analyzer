import streamlit as st
import json
from dotenv import load_dotenv
from modules import generative_ai, pdf_processing

# Load environment variables
load_dotenv()

# Configure generative AI model
generative_ai.configure_model()

# Streamlit app
st.set_page_config(page_title='Smart ATS', page_icon=":memo:", layout='wide', initial_sidebar_state='auto')

# Define colors
colors = {
    'background': '#37B5B6',
    'text': '#000000',
    'button': '#492E87',
    'button_hover': '#B7E5B4'
}
# Apply custom CSS with bold sidebar header
st.markdown(f"""
    <style>
        body {{
            background-color: {colors['background']};
            color: {colors['text']};
        }}
        .stButton>button {{
            background-color: {colors['button']};
            color: {colors['text']};
        }}
        .stButton>button:hover {{
            background-color: {colors['button_hover']};
            color: {colors['text']};
        }}
        /* Bold sidebar header */
        .sidebar .sidebar-content {{
            font-weight: bold;
        }}
    </style>
    """, unsafe_allow_html=True)


# Centered title and subtitle
st.markdown(
    f"<h1 style='text-align: center; color: {colors['text']};'>Smart ATS</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<h2 style='text-align: center; color: {colors['text']};'>Improve Your Resume ATS</h2>",
    unsafe_allow_html=True,
)

# Create a sidebar for input
st.sidebar.header("Input")
jd = st.sidebar.text_area("Paste the Job Description")
uploaded_file = st.sidebar.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

# Create a submit button in the sidebar
submit = st.sidebar.button("Submit")

if submit:
    if uploaded_file is not None:
        text = pdf_processing.input_pdf_text(uploaded_file)
        
        # Define the input prompt
        input_prompt = f"""
        Act like a skilled ATS (Application Tracking System) with a deep understanding of the tech field, software engineering, data science, data analyst, and big data engineering. Your task is to evaluate the resume based on the given job description. Consider that the job market is very competitive and you should provide the best assistance for improving the resumes. Assign the percentage match based on the job description and identify the missing keywords with high accuracy.
        resume: {text}
        description: {jd}

        I want the response in one single string having the structure:
        {{"JD Match": "", "MissingKeywords": [], "Profile Summary": ""}}
        """
        response = generative_ai.get_gemini_response(input_prompt)
        response_json = json.loads(response)

        # Display the results in separate boxes
        st.subheader("Results")
        st.info(f"JD Match: {response_json['JD Match']}")
        st.info(f"Missing Keywords: {', '.join(response_json['MissingKeywords'])}")
        st.info(f"Profile Summary: {response_json['Profile Summary']}")
    else:
        st.error("Please upload a PDF file.")
else:
    st.info("Please enter the job description and upload your resume, then click 'Submit'.")
