from flask import Flask, render_template, request
from predict import predict_sentiment
from response_links import get_negative_response_link
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    link = ""
    if request.method == "POST":
        text = request.form["text"]
        result = predict_sentiment(text)
        if result == 0:
            message = "🙁 That sounds negative."
            link = get_negative_response_link()
        else:
            message = "😊 That sounds positive!"
    return render_template("index.html", message=message, link=link)

# 👇 Add this block at the bottom
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Render-assigned port
    app.run(host="0.0.0.0", port=port)
