@echo off

:: Ensure you're in the project directory
cd /d "%~dp0"

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/
    pause
    exit /b
)

:: Create and activate the virtual environment (optional)
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

:: Install dependencies from requirements.txt
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

:: Run Behave tests
echo Running Behave tests...
behave

:: Deactivate the virtual environment
deactivate

pause
