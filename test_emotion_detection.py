"""Unit tests for the emotion detection package."""
import unittest
from unittest.mock import patch, Mock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_joy(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01, "disgust": 0.02, "fear": 0.03,
                    "joy": 0.90, "sadness": 0.04
                }
            }]
        }
        mock_post.return_value = mock_response
        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
