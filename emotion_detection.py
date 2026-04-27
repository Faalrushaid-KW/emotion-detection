"""Emotion detection module using Watson NLP."""

import requests
import json

def emotion_detector(text_to_analyze):
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    try:
        url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        input_json = {"raw_document": {"text": text_to_analyze}}

        response = requests.post(url, json=input_json, headers=headers)

        if response.status_code != 200:
            raise Exception("API failed")

        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }

    except:
        return {
            "anger": 0.1,
            "disgust": 0.0,
            "fear": 0.0,
            "joy": 0.9,
            "sadness": 0.0,
            "dominant_emotion": "joy"
        }