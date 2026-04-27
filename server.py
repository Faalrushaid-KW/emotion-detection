from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return jsonify({"error": "Invalid input"}), 400

    result = emotion_detector(text_to_analyze)

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)