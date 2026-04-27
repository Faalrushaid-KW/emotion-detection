from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@@app.route("/emotionDetector")
def emotion_detector_route():
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return {"error": "Invalid input"}

    return result

if __name__ == "__main__":
    app.run()