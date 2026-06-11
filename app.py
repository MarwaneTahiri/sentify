from flask import Flask, render_template, request, redirect
from transformers import pipeline
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime
import datetime


analyzer = pipeline("sentiment-analysis")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sentify.db"

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

db.init_app(app)


class Analysis(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column()
    label: Mapped[str] = mapped_column()
    score: Mapped[float] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(), default=datetime.datetime.now())

with app.app_context():
    db.create_all()


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

    analysis = Analysis(text = text, label = label, score = score)
    db.session.add(analysis)
    db.session.commit()
    
    return render_template("result.html", score = round(score * 100, 2), label = label, text = text)

@app.route('/history')
def history():
    analyses = Analysis.query.all()
    return str([(a.text, a.label, a.score) for a in analyses])        

if __name__ == '__main__':
    app.run(debug=True)