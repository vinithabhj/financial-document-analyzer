import os
from dotenv import load_dotenv
from crewai_tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader Tool"
    description: str = "Reads the text content from a financial PDF document, given its file path."

    def _run(self, file_path: str) -> str:
        """A tool to read and extract text from a PDF file."""

        # Check if the file exists
        if not os.path.exists(file_path):
            return f"Error: The file at path {file_path} was not found."

        # Load the PDF and extract text
        try:
            loader = PyPDFLoader(file_path)
            pages = loader.load_and_split()

            full_text = "".join(page.page_content for page in pages)

            # Basic cleaning
            cleaned_text = " ".join(full_text.split())

            return cleaned_text
        except Exception as e:
            return f"Error reading PDF file: {e}"

# Instantiate the tool for use in agents
pdf_reader_tool = FinancialDocumentTool()