from flask import Flask, request, jsonify
from summarize_backend import summarize_pdf, answer_question

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    pdf = request.files['pdf']
    summary = summarize_pdf(pdf)
    return jsonify({'summary': summary})

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    answer = answer_question(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

