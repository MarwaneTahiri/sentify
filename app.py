from flask import Flask, render_template, request
from transformers import pipeline

analyzer = pipeline("sentiment-analysis")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyse', methods=["POST"])
def analyse():
    text = request.form.get('text')
    sentiment = analyzer(text)
    return f"{sentiment}"
        

if __name__ == '__main__':
    app.run(debug=True)