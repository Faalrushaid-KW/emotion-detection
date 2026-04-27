import unittest
from unittest.mock import patch
import json
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):

        class MockResponse:
            text = json.dumps({
                "emotionPredictions": [
                    {
                        "emotion": {
                            "anger": 0.01,
                            "disgust": 0.0,
                            "fear": 0.02,
                            "joy": 0.95,
                            "sadness": 0.02
                        }
                    }
                ]
            })

        with patch('emotion_detection.requests.post', return_value=MockResponse()):
            result = emotion_detector("I am happy today")

            self.assertEqual(result["dominant_emotion"], "joy")
            self.assertAlmostEqual(result["anger"], 0.01)
            self.assertAlmostEqual(result["disgust"], 0.0)
            self.assertAlmostEqual(result["fear"], 0.02)
            self.assertAlmostEqual(result["joy"], 0.95)
            self.assertAlmostEqual(result["sadness"], 0.02)

if __name__ == "__main__":
    unittest.main()