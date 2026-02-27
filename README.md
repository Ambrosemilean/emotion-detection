# emotion-detection
AI-powered Emotion Detection System using Natural Language Processing (NLP) and Machine Learning to classify human emotions from text input in real-time.


# Emotion Detection Application

This application uses IBM Watson NLP library to detect emotions in text.

## Features
- Detects five emotions: anger, disgust, fear, joy, sadness
- Identifies dominant emotion
- Web interface for easy interaction
- Error handling for invalid inputs

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python server.py`
4. Open browser: `http://localhost:5000`

## Testing
Run unit tests: `python -m unittest tests/test_emotion_detection.py`