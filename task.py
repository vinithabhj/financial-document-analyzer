from crewai import Task
from agents import financial_analyst, investment_advisor, risk_assessor
from tools import pdf_reader_tool

# Task 1: Financial Analysis
analyze_financial_document = Task(
    description="""Analyze the financial document located at {file_path}. 
    Focus on key financial metrics such as revenue, net income, gross profit, operating margin, and cash flow. 
    Extract and summarize the most important figures, identify significant year-over-year (YoY) trends, and provide a concise summary of the company's overall financial performance as presented in the report. 
    The user's initial query is: {query}""",
    expected_output="""A detailed, data-driven summary of the company's financial health based *only* on the provided document.
    The output must be in Markdown format and include:
    - A 'Key Financial Highlights' section with bullet points for major metrics (e.g., Total Revenue, Net Income, EPS).
    - A 'Performance Trends' section analyzing YoY changes and other significant patterns.
    - A concluding 'Overall Financial Health Summary' paragraph.""",
    agent=financial_analyst, # Assigned to the correct agent
    tools=[pdf_reader_tool]
)

# Task 2: Investment Analysis
investment_analysis = Task(
    description="""Using the financial analysis report, formulate a well-reasoned investment recommendation.
    Evaluate the company's strengths (e.g., revenue growth, profitability) and weaknesses (e.g., declining margins, high debt) to build your case.
    Conclude with a clear 'Buy', 'Hold', or 'Sell' recommendation.""",
    expected_output="""A professional investment analysis in Markdown format.
    The output must include:
    - An 'Investment Thesis' section outlining the core reasoning.
    - A 'Strengths and Opportunities' section (bullet points).
    - A 'Weaknesses and Concerns' section (bullet points).
    - A final, bolded 'Recommendation' (e.g., **Recommendation: Buy**).""",
    agent=investment_advisor, # Assigned to the correct agent
    context=[analyze_financial_document] # This task depends on the output of the first task
)

# Task 3: Risk Assessment
risk_assessment = Task(
    description="""Based on the financial document and the preceding analysis, conduct a thorough risk assessment.
    Identify potential risks from the report, such as market volatility, operational challenges, regulatory issues, or competition mentioned in the outlook sections.
    Categorize these risks and explain their potential impact on the company.""",
    expected_output="""A comprehensive risk assessment report in Markdown format.
    The output must include:
    - A 'Key Risk Factors' section.
    - Bullet points for each identified risk, categorized (e.g., Market Risk, Operational Risk, Regulatory Risk).
    - A brief explanation of the potential impact of each risk.""",
    agent=risk_assessor, # Assigned to the correct agent
    context=[analyze_financial_document, investment_analysis] # Depends on both prior tasks
)