from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Set your AIPROXY_TOKEN here or retrieve it from environment variables
AIPROXY_TOKEN = os.getenv("eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjEwMDA1MzlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.5jidN468Jut3abJKoOkkGi7bxxkoCfWXC1R58iQpIFM")  # Set this in your environment

@app.route('/')
def home():
    return "Welcome to the AI Proxy API!"

@app.route('/api/', methods=['POST'])
def answer_question():
    question = request.form.get('question')
    file = request.files.get('file')

    if file:
        # Handle file processing if needed
        return jsonify({"error": "File uploads are not supported in this version."}), 400

    # Prepare the request to the AI Proxy
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AIPROXY_TOKEN}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": question}]
    }

    # Send the request to the AI Proxy
    response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to get response from AI Proxy", "details": response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
