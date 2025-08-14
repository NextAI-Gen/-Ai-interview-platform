// Global variables
let socket;
let currentInterviewData = {};
let currentQuestion = null;

// DOM elements
const setupSection = document.getElementById('setup-section');
const interviewSection = document.getElementById('interview-section');
const resultsSection = document.getElementById('results-section');
const interviewForm = document.getElementById('interview-form');
const chatMessages = document.getElementById('chat-messages');
const currentQuestionText = document.getElementById('current-question-text');
const answerInput = document.getElementById('answer-input');
const submitAnswerBtn = document.getElementById('submit-answer-btn');
const charCount = document.getElementById('char-count');
const questionCounter = document.getElementById('question-counter');
const currentRole = document.getElementById('current-role');
const finalScore = document.getElementById('final-score');
const scoreLabel = document.getElementById('score-label');
const overallFeedback = document.getElementById('overall-feedback');
const detailedFeedback = document.getElementById('detailed-feedback');
const restartInterviewBtn = document.getElementById('restart-interview-btn');
const downloadResultsBtn = document.getElementById('download-results-btn');

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeSocket();
    setupEventListeners();
    setupCharacterCounter();
});

// Initialize Socket.IO connection
function initializeSocket() {
    socket = io();
    
    socket.on('connect', () => {
        console.log('Connected to Python Flask server');
    });

    socket.on('interview-started', (data) => {
        console.log('Interview started:', data);
        startInterview(data);
    });

    socket.on('next-question', (questionData) => {
        console.log('Next question:', questionData);
        displayNextQuestion(questionData);
    });

    socket.on('answer-evaluated', (evaluation) => {
        console.log('Answer evaluated:', evaluation);
        displayAnswerEvaluation(evaluation);
    });

    socket.on('interview-completed', (summary) => {
        console.log('Interview completed:', summary);
        showInterviewResults(summary);
    });

    socket.on('error', (error) => {
        console.error('Socket error:', error);
        showError(error.message);
    });
}

// Setup event listeners
function setupEventListeners() {
    // Interview form submission
    interviewForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const candidateName = document.getElementById('candidate-name').value;
        const role = document.getElementById('interview-role').value;
        
        if (!candidateName || !role) {
            showError('Please fill in all fields');
            return;
        }

        startInterviewSetup(candidateName, role);
    });

    // Submit answer button
    submitAnswerBtn.addEventListener('click', submitAnswer);

    // Restart interview button
    restartInterviewBtn.addEventListener('click', restartInterview);

    // Download results button
    downloadResultsBtn.addEventListener('click', downloadResults);
}

// Setup character counter for answer input
function setupCharacterCounter() {
    answerInput.addEventListener('input', function() {
        const count = this.value.length;
        charCount.textContent = count;
        
        // Enable/disable submit button based on input length
        submitAnswerBtn.disabled = count < 10;
    });
}

// Start interview setup
function startInterviewSetup(candidateName, role) {
    currentInterviewData = {
        candidateName,
        role,
        startTime: new Date()
    };

    // Show loading state
    const submitBtn = interviewForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Starting Interview...';
    submitBtn.disabled = true;

    // Emit start interview event
    socket.emit('start-interview', {
        role: role,
        candidateName: candidateName
    });
}

// Start the interview
function startInterview(data) {
    // Hide setup section and show interview section
    setupSection.classList.add('hidden');
    interviewSection.classList.remove('hidden');
    resultsSection.classList.add('hidden');

    // Update interview header
    currentRole.textContent = data.message.split(' ').pop().replace('!', '');
    
    // Display welcome message
    addMessage('ai', data.message, 'welcome');
    
    // Display first question
    if (data.firstQuestion) {
        displayNextQuestion(data.firstQuestion);
    }

    // Reset form
    interviewForm.reset();
    submitAnswerBtn.disabled = true;
}

// Display next question
function displayNextQuestion(questionData) {
    currentQuestion = questionData;
    
    // Update question counter
    questionCounter.textContent = `${questionData.questionNumber}/${questionData.totalQuestions}`;
    
    // Update current question display
    currentQuestionText.textContent = questionData.question;
    
    // Add question to chat
    addMessage('ai', questionData.question, 'question');
    
    // Clear previous answer
    answerInput.value = '';
    charCount.textContent = '0';
    submitAnswerBtn.disabled = true;
    
    // Focus on answer input
    answerInput.focus();
}

// Submit answer
function submitAnswer() {
    const answer = answerInput.value.trim();
    
    if (!answer || answer.length < 10) {
        showError('Please provide a detailed answer (at least 10 characters)');
        return;
    }

    if (!currentQuestion) {
        showError('No current question available');
        return;
    }

    // Disable submit button and show loading
    submitAnswerBtn.disabled = true;
    submitAnswerBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Evaluating...';

    // Add user answer to chat
    addMessage('user', answer, 'answer');

    // Emit answer to server
    socket.emit('submit-answer', {
        answer: answer,
        question: currentQuestion.question
    });

    // Clear input
    answerInput.value = '';
    charCount.textContent = '0';
}

