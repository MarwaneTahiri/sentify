from flask import Flask, render_template, request, redirect
from transformers import pipeline

analyzer = pipeline("sentiment-analysis")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html" )

@app.route('/analyse', methods=["POST"])
def analyse():
    text = request.form.get('text')
    if text.strip() == "":
        return redirect('/')

    sentiment = analyzer(text)
    
    label = sentiment[0]['label']
    score = sentiment[0]['score']
    
    return render_template("result.html", score = round(score * 100, 2), label = label)

        

if __name__ == '__main__':
    app.run(debug=True)