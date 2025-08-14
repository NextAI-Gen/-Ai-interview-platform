# 🚀 AI Interview Platform with ATS System

> **Intelligent Interview Practice with AI-powered Question Generation and Resume Analysis**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![AI](https://img.shields.io/badge/AI-NLP%20%7C%20ML-purple.svg)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌟 **Project Overview**

An **intelligent AI-powered interview system** that conducts realistic interviews with candidates, providing instant feedback, intelligent scoring, and comprehensive performance analysis. Built with Python Flask and featuring advanced Natural Language Processing capabilities.

## 🧠 **Key Features**

### **AI-Powered Interview System**
- **Dynamic Question Generation**: AI generates context-aware questions based on role and experience
- **Real-time Feedback**: Instant analysis of answers with detailed scoring
- **Multi-role Support**: Software Developer, Data Scientist, Product Manager, General Interview
- **Follow-up Questions**: Intelligent follow-ups to probe deeper into responses

### **ATS (Applicant Tracking System)**
- **Resume Analysis**: AI-powered resume parsing and keyword analysis
- **Job Role Matching**: Identifies missing keywords and suggests improvements
- **Performance Scoring**: Comprehensive evaluation of resume quality
- **Optimization Suggestions**: Actionable recommendations for better ATS performance

### **Advanced Analytics**
- **Multi-dimensional Scoring**: 8 different metrics for comprehensive evaluation
- **Sentiment Analysis**: Detects positive/negative language patterns
- **Technical Relevance**: Matches answers against role-specific knowledge bases
- **Performance Tracking**: Historical interview performance analysis

## 🎯 **Supported Interview Roles**

- **👨‍💻 Software Developer** - Python, JavaScript, Java, DevOps, etc.
- **📊 Data Scientist** - Machine Learning, Statistics, Data Analysis
- **🎯 Product Manager** - Strategy, User Research, Agile, Metrics
- **🌐 General Interview** - Leadership, Communication, Problem Solving

## 🛠️ **Technology Stack**

- **Backend**: Python 3.8+, Flask, Flask-SocketIO
- **AI Engine**: Custom NLP algorithms, sentiment analysis, pattern recognition
- **Frontend**: HTML5, CSS3, JavaScript (ES6+), Tailwind CSS
- **Real-time**: WebSocket communication for live interview experience
- **Data**: JSON-based knowledge base with role-specific concepts
- **ATS System**: Resume parsing, keyword analysis, optimization suggestions

## 📊 **AI Analysis Metrics**

| Metric | Description | Weight |
|--------|-------------|---------|
| **Length Score** | Answer comprehensiveness | 15% |
| **Vocabulary Score** | Language diversity | 10% |
| **Technical Score** | Role-specific knowledge | 25% |
| **Structure Score** | Logical flow & organization | 15% |
| **Sentiment Score** | Positive/negative language | 5% |
| **Specificity Score** | Concrete examples & metrics | 15% |
| **Example Score** | Real-world examples | 10% |
| **Impact Score** | Results & outcomes focus | 5% |

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package installer)

### **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/NextAI-Gen/ai-interview-platform.git
   cd ai-interview-platform
   ```

2. **Create virtual environment (Recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   http://localhost:5000
   ```

## 📁 **Project Structure**

```
ai-interview-platform/
├── app.py                 # Main Flask application
├── ai_engine.py          # AI interview engine and analysis
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   └── index.html       # Main interview interface
├── static/              # Static assets
│   └── script.js        # Frontend JavaScript
├── docs/                # Documentation
├── LICENSE              # MIT License
└── README.md            # This file
```

## 🔧 **Configuration**

The application uses default configurations for development. For production deployment, consider:

- Setting up environment variables
- Configuring database connections
- Setting up proper logging
- Implementing security measures

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 **Author**

**Ankit Choudhary** - [GitHub](https://github.com/NextAI-Gen) | [LinkedIn](https://linkedin.com/in/ankit-choudhary-aanku)

## 🙏 **Acknowledgments**

- Flask community for the excellent web framework
- OpenAI for inspiration in AI-powered applications
- All contributors and testers of this project

---

⭐ **Star this repository if you find it helpful!**
