"""Module docstring"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

"""Flask server for emotion detection application."""


@app.route('/emotionDetector', methods=['GET'])
def emotion_analysis():
    """Analyze emotions from the given text."""
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again."

    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Could not process the text. Please try again."

    # Extract emotions and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if not dominant_emotion:
        return "Could not detect a dominant emotion. Please try with different input."

    # Return the formatted response
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route('/')
def render_index_page():
    """Render the index webpage."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
