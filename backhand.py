from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Set your Gemini API key here
genai.configure(api_key="AIzaSyCxAzkmAV8mOv2-T563Z4xwAVyriMfxDB8")

@app.route("/simplify-law", methods=["POST"])
def simplify_law():
    data = request.get_json()
    text = data.get("text")
    law_type = data.get("lawType", "general")

    if not text:
        return jpytsonify({"error": "Missing legal text"}), 400

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"Simplify the following legal text related to {law_type} law into plain language:\n\n\"{text}\""

        response = model.generate_content(prompt)
        simplified = response.text.strip()

        return jsonify({"simplified": simplified})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Failed to simplify the text"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=3000)
