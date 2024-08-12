from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import wave
import os
import tempfile

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

# Ensure the temporary files directory exists
TEMP_DIR = tempfile.gettempdir()

@app.route('/process', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        try:
            # Read WAV file using wave module
            with wave.open(file.stream, 'rb') as wav_file:
                frames = wav_file.readframes(wav_file.getnframes())
                channels = wav_file.getnchannels()
                rate = wav_file.getframerate()
                sample_width = wav_file.getsampwidth()
                nframes = wav_file.getnframes()
                duration = nframes / float(rate)
                
                # Placeholder for your transcript
                transcribed_text = "Processed WAV file: {} channels, {} rate, {} width, {} frames, duration {} seconds.".format(channels, rate, sample_width, nframes, duration)

        except wave.Error as e:
            return jsonify({"error": "Could not process WAV file: {}".format(str(e))}), 500

        return jsonify({
            "transcript": transcribed_text
        })

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
