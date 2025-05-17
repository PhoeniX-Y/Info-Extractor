from flask import Flask, render_template, request, jsonify
from openai_extractor import OpenAICompanyInfoExtractor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    data = request.json
    company_text = data.get('text', '')
    if not company_text:
        return jsonify({"error": "No text provided"}), 400
    
    extractor = OpenAICompanyInfoExtractor(company_text)
    extracted_info = extractor.extract_info()
    return jsonify(extracted_info)


if __name__ == '__main__':
    app.run(debug=True)