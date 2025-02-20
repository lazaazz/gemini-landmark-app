from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from tts_engine import generate_audio
from image_recognition import identify_monument
import os

app = Flask(__name__)

# Set up Gemini API
GEMINI_API_KEY = "your_gemini_api_key_here"  # 🔹 Replace with your API Key
genai.configure(api_key=GEMINI_API_KEY)

# Folder paths
AUDIO_DIR = "static/audio/"
VIDEO_DIR = "static/videos/"

# List of supported monuments
MONUMENTS = {
    "taj_mahal": {"text": "I am the Taj Mahal, built by Emperor Shah Jahan in 1632.", "video": "taj_mahal.mp4"},
    "eiffel_tower": {"text": "I am the Eiffel Tower, a symbol of France built in 1889.", "video": "eiffel_tower.mp4"},
    "statue_of_liberty": {"text": "I am the Statue of Liberty, a gift from France in 1886.", "video": "statue_of_liberty.mp4"}
}

# Supported languages
LANGUAGES = {"english": "english", "hindi": "hindi", "telugu": "telugu"}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    monument = request.json.get("monument", "unknown")
    language = request.json.get("language", "english")

    if monument not in MONUMENTS:
        return jsonify({"error": "Monument not found"}), 404

    # Generate AI response
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"You are {monument}. Answer in first person. User asks: {user_input}")
    story_text = response.text

    # Generate voice narration
    audio_path = generate_audio(story_text, language, f"{monument}_{language}")

    return jsonify({
        "response": story_text,
        "audio_url": audio_path,
        "video_url": f"/static/videos/{MONUMENTS[monument]['video']}"
    })

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/identify", methods=["POST"])
def identify():
    """Receives an image and returns the identified monument."""
    image = request.files["image"]
    monument = identify_monument(image)

    if monument in MONUMENTS:
        return jsonify({
            "monument": monument,
            "description": MONUMENTS[monument]["text"],
            "video_url": f"/static/videos/{MONUMENTS[monument]['video']}"
        })
    else:
        return jsonify({
            "monument": "unknown",
            "description": "Monument not recognized."
        })
