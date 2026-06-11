from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

# List of supported languages
LANGUAGES = {
    'auto': 'Auto Detect',
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh-CN': 'Chinese (Simplified)',
    'ar': 'Arabic',
    'hi': 'Hindi',
    'tr': 'Turkish',
    'nl': 'Dutch',
    'pl': 'Polish',
    'sv': 'Swedish',
    'da': 'Danish',
    'fi': 'Finnish',
    'no': 'Norwegian',
}

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '').strip()
    source = data.get('source', 'auto')
    target = data.get('target', 'en')

    if not text:
        return jsonify({'error': 'Please enter some text to translate.'}), 400

    if source == target and source != 'auto':
        return jsonify({'error': 'Source and target languages are the same.'}), 400

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        return jsonify({'translated_text': translated})
    except Exception as e:
        return jsonify({'error': f'Translation failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
