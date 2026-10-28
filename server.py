"""Flask web server for emotion detection."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Display the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Analyze input text and display the emotion results."""
    text_to_analyze = (
        request.values.get("textToAnalyze", "").strip()
    )
    if not text_to_analyze:
        return "Invalid text! Please enter a sentence.", 400

    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Unable to analyze the text. Please try again.", 502

    return (
        f"For the given statement, the dominant emotion is "
        f"{result['dominant_emotion']}. "
        f"Scores: anger={result['anger']}, "
        f"disgust={result['disgust']}, fear={result['fear']}, "
        f"joy={result['joy']}, sadness={result['sadness']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
