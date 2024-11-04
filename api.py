from flask import Flask, request, jsonify
import whisper
import tempfile
import subprocess
import os

# Load Whisper model
model = whisper.load_model("base")  # Change to "small", "medium", etc. as needed

app = Flask(__name__)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(suffix=".mp4") as temp_video_file, \
         tempfile.NamedTemporaryFile(suffix=".wav") as temp_audio_file:
        
        file.save(temp_video_file.name)

        # Extract audio if it's a video file
        subprocess.run([
            "ffmpeg", "-y", "-i", temp_video_file.name, "-q:a", "0", "-map", "a", temp_audio_file.name
        ], check=True)

        # Transcribe the extracted audio
        result = model.transcribe(temp_audio_file.name)
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
