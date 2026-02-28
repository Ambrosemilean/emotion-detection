import requests
import json
def emotion_detector(text_to_analyze):
    """Function to detect the emotions in text using Watson NLP"""
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        url = 'https://sn-watson-emotion.Lab.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers ={"grpc-metadata-mm-model-id"}
        if response.status_code == 200