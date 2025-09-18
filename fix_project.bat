@echo off
echo =================================================================
echo == This script will perform a full reset and installation.     ==
echo =================================================================
echo.
echo [STEP 1] Cleaning up old environment and pip cache...
if exist venv rmdir /s /q venv
pip cache purge
echo.
echo [STEP 2] Creating and activating a new virtual environment...
python -m venv venv
call venv\Scripts\activate.bat
echo.
echo [STEP 3] Creating a perfect 'requirements.txt' file...
(
    echo crewai==0.35.8
    echo crewai-tools==0.4.0
    echo fastapi==0.111.0
    echo uvicorn==0.29.0
    echo python-dotenv==1.0.1
    echo langchain-google-genai==1.0.1
    echo langchain-community==0.0.38
    echo python-multipart==0.0.9
) > requirements.txt
echo File has been created successfully.
echo.

echo [STEP 4] Installing all packages from the clean file...
pip install --no-cache-dir -r requirements.txt
echo.

echo =================================================================
echo == SETUP COMPLETE!
==
echo == If you see no red ERROR messages above, it is fixed.
==
echo ==                                                             ==
echo == You can now start the server with the command:              ==
echo == python -m uvicorn main:app --reload
==
echo =================================================================
pause