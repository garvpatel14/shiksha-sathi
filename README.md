# Shiksha Sathi – Just-in-Time Teaching Assistant

Shiksha Sathi is an AI-powered classroom assistant that provides real-time, need-based teaching and classroom management support to teachers.

## Problem
Teachers often face classroom challenges during live instruction but receive delayed and generic support through periodic mentoring visits.

## Solution
Teachers describe the classroom problem they are facing, and Shiksha Sathi instantly provides:
- Classroom management strategies
- Pedagogical hooks using local materials
- Activities to engage advanced students

The solution is designed to work offline and in low-connectivity rural environments.

## Tech Stack
- Python
- Flask
- Ollama (Local AI – llama3:8b)
- HTML, JavaScript

## How to Run
1. Install Ollama and run: `ollama run llama3:8b`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Open browser: `http://127.0.0.1:5000/ui`

## Future Enhancements
- Voice-based input
- Multilingual support
- Mobile-friendly interface
