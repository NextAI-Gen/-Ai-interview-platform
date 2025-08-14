from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import json
from datetime import datetime
import random
from ai_engine import AIInterviewer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app, cors_allowed_origins="*")

# Interview sessions storage
interview_sessions = {}

# Interview questions are now handled by the AI engine

# AI Interviewer class is now imported from ai_engine.py

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/roles')
def get_roles():
    # Get roles from the AI engine knowledge base
    from ai_engine import AdvancedAIEngine
    ai_engine = AdvancedAIEngine()
    return jsonify(list(ai_engine.knowledge_base.keys()) + ['general'])

# Socket.IO events
@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Client disconnected: {request.sid}')
    if request.sid in interview_sessions:
        del interview_sessions[request.sid]

@socketio.on('start-interview')
def handle_start_interview(data):
    role = data.get('role', 'general')
    candidate_name = data.get('candidateName', 'Candidate')
    
    # Create new interviewer instance
    interviewer = AIInterviewer(role)
    
    # Store session
    interview_sessions[request.sid] = {
        'interviewer': interviewer,
        'candidateName': candidate_name,
        'startTime': datetime.now(),
        'status': 'active'
    }
    
    # Get first question
    first_question = interviewer.get_next_question()
    
    emit('interview-started', {
        'message': f'Welcome {candidate_name}! Let\'s begin your {role} interview.',
        'firstQuestion': first_question
    })

@socketio.on('submit-answer')
def handle_submit_answer(data):
    session = interview_sessions.get(request.sid)
    if not session:
        emit('error', {'message': 'No active interview session found.'})
        return
    
    answer = data.get('answer', '')
    question = data.get('question', '')
    
    if not answer or len(answer.strip()) < 10:
        emit('error', {'message': 'Please provide a detailed answer (at least 10 characters).'})
        return
    
    # Evaluate answer
    evaluation = session['interviewer'].evaluate_answer(answer, question)
    emit('answer-evaluated', evaluation)
    
    # Get next question
    next_question = session['interviewer'].get_next_question()
    if next_question:
        emit('next-question', next_question)
    else:
        # Interview completed
        summary = session['interviewer'].get_interview_summary()
        session['status'] = 'completed'
        session['endTime'] = datetime.now()
        session['summary'] = summary
        
        emit('interview-completed', summary)

@socketio.on('request-feedback')
def handle_request_feedback():
    session = interview_sessions.get(request.sid)
    if session and session.get('status') == 'completed':
        emit('interview-feedback', session['summary'])

if __name__ == '__main__':
    print("🚀 Starting AI Interview System...")
    print("📱 Open http://localhost:5000 in your browser")
    print("🤖 AI Interview System is ready!")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
