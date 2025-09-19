# 📊 Financial Document Analyzer 

A comprehensive **financial document analysis system** that processes corporate reports, financial statements, and investment documents using **AI-powered analysis agents**.  
The project has been fully debugged and now runs smoothly with secure API integration, correct task distribution, and optimized AI prompts.

---

## 📝 Project Overview
This system is designed to:
-  This project is a comprehensive financial document analysis system powered by CrewAI.
-  It accepts a financial document (in PDF format) and a user query via an API.
-  A specialized crew of AI agents then collaborates to perform a detailed financial analysis, formulate an investment recommendation, and conduct a thorough risk assessment. 
-  Extract insights using multiple **specialist AI agents**  

This repository contains the debugged and fully functional version of the original buggy codebase.

---

## ⚙️ Tech Stack
- **Python 3.11+**
- **FastAPI** – Backend framework  
- **Uvicorn** – ASGI server  
- **CrewAI** – Multi-agent orchestration  
- **Google Generative AI** – Document analysis  
- **dotenv** – Secure API key management  
- **PyPDF2** – PDF text extraction  

---

## 🚀 Setup & Installation

### 1. Install Required Libraries
```sh
pip install -r requirements.txt
````

### 2. Set Up Environment File

Create a `.env` file in the project root and add your Google AI API Key:

```env
GOOGLE_API_KEY="YOUR_REAL_API_KEY_HERE"
```

---

## ▶️ Running the Application

Start the server from your terminal:

```sh
uvicorn main:app --reload
```

The app will run at:

```
http://127.0.0.1:8000
```

For interactive API docs, open:

```
http://127.0.0.1:8000/docs
```

---

## 📑 Sample Document

You can test the system with **Tesla’s Q2 2025 Financial Update**:

1. Download from: [Tesla Q2 2025 Update PDF](https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf)
2. Save it as `data/sample.pdf` in the project folder
3. Or upload any other financial PDF using the API

---
## 🐛 Summary of Bugs Found and Fixes Implemented

The original project was non-functional due to a combination of code errors, poor AI prompt engineering, and structural flaws. Here’s a detailed breakdown of the fixes:

### 1. **Dependency and Environment (`requirements.txt`)**
* **Bug**: The `crewai` and `crewai-tools` packages had invalid version numbers that don't exist on PyPI. Several required libraries were also missing.
* **Fix**: Updated `crewai` and `crewai-tools` to recent, stable versions. Added missing dependencies: `python-dotenv` (for environment variables), `langchain-community` & `langchain-google-genai` (for LLM and document loading), and `python-multipart` (for FastAPI file uploads).

### 2. **Tooling (`tools.py`)**
* **Bug**: The `FinancialDocumentTool` was broken. It tried to use an undefined `Pdf` class and was structured as an `async` method, which is incompatible with the standard CrewAI tool structure.
* **Fix**: The tool was completely rewritten as `PDFReaderTool`. It now correctly uses the `PyPDFLoader` from `langchain_community` to read PDF content. It has been refactored into a proper synchronous CrewAI tool by inheriting from `BaseTool`, making it reliable and easy for agents to use.

### 3. **AI Agent Prompts (`agents.py`)**
* **Bug**: The prompts (`role`, `goal`, `backstory`) for all agents were inefficient and unprofessional, instructing them to generate sarcastic, incorrect, and unhelpful responses.
* **Fix**: All agent prompts have been rewritten from scratch. They are now professional, specific, and goal-oriented, guiding the AI to perform high-quality, specialized tasks. For example, the `financial_analyst` is no longer an "inexperienced" analyst but a "Senior Financial Analyst" focused on data-driven insights.

### 4. **LLM Initialization (`agents.py`)**
* **Bug**: The code had a critical error `llm = llm`, which meant no Large Language Model was ever initialized.
* **Fix**: Implemented proper LLM initialization using `ChatGoogleGenerativeAI` from the `langchain-google-genai` library, which connects to Google's Gemini models.

### 5. **Task Definitions (`task.py`)**
* **Bug**: Task descriptions were vague and unhelpful (e.g., "Maybe solve the user's query"). They also failed to pass the file path to the agents.
* **Fix**: All tasks were redefined to create a clear, multi-step workflow. Each task now has a precise `description` and `expected_output`, and the `{file_path}` variable is correctly passed to ensure agents know which document to analyze. The tasks now build on each other using the `context` parameter.

### 6. **Core Application Logic (`main.py`)**
* **Bug**: The main structural flaw was that the `Crew` was initialized with only a single agent and a single task. This prevented any meaningful collaboration and failed to use the other defined agents and tasks.
* **Fix**: The `run_crew` function was re-engineered to create a complete `Crew` with the full team of specialized agents (`financial_analyst`, `investment_advisor`, `risk_assessor`) and a logical sequence of tasks. This ensures a comprehensive analysis is performed from start to finish. The `kickoff` method was also corrected to pass all necessary inputs (`query` and `file_path`) to the tasks.
* 
---

## ✅ Expected Features

* 📂 Upload financial documents (PDF format)
* 🤖 AI-powered financial analysis
* 💡 Investment recommendations
* ⚠️ Risk assessment
* 📊 Market insights

---

## 🔄 Demo Workflow

1. Upload a financial PDF
2. **Financial Analyst** → Extracts ratios, evaluates performance
3. **Investment Advisor** → Provides investment recommendations
4. **Risk Assessor** → Highlights risks & mitigation strategies
5. Consolidated results returned as structured insights

---

### 🖼️ Screenshots

**1. API Documentation**

![API Docs](outputs/Screenshot%20(261).png)

**2. Analysis Results**

![Results](outputs/Screenshot%20(260).png)

---

