from flask import Flask, render_template, request
from predict import predict_sentiment
from response_links import get_negative_response_link

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

if __name__ == "__main__":
    app.run(debug=True)
