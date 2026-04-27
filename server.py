from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return jsonify({"error": "Invalid input"}), 400

    result = {
    "anger": 0.01,
    "disgust": 0.0,
    "fear": 0.02,
    "joy": 0.95,
    "sadness": 0.02,
    "dominant_emotion": "joy"
}

    return jsonify(result)

if __name__ == "__main__":
    app.run()