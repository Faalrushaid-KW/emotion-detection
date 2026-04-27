"""Flask server for the emotion detection application."""

from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """Handle emotion detection requests from query parameters."""
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return {"error": "Invalid input"}

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)