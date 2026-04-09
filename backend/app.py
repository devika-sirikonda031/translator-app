from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

app = Flask(__name__)
CORS(app)

if not os.path.exists("static"):
    os.makedirs("static")

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text', '')
        lang = data.get('lang', 'en')  # 👈 new

        result = GoogleTranslator(source='auto', target=lang).translate(text)

        audio_path = "static/audio.mp3"
        voice = gTTS(text=result, lang=lang)
        voice.save(audio_path)

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🔥 Flask Running...")
    app.run(debug=True)