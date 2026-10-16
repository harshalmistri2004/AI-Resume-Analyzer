# AI Resume Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/LangChain-LLM-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Google_Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini"/>
</p>

<p align="center">
  <b>Analyze smarter. Improve your resume. Move closer to your next opportunity.</b>
</p>

<p align="center">
  An AI-powered application designed to help job seekers analyze PDF resumes and explore AI-driven resume evaluation using Python, Streamlit, LangChain, and Google Gemini.
</p>

<p align="center">
  <a href="https://github.com/harshalmistri2004/AI-Resume-Analyzer"><b>Explore Repository</b></a>
</p>

---

## Overview

AI Resume Analyzer brings resume processing and generative AI together in a simple web application. It extracts text from PDF resumes, preprocesses the content, and organizes the logic required for AI-powered resume and ATS analysis.

## Features

| Feature | Description |
|---|---|
| PDF Resume Processing | Upload PDF resumes and extract text for analysis. |
| Text Preprocessing | Prepare extracted resume content for downstream processing. |
| AI Integration | Connect LLM-based analysis workflows through LangChain and Google Gemini. |
| ATS Analysis | Structure prompts and analysis logic for resume evaluation. |
| Modular Design | Keep document processing, prompts, and AI chain logic separate. |
| Interactive UI | Access the application through a Streamlit interface. |

## Tech Stack

<p>
  <img src="https://skillicons.dev/icons?i=python,git,github" alt="Technology stack"/>
</p>

- **Language:** Python
- **Frontend:** Streamlit
- **LLM Orchestration:** LangChain
- **Generative AI:** Google Gemini API
- **Document Processing:** PDF parsing libraries
- **Configuration:** Environment variables and `.env`

## Architecture

```text
                 ┌──────────────────────┐
                 │   Streamlit UI       │
                 │       app.py         │
                 └──────────┬───────────┘
                            │
                 ┌──────────▼───────────┐
                 │  Resume Processing   │
                 │  PDF Text Extraction │
                 └──────────┬───────────┘
                            │
                 ┌──────────▼───────────┐
                 │   Text Processing    │
                 │  Cleaning & Parsing  │
                 └──────────┬───────────┘
                            │
                 ┌──────────▼───────────┐
                 │   ATS Analysis Chain │
                 │      LangChain       │
                 └──────────┬───────────┘
                            │
                 ┌──────────▼───────────┐
                 │    Google Gemini     │
                 │    AI Processing     │
                 └──────────────────────┘
```

*Architecture illustrates the intended processing flow; exact behavior depends on the current implementation.*

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── chains/
│   └── ats_chain.py
│
├── prompt/
│   ├── ats_prompt.md
│   └── prompt_reader.py
│
└── services/
    ├── pdf_parser.py
    └── resume_exactor.py
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/harshalmistri2004/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a Virtual Environment

**Windows — Git Bash**

```bash
python -m venv .venv
source .venv/Scripts/activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Your API Key

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

**Security:** Never commit `.env` or expose your API key in source code. Keep `.env` in `.gitignore`.

### 5. Launch the Application

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, typically `http://localhost:8501`.

## Application Workflow

1. Upload a resume in PDF format.
2. Extract and preprocess resume text.
3. Pass the prepared content into the available analysis workflow.
4. Review the analysis provided by the implemented application.

## Roadmap

- [ ] Job description matching
- [ ] Explainable ATS compatibility scoring
- [ ] Missing keyword and skill identification
- [ ] AI-powered resume improvement suggestions
- [ ] Downloadable analysis reports
- [ ] Automated testing and deployment

*Roadmap items represent potential enhancements, not necessarily existing features.*

## Security & Privacy

- Keep credentials in environment variables.
- Never commit API keys or other secrets.
- Treat uploaded resumes as sensitive personal information.
- Review AI-generated recommendations before using them.

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Commit your changes.
5. Open a pull request.

## Author

**Harshal Mistri**

<p>
  <a href="https://github.com/harshalmistri2004">
    <img src="https://img.shields.io/badge/GitHub-Harshal_Mistri-181717?style=for-the-badge&logo=github" alt="GitHub profile"/>
  </a>
</p>

---

<p align="center">
  <b>Built with Python and AI to support smarter resume analysis.</b>
  <br/>
  If you find this project useful, consider giving it a star.
</p>

<p align="center">
  <sub>AI-generated analysis is intended as guidance and does not guarantee ATS success or employment.</sub>
</p>
