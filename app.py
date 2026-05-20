from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyse', methods=["POST"])
def analyse():
    text = request.form.get('text')
    return f"you returned {text}"
        

if __name__ == '__main__':
    app.run(debug=True)