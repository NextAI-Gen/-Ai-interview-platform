#!/usr/bin/env python3
"""
AI Interview Platform Demo Script
Demonstrates the key features of the AI Interview system
"""

import json
from ai_engine import AdvancedAIEngine

def demo_ai_engine():
    """Demonstrate the AI Engine capabilities"""
    print("🧠 AI Interview Platform Demo")
    print("=" * 50)
    
    # Initialize AI Engine
    ai_engine = AdvancedAIEngine()
    
    # Demo 1: Software Developer Interview
    print("\n🎯 Demo 1: Software Developer Interview")
    print("-" * 40)
    
    question = "Explain the concept of Object-Oriented Programming"
    answer = "Object-Oriented Programming is a programming paradigm that organizes code into objects that contain data and code. It's based on four main principles: encapsulation, inheritance, polymorphism, and abstraction. For example, in Python, we create classes that serve as blueprints for objects. This approach makes code more modular, reusable, and easier to maintain."
    
    print(f"Question: {question}")
    print(f"Answer: {answer}")
    
    # Analyze the answer
    metrics = ai_engine.analyze_answer_sophistication(answer, question, 'software-developer')
    print("\n📊 AI Analysis Results:")
    for metric, score in metrics.items():
        print(f"  {metric.replace('_', ' ').title()}: {score:.2f}")
    
    # Demo 2: Data Scientist Interview
    print("\n🎯 Demo 2: Data Scientist Interview")
    print("-" * 40)
    
    question = "What is Machine Learning and how does it work?"
    answer = "Machine Learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed. It works by training algorithms on large datasets to identify patterns and make predictions. For instance, in supervised learning, we provide labeled training data to teach the model to recognize relationships between inputs and outputs. Common algorithms include linear regression, decision trees, and neural networks."
    
    print(f"Question: {question}")
    print(f"Answer: {answer}")
    
    # Analyze the answer
    metrics = ai_engine.analyze_answer_sophistication(answer, question, 'data-scientist')
    print("\n📊 AI Analysis Results:")
    for metric, score in metrics.items():
        print(f"  {metric.replace('_', ' ').title()}: {score:.2f}")
    
    # Demo 3: Product Manager Interview
    print("\n🎯 Demo 3: Product Manager Interview")
    print("-" * 40)
    
    question = "How do you prioritize features in a product roadmap?"
    answer = "Feature prioritization involves evaluating features based on business value, user impact, and technical feasibility. I use frameworks like RICE (Reach, Impact, Confidence, Effort) or MoSCoW (Must-have, Should-have, Could-have, Won't-have) to score features. For example, a feature that affects 80% of users and has high business impact would get priority over a nice-to-have feature with low user reach. I also consider market timing, competitive landscape, and resource constraints."
    
    print(f"Question: {question}")
    print(f"Answer: {answer}")
    
    # Analyze the answer
    metrics = ai_engine.analyze_answer_sophistication(answer, question, 'product-manager')
    print("\n📊 AI Analysis Results:")
    for metric, score in metrics.items():
        print(f"  {metric.replace('_', ' ').title()}: {score:.2f}")
    
    print("\n" + "=" * 50)
    print("🎉 Demo completed! This showcases the AI Engine's ability to:")
    print("  • Analyze answer sophistication across multiple dimensions")
    print("  • Provide role-specific technical relevance scoring")
    print("  • Generate comprehensive feedback for improvement")
    print("  • Support multiple interview roles and question types")

def demo_knowledge_base():
    """Show the knowledge base structure"""
    print("\n📚 Knowledge Base Structure")
    print("=" * 50)
    
    ai_engine = AdvancedAIEngine()
    
    for role, data in ai_engine.knowledge_base.items():
        print(f"\n🎯 {role.replace('-', ' ').title()}:")
        print(f"  Concepts: {len(data['concepts'])} key concepts")
        print(f"  Technologies: {len(data['technologies'])} technologies")
        print(f"  Skills: {len(data['skills'])} core skills")
        
        # Show some examples
        print(f"  Sample concepts: {', '.join(data['concepts'][:3])}...")
        print(f"  Sample technologies: {', '.join(data['technologies'][:3])}...")

if __name__ == "__main__":
    try:
        demo_ai_engine()
        demo_knowledge_base()
    except Exception as e:
        print(f"❌ Error running demo: {e}")
        print("Make sure all dependencies are installed and the AI engine is working properly.")
