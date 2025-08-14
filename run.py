#!/usr/bin/env python3
"""
AI Interview Platform Runner Script
Simple script to start the AI Interview application
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import flask
        import flask_socketio
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Installing dependencies...")
        return False

def install_dependencies():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def main():
    """Main function to run the AI Interview platform"""
    print("🚀 AI Interview Platform")
    print("=" * 40)
    
    # Check Python version
    check_python_version()
    
    # Check and install dependencies if needed
    if not check_dependencies():
        if not install_dependencies():
            sys.exit(1)
    
    # Start the application
    print("\n🎯 Starting AI Interview Platform...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the application")
    print("=" * 40)
    
    try:
        # Import and run the Flask app
        from app import app, socketio
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n\n👋 AI Interview Platform stopped")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
