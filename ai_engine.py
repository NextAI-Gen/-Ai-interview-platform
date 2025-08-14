import re
import random
from datetime import datetime

class AdvancedAIEngine:
    def __init__(self):
        # Load knowledge base for different roles
        self.knowledge_base = self._load_knowledge_base()
    
    def _load_knowledge_base(self):
        """Load role-specific knowledge base with key concepts and terms"""
        return {
            'software-developer': {
                'concepts': [
                    'object-oriented programming', 'design patterns', 'data structures',
                    'algorithms', 'version control', 'testing', 'debugging',
                    'code review', 'agile methodology', 'clean code',
                    'refactoring', 'performance optimization', 'security',
                    'database design', 'API development', 'microservices',
                    'containerization', 'CI/CD', 'monitoring', 'logging'
                ],
                'technologies': [
                    'python', 'javascript', 'java', 'c++', 'c#', 'go', 'rust',
                    'react', 'angular', 'vue', 'node.js', 'django', 'flask',
                    'spring', 'docker', 'kubernetes', 'aws', 'azure', 'gcp',
                    'git', 'jenkins', 'jira', 'confluence'
                ],
                'skills': [
                    'problem solving', 'analytical thinking', 'attention to detail',
                    'communication', 'teamwork', 'time management', 'learning ability',
                    'creativity', 'adaptability', 'leadership'
                ]
            },
            'data-scientist': {
                'concepts': [
                    'machine learning', 'deep learning', 'statistical analysis',
                    'data preprocessing', 'feature engineering', 'model validation',
                    'cross-validation', 'overfitting', 'bias-variance tradeoff',
                    'ensemble methods', 'neural networks', 'natural language processing',
                    'computer vision', 'time series analysis', 'clustering',
                    'classification', 'regression', 'dimensionality reduction'
                ],
                'technologies': [
                    'python', 'r', 'sql', 'pandas', 'numpy', 'scikit-learn',
                    'tensorflow', 'pytorch', 'keras', 'matplotlib', 'seaborn',
                    'plotly', 'jupyter', 'spark', 'hadoop', 'aws sagemaker',
                    'google colab', 'kaggle', 'tableau', 'power bi'
                ],
                'skills': [
                    'mathematical thinking', 'statistical reasoning', 'data intuition',
                    'business acumen', 'storytelling', 'critical thinking',
                    'experimental design', 'hypothesis testing', 'data visualization'
                ]
            },
            'product-manager': {
                'concepts': [
                    'product strategy', 'market research', 'user research',
                    'user experience', 'product lifecycle', 'roadmapping',
                    'prioritization', 'stakeholder management', 'agile methodology',
                    'scrum', 'kanban', 'sprint planning', 'retrospectives',
                    'metrics and KPIs', 'A/B testing', 'customer feedback',
                    'competitive analysis', 'go-to-market strategy', 'pricing strategy'
                ],
                'technologies': [
                    'jira', 'confluence', 'figma', 'sketch', 'invision',
                    'mixpanel', 'amplitude', 'google analytics', 'hotjar',
                    'userzoom', 'typeform', 'survey monkey', 'slack',
                    'zoom', 'microsoft teams', 'notion', 'airtable'
                ],
                'skills': [
                    'leadership', 'communication', 'strategic thinking',
                    'user empathy', 'data analysis', 'project management',
                    'negotiation', 'presentation', 'decision making',
                    'problem solving', 'creativity', 'adaptability'
                ]
            }
        }
    
    def analyze_answer_sophistication(self, answer, question, role):
        """Analyze the sophistication and depth of an answer"""
        # Text preprocessing
        processed_answer = self._preprocess_text(answer)
        
        # Calculate various metrics
        metrics = {
            'length_score': self._calculate_length_score(answer),
            'vocabulary_score': self._calculate_vocabulary_score(processed_answer),
            'technical_score': self._calculate_technical_relevance(processed_answer, role),
            'structure_score': self._calculate_structure_score(answer),
            'sentiment_score': self._calculate_sentiment_score(answer),
            'specificity_score': self._calculate_specificity_score(answer),
            'example_score': self._calculate_example_score(answer),
            'impact_score': self._calculate_impact_score(answer)
        }
        
        return metrics
    
    def _preprocess_text(self, text):
        """Preprocess text for analysis"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters but keep important ones
        text = re.sub(r'[^a-zA-Z0-9\s\.\,\!\?\-]', ' ', text)
        
        # Split into words
        words = text.split()
        
        # Remove very short words
        processed_words = [word for word in words if len(word) > 2]
        
        return ' '.join(processed_words)
    
    def _calculate_length_score(self, answer):
        """Calculate score based on answer length"""
        words = len(answer.split())
        if words < 20:
            return 0.3
        elif words < 50:
            return 0.6
        elif words < 100:
            return 0.8
        else:
            return 1.0
    
    def _calculate_vocabulary_score(self, processed_answer):
        """Calculate vocabulary diversity score"""
        words = processed_answer.split()
        if not words:
            return 0.0
        
        unique_words = len(set(words))
        total_words = len(words)
        
        # Type-token ratio
        ttr = unique_words / total_words if total_words > 0 else 0
        
        # Normalize to 0-1 scale
        return min(ttr * 2, 1.0)
    
    def _calculate_technical_relevance(self, processed_answer, role):
        """Calculate technical relevance to the role"""
        if role not in self.knowledge_base:
            return 0.5
        
        role_concepts = (
            self.knowledge_base[role]['concepts'] +
            self.knowledge_base[role]['technologies'] +
            self.knowledge_base[role]['skills']
        )
        
        if not role_concepts:
            return 0.5
        
        # Count matches with role concepts
        answer_words = set(processed_answer.lower().split())
        concept_words = set()
        for concept in role_concepts:
            concept_words.update(concept.lower().split())
        
        # Calculate overlap
        matches = len(answer_words.intersection(concept_words))
        total_concept_words = len(concept_words)
        
        if total_concept_words == 0:
            return 0.5
        
        relevance = min(matches / (total_concept_words * 0.1), 1.0)  # Normalize
        return relevance
    
    def _calculate_structure_score(self, answer):
        """Calculate structural quality score"""
        sentences = answer.split('.')
        if len(sentences) < 2:
            return 0.3
        
        # Check for logical connectors
        connectors = ['because', 'therefore', 'however', 'although', 'furthermore', 'additionally']
        connector_count = sum(1 for connector in connectors if connector.lower() in answer.lower())
        
        # Check for bullet points or numbered lists
        has_structure = bool(re.search(r'[\-\*]\s|\d+\.\s', answer))
        
        base_score = min(connector_count * 0.2, 0.6)
        structure_bonus = 0.2 if has_structure else 0
        
        return min(base_score + structure_bonus, 1.0)
    
    def _calculate_sentiment_score(self, answer):
        """Calculate sentiment positivity score"""
        positive_words = ['good', 'great', 'excellent', 'successful', 'improved', 'achieved', 'solved', 'created', 'developed', 'implemented']
        negative_words = ['bad', 'failed', 'problem', 'issue', 'difficult', 'challenging', 'struggled', 'complicated']
        
        answer_lower = answer.lower()
        positive_count = sum(1 for word in positive_words if word in answer_lower)
        negative_count = sum(1 for word in negative_words if word in answer_lower)
        
        if positive_count == 0 and negative_count == 0:
            return 0.5
        
        total = positive_count + negative_count
        positive_ratio = positive_count / total
        
        return positive_ratio
    
    def _calculate_specificity_score(self, answer):
        """Calculate specificity and concreteness score"""
        # Look for specific numbers, dates, names, technologies
        specific_patterns = [
            r'\d+%', r'\d+ years?', r'\d+ months?', r'\d+ weeks?',
            r'\$\d+', r'\d+ users?', r'\d+ customers?', r'\d+ projects?',
            r'[A-Z][a-z]+ [A-Z][a-z]+',  # Names
            r'[A-Z]{2,}',  # Acronyms
            r'v\d+\.\d+',  # Version numbers
        ]
        
        pattern_matches = sum(1 for pattern in specific_patterns if re.search(pattern, answer))
        return min(pattern_matches * 0.2, 1.0)
    
    def _calculate_example_score(self, answer):
        """Calculate score for providing examples"""
        # Look for example indicators
        example_indicators = [
            'for example', 'for instance', 'such as', 'like',
            'specifically', 'in particular', 'one time', 'recently',
            'when i', 'i worked on', 'i developed', 'i created'
        ]
        
        indicator_count = sum(1 for indicator in example_indicators if indicator.lower() in answer.lower())
        return min(indicator_count * 0.25, 1.0)
    
    def _calculate_impact_score(self, answer):
        """Calculate score for discussing impact and results"""
        impact_indicators = [
            'increased', 'decreased', 'improved', 'reduced',
            'achieved', 'accomplished', 'delivered', 'completed',
            'resulted in', 'led to', 'caused', 'impact',
            'outcome', 'result', 'success', 'efficiency'
        ]
        
        indicator_count = sum(1 for indicator in impact_indicators if indicator.lower() in answer.lower())
        return min(indicator_count * 0.2, 1.0)
    
    def generate_intelligent_score(self, answer, question, role):
        """Generate intelligent score based on multiple factors"""
        metrics = self.analyze_answer_sophistication(answer, question, role)
        
        # Weighted scoring system
        weights = {
            'length_score': 0.15,
            'vocabulary_score': 0.10,
            'technical_score': 0.25,
            'structure_score': 0.15,
            'sentiment_score': 0.05,
            'specificity_score': 0.15,
            'example_score': 0.10,
            'impact_score': 0.05
        }
        
        # Calculate weighted score
        total_score = sum(metrics[key] * weights[key] for key in weights)
        
        # Convert to 60-100 scale (minimum passing score)
        final_score = int(60 + (total_score * 40))
        
        return final_score, metrics
    
    def generate_intelligent_feedback(self, answer, question, role, metrics):
        """Generate intelligent, personalized feedback"""
        feedback_parts = []
        
        # Length feedback
        if metrics['length_score'] < 0.5:
            feedback_parts.append("Consider providing more detailed answers with specific examples.")
        
        # Technical relevance feedback
        if metrics['technical_score'] < 0.6:
            feedback_parts.append("Try to incorporate more role-specific technical concepts and terminology.")
        
        # Structure feedback
        if metrics['structure_score'] < 0.6:
            feedback_parts.append("Organize your answer with clear structure and logical flow.")
        
        # Specificity feedback
        if metrics['specificity_score'] < 0.5:
            feedback_parts.append("Include specific numbers, metrics, or concrete examples to strengthen your response.")
        
        # Example feedback
        if metrics['example_score'] < 0.5:
            feedback_parts.append("Support your points with real-world examples or personal experiences.")
        
        # Impact feedback
        if metrics['impact_score'] < 0.5:
            feedback_parts.append("Discuss the impact and results of your actions or decisions.")
        
        # Positive reinforcement
        strengths = []
        if metrics['technical_score'] > 0.7:
            strengths.append("strong technical knowledge")
        if metrics['structure_score'] > 0.7:
            strengths.append("well-organized response")
        if metrics['specificity_score'] > 0.7:
            strengths.append("specific examples")
        if metrics['example_score'] > 0.7:
            strengths.append("good use of examples")
        
        if strengths:
            feedback_parts.insert(0, f"Excellent work on {', '.join(strengths)}!")
        
        # Generate personalized suggestions
        suggestions = self._generate_role_specific_suggestions(role, metrics)
        if suggestions:
            feedback_parts.append(suggestions)
        
        return ' '.join(feedback_parts)
    
    def _generate_role_specific_suggestions(self, role, metrics):
        """Generate role-specific improvement suggestions"""
        if role == 'software-developer':
            if metrics['technical_score'] < 0.7:
                return "Consider mentioning specific programming languages, frameworks, or development methodologies relevant to your experience."
        elif role == 'data-scientist':
            if metrics['technical_score'] < 0.7:
                return "Try to include specific ML algorithms, statistical methods, or data analysis techniques you've used."
        elif role == 'product-manager':
            if metrics['technical_score'] < 0.7:
                return "Include specific product management methodologies, tools, or frameworks you've worked with."
        
        return ""
    
    def generate_follow_up_question(self, answer, question, role, metrics):
        """Generate intelligent follow-up questions based on answer analysis"""
        follow_ups = {
            'software-developer': [
                "Can you elaborate on the specific technologies you used in that project?",
                "What challenges did you face during implementation and how did you overcome them?",
                "How did you ensure code quality and maintainability?",
                "What was the impact of your solution on the business or users?"
            ],
            'data-scientist': [
                "What specific algorithms or models did you use and why?",
                "How did you validate your results and ensure model accuracy?",
                "What was the business impact of your analysis?",
                "How did you handle data quality issues?"
            ],
            'product-manager': [
                "How did you measure the success of that feature or product?",
                "What user research methods did you use to inform your decisions?",
                "How did you handle competing stakeholder priorities?",
                "What was the go-to-market strategy for that product?"
            ]
        }
        
        # Choose follow-up based on areas that could use more detail
        if metrics['specificity_score'] < 0.6:
            return "Can you provide more specific details about that experience?"
        elif metrics['example_score'] < 0.6:
            return "Could you share a specific example to illustrate your point?"
        elif metrics['impact_score'] < 0.6:
            return "What were the measurable results or impact of your actions?"
        else:
            # Random follow-up from role-specific questions
            role_questions = follow_ups.get(role, follow_ups['software-developer'])
            return random.choice(role_questions)

class AIInterviewer:
    def __init__(self, role='general'):
        self.role = role
        self.ai_engine = AdvancedAIEngine()
        self.interview_history = []
        self.current_question_index = 0
        
        # Load questions
        self.questions = self._get_questions_for_role(role)
    
    def _get_questions_for_role(self, role):
        """Get role-specific questions with AI-generated variations"""
        base_questions = {
            'software-developer': [
                "Can you tell me about your experience with Python and how you've used it in real projects?",
                "How do you approach debugging complex issues in production systems?",
                "What's your methodology for writing clean, maintainable code that scales?",
                "How do you stay updated with the latest technologies and industry trends?",
                "Can you describe a challenging project where you had to make architectural decisions?",
                "How do you handle working in a team environment with different skill levels?",
                "What's your experience with version control systems and collaborative development?",
                "How do you approach code reviews and ensure code quality?",
                "What's your testing strategy for ensuring robust and reliable software?",
                "How do you handle tight deadlines while maintaining code quality?"
            ],
            'data-scientist': [
                "Can you explain your experience with machine learning algorithms and when you'd use each type?",
                "How do you handle missing data and outliers in your datasets?",
                "What's your approach to feature engineering and selecting the right features?",
                "How do you validate your models and prevent overfitting?",
                "Can you describe a data visualization project that provided business insights?",
                "How do you handle large-scale data processing and performance optimization?",
                "What's your experience with statistical analysis and hypothesis testing?",
                "How do you communicate technical results to non-technical stakeholders?",
                "What's your approach to A/B testing and experimental design?",
                "How do you stay current with the latest ML research and techniques?"
            ],
            'product-manager': [
                "Can you tell me about a product you successfully launched and the strategy behind it?",
                "How do you gather and prioritize user requirements from multiple stakeholders?",
                "What's your approach to competitive analysis and market positioning?",
                "How do you handle conflicts between different stakeholder priorities?",
                "Can you describe your experience with agile methodologies and sprint planning?",
                "How do you measure product success and what metrics do you track?",
                "What's your approach to user research and understanding user needs?",
                "How do you handle scope creep and changing requirements?",
                "Can you describe a time you had to pivot a product strategy?",
                "How do you balance user needs with business goals and technical constraints?"
            ],
            'general': [
                "Tell me about yourself and your professional background.",
                "What are your greatest strengths and areas for improvement?",
                "Where do you see yourself in 5 years professionally?",
                "Why are you interested in this position and company?",
                "What motivates you in your work and drives your performance?",
                "How do you handle stress and pressure in high-stakes situations?",
                "Can you describe a time you failed and what you learned from it?",
                "What's your leadership style and how do you motivate others?",
                "How do you handle criticism and feedback from others?",
                "What questions do you have for me about the role and company?"
            ]
        }
        
        return base_questions.get(role, base_questions['general'])
    
    def get_next_question(self):
        """Get the next question in the interview"""
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return {
                'question': question,
                'questionNumber': self.current_question_index,
                'totalQuestions': len(self.questions)
            }
        return None
    
    def evaluate_answer(self, answer, question):
        """Evaluate answer using advanced AI analysis"""
        # Get intelligent score and metrics
        score, metrics = self.ai_engine.generate_intelligent_score(answer, question, self.role)
        
        # Generate intelligent feedback
        feedback = self.ai_engine.generate_intelligent_feedback(answer, question, self.role, metrics)
        
        # Generate follow-up question if needed
        follow_up = self.ai_engine.generate_follow_up_question(answer, question, self.role, metrics)
        
        evaluation = {
            'question': question,
            'answer': answer,
            'score': score,
            'feedback': feedback,
            'follow_up': follow_up,
            'metrics': metrics,
            'timestamp': self._get_timestamp()
        }
        
        self.interview_history.append(evaluation)
        return evaluation
    
    def get_interview_summary(self):
        """Get comprehensive interview summary with AI insights"""
        if not self.interview_history:
            return {
                'totalQuestions': len(self.questions),
                'answeredQuestions': 0,
                'averageScore': 0,
                'overallFeedback': "No answers provided.",
                'detailedFeedback': [],
                'aiInsights': {},
                'improvementAreas': [],
                'strengths': []
            }
        
        # Calculate scores
        scores = [eval_item['score'] for eval_item in self.interview_history]
        average_score = sum(scores) / len(scores)
        
        # Generate AI insights
        ai_insights = self._generate_ai_insights()
        
        # Identify improvement areas and strengths
        improvement_areas, strengths = self._analyze_performance_patterns()
        
        return {
            'totalQuestions': len(self.questions),
            'answeredQuestions': len(self.interview_history),
            'averageScore': round(average_score),
            'overallFeedback': self._generate_overall_feedback(average_score),
            'detailedFeedback': self.interview_history,
            'aiInsights': ai_insights,
            'improvementAreas': improvement_areas,
            'strengths': strengths
        }
    
    def _generate_ai_insights(self):
        """Generate AI-powered insights about the interview performance"""
        if not self.interview_history:
            return {}
        
        # Analyze patterns across all answers
        all_metrics = [eval_item['metrics'] for eval_item in self.interview_history]
        
        insights = {
            'communication_strength': sum(m['vocabulary_score'] for m in all_metrics) / len(all_metrics),
            'technical_depth': sum(m['technical_score'] for m in all_metrics) / len(all_metrics),
            'answer_quality': sum(m['structure_score'] for m in all_metrics) / len(all_metrics),
            'concrete_examples': sum(m['example_score'] for m in all_metrics) / len(all_metrics),
            'impact_focus': sum(m['impact_score'] for m in all_metrics) / len(all_metrics)
        }
        
        # Generate insights text
        insights_text = []
        if insights['communication_strength'] > 0.7:
            insights_text.append("Strong communication skills demonstrated throughout the interview.")
        elif insights['communication_strength'] < 0.5:
            insights_text.append("Consider improving clarity and articulation in your responses.")
        
        if insights['technical_depth'] > 0.7:
            insights_text.append("Excellent technical knowledge and understanding shown.")
        elif insights['technical_depth'] < 0.5:
            insights_text.append("Focus on demonstrating deeper technical expertise in your answers.")
        
        if insights['concrete_examples'] > 0.7:
            insights_text.append("Great use of specific examples to support your points.")
        elif insights['concrete_examples'] < 0.5:
            insights_text.append("Try to include more concrete examples and specific experiences.")
        
        insights['summary'] = ' '.join(insights_text)
        
        return insights
    
    def _analyze_performance_patterns(self):
        """Analyze performance patterns to identify areas for improvement and strengths"""
        if not self.interview_history:
            return [], []
        
        all_metrics = [eval_item['metrics'] for eval_item in self.interview_history]
        
        # Calculate average scores for each metric
        avg_metrics = {}
        for key in all_metrics[0].keys():
            avg_metrics[key] = sum(m[key] for m in all_metrics) / len(all_metrics)
        
        # Identify improvement areas (scores below 0.6)
        improvement_areas = []
        if avg_metrics.get('technical_score', 0) < 0.6:
            improvement_areas.append("Technical depth and role-specific knowledge")
        if avg_metrics.get('structure_score', 0) < 0.6:
            improvement_areas.append("Answer structure and organization")
        if avg_metrics.get('specificity_score', 0) < 0.6:
            improvement_areas.append("Providing specific examples and metrics")
        if avg_metrics.get('example_score', 0) < 0.6:
            improvement_areas.append("Using concrete examples to support points")
        
        # Identify strengths (scores above 0.7)
        strengths = []
        if avg_metrics.get('vocabulary_score', 0) > 0.7:
            strengths.append("Strong vocabulary and communication skills")
        if avg_metrics.get('sentiment_score', 0) > 0.7:
            strengths.append("Positive and confident communication style")
        if avg_metrics.get('length_score', 0) > 0.7:
            strengths.append("Comprehensive and detailed responses")
        
        return improvement_areas, strengths
    
    def _generate_overall_feedback(self, average_score):
        """Generate overall feedback based on performance"""
        if average_score >= 90:
            return "Exceptional performance! You demonstrated outstanding knowledge, communication skills, and technical expertise throughout the interview."
        elif average_score >= 80:
            return "Excellent performance! You showed strong understanding and excellent communication skills with room for minor improvements."
        elif average_score >= 70:
            return "Very good performance! You have a solid foundation with good communication skills and some areas for enhancement."
        elif average_score >= 60:
            return "Good performance! You demonstrated basic competence with several areas that could benefit from improvement."
        else:
            return "Fair performance. Focus on providing more detailed answers, specific examples, and demonstrating deeper technical knowledge."
    
    def _get_timestamp(self):
        """Get current timestamp"""
        return datetime.now().isoformat()
