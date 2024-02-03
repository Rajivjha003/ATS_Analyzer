Smart ATS
Smart ATS is a web application that helps you improve your resume for a specific job description. It uses a generative AI model to evaluate your resume and provide feedback on how well it matches the job description, what keywords are missing, and what your profile summary is.

Features
Paste or upload a job description and your resume in PDF format
Get a percentage match score based on the job description and your resume
Get a list of missing keywords that you should include in your resume
Get a profile summary that highlights your skills and experience
Get a visual representation of your resume and the job description using Streamlit
Installation
To run this project, you need to have Python 3.10 or higher and pip installed on your system. You also need to have a Gemini API key, which you can get from here.

Clone this repository or download the zip file
Navigate to the project directory and create a virtual environment (optional)
Install the required packages using pip install -r requirements.txt
Create a .env file in the project directory and add your Gemini API key as GEMINI_API_KEY=your_key
Run streamlit run app.py to launch the web app
Open your browser and go to http://localhost:8501 to use the app
Usage
On the sidebar, paste the job description in the text area or upload a file containing the job description
On the sidebar, upload your resume in PDF format
Click on the “Submit” button on the sidebar
Wait for the app to process your resume and the job description
On the main page, you will see the results in separate boxes
You can use the feedback to improve your resume and increase your chances of getting hired
Project Structure
This is how the project is organized:

📁 ATS_Analyzer/
│
├── 🐍 app.py  
│
├── 📁 modules/  
│   ├── 🐍 __init__.py
│   ├── 🐍 generative_ai.py
│   └── 🐍 pdf_processing.py
│
├── 📁 tests/ 
│   ├── 🐍 __init__.py
│   ├── 🐍 test_generative_ai.py
│   └── 🐍 test_pdf_processing.py
│
├── 🔑 .env  
├── 🚫 .gitignore  
├── 📝 requirements.txt  
└── 📄 README.md