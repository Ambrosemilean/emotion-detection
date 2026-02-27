"""
Flask server for emotion detection application
"""
from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Handle emotion detection requests"""
    text_to_analyze = request.form.get('text', '')
    
    if not text_to_analyze:
        return "Invalid text! Please try again."
    
    result = emotion_detector(text_to_analyze)
    
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    
    return response_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)