import requests
import json
def emotion_detector(text_to_analyze):
    """Function to detect the emotions in text using Watson NLP"""
    if not text_to_analyze:
        return