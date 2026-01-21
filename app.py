from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# FAST local model
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:8b"   # much faster than llama3

@app.route("/")
def home():
    return "Shiksha Sathi AI running (fast mode)"

@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/get-advice", methods=["POST"])
def get_advice():
    data = request.get_json(force=True)
    problem = data.get("problem", "").strip()

    if not problem:
        return jsonify({"advice": "Please enter a classroom problem."})

    # VERY SHORT PROMPT = FAST RESPONSE
    prompt = f"""
You are a teaching assistant for Indian classrooms.

If input is a simple question, give a short child-friendly answer.
If it is a classroom problem, give:
1. Management steps
2. Teaching hook
3. Advanced task

Input:
{problem}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=40
    )

    return jsonify({
        "advice": response.json().get("response", "")
    })


if __name__ == "__main__":
    print("Starting Shiksha Sathi AI (FAST MODE)...")
    app.run(host="127.0.0.1", port=5000, debug=False)
