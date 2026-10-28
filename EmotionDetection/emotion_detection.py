"""Emotion detection using the Watson NLP service."""
import requests


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the dominant emotion."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow"
    }

    try:
        response = requests.post(
            url,
            json={"raw_document": {"text": text_to_analyze}},
            headers=headers,
            timeout=30,
        )
        if response.status_code == 400:
            return {
                "anger": None, "disgust": None, "fear": None,
                "joy": None, "sadness": None, "dominant_emotion": None,
            }

        response.raise_for_status()
        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]
        dominant = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant,
        }
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return {
            "anger": None, "disgust": None, "fear": None,
            "joy": None, "sadness": None, "dominant_emotion": None,
        }
