@echo off
echo 🚀 AI Interview Platform
echo ========================================
echo.
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo ✅ Python detected
echo.
echo Installing/updating dependencies...
pip install -r requirements.txt

echo.
echo 🎯 Starting AI Interview Platform...
echo 📱 Open your browser and go to: http://localhost:5000
echo ⏹️  Press Ctrl+C to stop the application
echo ========================================
echo.

python run.py

pause