// Display answer evaluation
function displayAnswerEvaluation(evaluation) {
    // Re-enable submit button
    submitAnswerBtn.disabled = false;
    submitAnswerBtn.innerHTML = '<i class="fas fa-paper-plane mr-2"></i>Submit Answer';

    // Add evaluation to chat
    addMessage('ai', `Score: ${evaluation.score}/100\n\nFeedback: ${evaluation.feedback}`, 'evaluation');
    
    // Show typing indicator for next question
    showTypingIndicator();
}

// Show typing indicator
function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'flex items-center space-x-2 text-gray-500 italic';
    typingDiv.innerHTML = `
        <div class="typing-indicator"></div>
        <span>Python AI is preparing the next question...</span>
    `;
    typingDiv.id = 'typing-indicator';
    
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Hide typing indicator
function hideTypingIndicator() {
    const typingIndicator = document.getElementById('typing-indicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

// Show interview results
function showInterviewResults(summary) {
    // Hide interview section and show results
    interviewSection.classList.add('hidden');
    resultsSection.classList.remove('hidden');
    
    // Update results display
    finalScore.textContent = summary.averageScore;
    scoreLabel.textContent = getScoreLabel(summary.averageScore);
    overallFeedback.textContent = summary.overallFeedback;
    
    // Display detailed feedback
    displayDetailedFeedback(summary.detailedFeedback);
    
    // Display AI insights
    displayAIInsights(summary.aiInsights);
    
    // Display performance analysis
    displayPerformanceAnalysis(summary.improvementAreas, summary.strengths);
    
    // Store results for download
    currentInterviewData.results = summary;
}

// Get score label
function getScoreLabel(score) {
    if (score >= 90) return 'Excellent';
    if (score >= 80) return 'Very Good';
    if (score >= 70) return 'Good';
    if (score >= 60) return 'Fair';
    return 'Needs Improvement';
}

// Display detailed feedback
function displayDetailedFeedback(feedbackArray) {
    detailedFeedback.innerHTML = '';
    
    feedbackArray.forEach((item, index) => {
        const feedbackDiv = document.createElement('div');
        feedbackDiv.className = 'bg-gray-50 rounded-lg p-4';
        feedbackDiv.innerHTML = `
            <div class="flex justify-between items-start mb-2">
                <h4 class="font-semibold text-gray-800">Question ${index + 1}</h4>
                <span class="bg-blue-100 text-blue-800 text-sm font-semibold px-2 py-1 rounded">${item.score}/100</span>
            </div>
            <p class="text-gray-700 mb-2"><strong>Q:</strong> ${item.question}</p>
            <p class="text-gray-700 mb-2"><strong>A:</strong> ${item.answer}</p>
            <p class="text-gray-600 italic">${item.feedback}</p>
            ${item.follow_up ? `<p class="text-blue-600 mt-2"><strong>Follow-up:</strong> ${item.follow_up}</p>` : ''}
        `;
        detailedFeedback.appendChild(feedbackDiv);
    });
}

// Display AI insights
function displayAIInsights(aiInsights) {
    const aiInsightsContainer = document.getElementById('ai-insights');
    if (!aiInsightsContainer || !aiInsights) return;
    
    aiInsightsContainer.innerHTML = '';
    
    // Display summary insight
    if (aiInsights.summary) {
        const summaryDiv = document.createElement('div');
        summaryDiv.className = 'col-span-2 bg-purple-50 border-l-4 border-purple-500 p-4 rounded';
        summaryDiv.innerHTML = `
            <h4 class="font-semibold text-purple-800 mb-2">AI Analysis Summary</h4>
            <p class="text-purple-700">${aiInsights.summary}</p>
        `;
        aiInsightsContainer.appendChild(summaryDiv);
    }
    
    // Display metric scores
    const metrics = [
        { key: 'communication_strength', label: 'Communication', icon: 'fas fa-comments', color: 'blue' },
        { key: 'technical_depth', label: 'Technical Depth', icon: 'fas fa-code', color: 'green' },
        { key: 'answer_quality', label: 'Answer Quality', icon: 'fas fa-star', color: 'yellow' },
        { key: 'concrete_examples', label: 'Examples Used', icon: 'fas fa-lightbulb', color: 'purple' },
        { key: 'impact_focus', label: 'Impact Focus', icon: 'fas fa-chart-line', color: 'red' }
    ];
    
    metrics.forEach(metric => {
        if (aiInsights[metric.key] !== undefined) {
            const score = Math.round(aiInsights[metric.key] * 100);
            const scoreDiv = document.createElement('div');
            scoreDiv.className = 'bg-white border rounded-lg p-4 text-center';
            scoreDiv.innerHTML = `
                <i class="${metric.icon} text-${metric.color}-500 text-2xl mb-2"></i>
                <h4 class="font-semibold text-gray-800 mb-1">${metric.label}</h4>
                <div class="text-2xl font-bold text-${metric.color}-600">${score}%</div>
                <div class="w-full bg-gray-200 rounded-full h-2 mt-2">
                    <div class="bg-${metric.color}-500 h-2 rounded-full" style="width: ${score}%"></div>
                </div>
            `;
            aiInsightsContainer.appendChild(scoreDiv);
        }
    });
}

// Display performance analysis
function displayPerformanceAnalysis(improvementAreas, strengths) {
    const strengthsList = document.getElementById('strengths-list');
    const improvementList = document.getElementById('improvement-list');
    
    if (strengthsList) {
        if (strengths && strengths.length > 0) {
            strengthsList.innerHTML = strengths.map(strength => 
                `<div class="flex items-center mb-2">
                    <i class="fas fa-check-circle text-green-600 mr-2"></i>
                    <span>${strength}</span>
                </div>`
            ).join('');
        } else {
            strengthsList.innerHTML = '<p class="text-gray-500 italic">No specific strengths identified yet.</p>';
        }
    }
    
    if (improvementList) {
        if (improvementAreas && improvementAreas.length > 0) {
            improvementList.innerHTML = improvementAreas.map(area => 
                `<div class="flex items-center mb-2">
                    <i class="fas fa-arrow-up text-yellow-600 mr-2"></i>
                    <span>${area}</span>
                </div>`
            ).join('');
        } else {
            improvementList.innerHTML = '<p class="text-gray-500 italic">Great job! No major improvement areas identified.</p>';
        }
    }
}

// Restart interview
function restartInterview() {
    // Reset all sections
    setupSection.classList.remove('hidden');
    interviewSection.classList.add('hidden');
    resultsSection.classList.add('hidden');
    
    // Clear chat messages
    chatMessages.innerHTML = '';
    
    // Reset form
    interviewForm.reset();
    
    // Reset current data
    currentInterviewData = {};
    currentQuestion = null;
    
    // Reset submit button
    submitAnswerBtn.disabled = false;
    submitAnswerBtn.innerHTML = '<i class="fas fa-paper-plane mr-2"></i>Submit Answer';
}

// Download results
function downloadResults() {
    if (!currentInterviewData.results) {
        showError('No results available to download');
        return;
    }

    const results = currentInterviewData.results;
    const candidateName = currentInterviewData.candidateName;
    const role = currentInterviewData.role;
    const date = new Date().toLocaleDateString();

    // Create CSV content
    let csvContent = `AI Interview Results (Python Edition)\n`;
    csvContent += `Candidate: ${candidateName}\n`;
    csvContent += `Role: ${role}\n`;
    csvContent += `Date: ${date}\n`;
    csvContent += `Overall Score: ${results.averageScore}/100\n\n`;
    csvContent += `Question,Answer,Score,Feedback\n`;

    results.detailedFeedback.forEach((item, index) => {
        csvContent += `"${item.question}","${item.answer}",${item.score},"${item.feedback}"\n`;
    });

    // Create and download file
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `python-interview-results-${candidateName}-${date}.csv`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

// Add message to chat
function addMessage(sender, content, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-bubble flex ${sender === 'ai' ? 'justify-start' : 'justify-end'}`;
    
    const messageContent = document.createElement('div');
    messageContent.className = `max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
        sender === 'ai' 
            ? 'bg-blue-100 text-blue-900' 
            : 'bg-green-100 text-green-900'
    }`;
    
    // Format content based on type
    if (type === 'evaluation') {
        messageContent.innerHTML = content.replace(/\n/g, '<br>');
    } else {
        messageContent.textContent = content;
    }
    
    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    // Hide typing indicator if it exists
    hideTypingIndicator();
}

// Show error message
function showError(message) {
    // Create error notification
    const errorDiv = document.createElement('div');
    errorDiv.className = 'fixed top-4 right-4 bg-red-500 text-white px-6 py-3 rounded-lg shadow-lg z-50';
    errorDiv.innerHTML = `
        <div class="flex items-center space-x-2">
            <i class="fas fa-exclamation-triangle"></i>
            <span>${message}</span>
        </div>
    `;
    
    document.body.appendChild(errorDiv);
    
    // Remove after 5 seconds
    setTimeout(() => {
        if (errorDiv.parentNode) {
            errorDiv.parentNode.removeChild(errorDiv);
        }
    }, 5000);
}

// Show success message
function showSuccess(message) {
    const successDiv = document.createElement('div');
    successDiv.className = 'fixed top-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50';
    successDiv.innerHTML = `
        <div class="flex items-center space-x-2">
            <i class="fas fa-check-circle"></i>
            <span>${message}</span>
        </div>
    `;
    
    document.body.appendChild(successDiv);
    
    setTimeout(() => {
        if (successDiv.parentNode) {
            successDiv.parentNode.removeChild(successDiv);
        }
    }, 5000);
}
