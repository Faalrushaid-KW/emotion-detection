from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid input! Try again."

    return f"""
    For the given statement, the system response is:
    anger: {result['anger']},
    disgust: {result['disgust']},
    fear: {result['fear']},
    joy: {result['joy']},
    sadness: {result['sadness']}.
    The dominant emotion is {result['dominant_emotion']}.
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)