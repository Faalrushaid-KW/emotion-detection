"""Unit tests for the emotion detection module."""

import json
import unittest
from unittest.mock import patch

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector."""

    def test_emotion_detector(self):
        """Test that emotion_detector returns formatted emotion results."""

        class MockResponse:
            """Mock response object."""
            text = json.dumps(
                {
                    "emotionPredictions": [
                        {
                            "emotion": {
                                "anger": 0.01,
                                "disgust": 0.0,
                                "fear": 0.02,
                                "joy": 0.95,
                                "sadness": 0.02,
                            }
                        }
                    ]
                }
            )

        with patch("emotion_detection.requests.post", return_value=MockResponse()):
            result = emotion_detector("I am happy today")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertAlmostEqual(result["anger"], 0.01)
        self.assertAlmostEqual(result["disgust"], 0.0)
        self.assertAlmostEqual(result["fear"], 0.02)
        self.assertAlmostEqual(result["joy"], 0.95)
        self.assertAlmostEqual(result["sadness"], 0.02)


if __name__ == "__main__":
    unittest.main()