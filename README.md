# Financial Document Analyzer - Assignment Complete ✅

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.
The system now runs smoothly after debugging and includes secure API integration, correct task distribution, and optimized AI prompts.

---

## Full Instructions & Details

```text
Set Up Environment File

An API Key is required. In the project's root directory, create a new file named .env and add your Google AI API Key:

GOOGLE_API_KEY="YOUR_REAL_API_KEY_HERE"


Running the Application

Start the server from your terminal. The application will be available at http://127.0.0.1:8000.

uvicorn main:app --reload


To use the application, navigate to the interactive documentation at:

http://127.0.0.1:8000/docs


Sample Document

The system analyzes financial documents like Tesla’s Q2 2025 financial update.

To test with Tesla’s financial document:

Download Tesla Q2 2025 update from:
Tesla Q2 2025 Update PDF

Save it as data/sample.pdf in the project directory

Or upload any financial PDF through the API endpoint


Summary of Bugs Fixed

1. Invalid API Key & Setup
Bug: Application hung on startup due to placeholder API key.
Fix: Added .env file for secure API key management and updated setup docs.

2. Faulty Agent & Task Logic
Bug: All analysis tasks were assigned to a single agent.
Fix: Re-assigned tasks to correct specialist agents (financial_analyst, investment_advisor, risk_assessor).

3. Incorrect CrewAI Syntax
Bug: Used tool instead of tools in agent definitions, breaking file-reading.
Fix: Corrected to tools, ensuring proper integration.

4. Ineffective AI Prompts
Bug: Prompts were satirical, producing random results.
Fix: Rewritten to be professional, specific, and data-driven.


Expected Features

✅ Upload financial documents (PDF format)
✅ AI-powered financial analysis
✅ Investment recommendations
✅ Risk assessment
✅ Market insights


Tech Stack

- Backend: FastAPI
- AI: Google Generative AI API
- Orchestration: CrewAI
- Server: Uvicorn
- Language: Python 3.11+


Status

🚀 The project is fully debugged, functional, and production-ready.
