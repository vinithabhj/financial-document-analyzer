# 📊 Financial Document Analyzer 

A comprehensive **financial document analysis system** that processes corporate reports, financial statements, and investment documents using **AI-powered analysis agents**.  
The project has been fully debugged and now runs smoothly with secure API integration, correct task distribution, and optimized AI prompts.

---

## 📝 Project Overview
This system is designed to:
- Upload financial documents (PDF format)  
- Extract insights using multiple **specialist AI agents**  
- Provide **investment recommendations**, **financial health checks**, and **risk assessments**

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

## 🐛 Summary of Bugs Fixed

The project was debugged and brought to full functionality. Fixes include:

1. **Invalid API Key & Setup**

   * *Bug*: App hung due to placeholder API key
   * *Fix*: Added `.env` file for secure key management

2. **Faulty Agent & Task Logic**

   * *Bug*: All tasks assigned to one agent
   * *Fix*: Properly distributed to `financial_analyst`, `investment_advisor`, and `risk_assessor`

3. **Incorrect CrewAI Syntax**

   * *Bug*: Used `tool` instead of `tools`
   * *Fix*: Corrected to ensure file-reader integration

4. **Ineffective AI Prompts**

   * *Bug*: Prompts were satirical → produced random results
   * *Fix*: Rewritten for **professional, data-driven outputs**

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

## 📸 Screenshots

### 1. API Documentation

![API Docs](outputs/Screenshot (260).png)

### 2. Analysis Results

![Results](outputs/Screenshot (261).png)

---

