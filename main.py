from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import uvicorn

from crewai import Crew, Process
# Correctly import the agents that will be used in the crew
from agents import financial_analyst, investment_advisor, risk_assessor
# Import the tasks that are now correctly assigned to the agents
from task import analyze_financial_document, investment_analysis, risk_assessment

app = FastAPI(
    title="Financial Document Analyzer API",
    description="An AI-powered system to analyze financial documents and provide investment insights."
)

def run_crew(query: str, file_path: str):
    """Initializes and runs the financial analysis crew."""

    tasks = [
        analyze_financial_document,
        investment_analysis,
        risk_assessment
    ]

    # Define the crew with the correct agents
    financial_crew = Crew(
        agents=[financial_analyst, investment_advisor, risk_assessor],
        tasks=tasks,
        process=Process.sequential,
        verbose=2
    )

    # Kick off the crew with the query and file path
    result = financial_crew.kickoff({'query': query, 'file_path': file_path})
    return result

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_financial_document_endpoint(
    file: UploadFile = File(...),
    query: str = Form(default="Provide a comprehensive analysis of this financial document. Include a summary of key financial highlights, an investment recommendation, and a thorough risk assessment.")
):
    """Analyzes a financial document and returns a comprehensive report."""

    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        # Save the uploaded file temporarily
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Process the document with the CrewAI crew
        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")

    finally:
        # Clean up by removing the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)