import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detector_joy(self):
        """Test joy emotion detection"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detector_anger(self):
        """Test anger emotion detection"""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_detector_disgust(self):
        """Test disgust emotion detection"""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_detector_sadness(self):
        """Test sadness emotion detection"""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_emotion_detector_fear(self):
        """Test fear emotion detection"""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')
    
    def test_emotion_detector_blank_input(self):
        """Test blank input handling"""
        result = emotion_detector("")
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()