from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, URL, Float, create_engine, desc,asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, URLField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# --------------------- Flask Forms -------------------------#
class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    rating = FloatField("Rating", validators=[DataRequired()])
    ranking = IntegerField("Ranking", validators=[DataRequired()])
    review = StringField("Rreview", validators=[DataRequired()])
    img_url = URLField("Imag URL", validators=[DataRequired()])
    add = SubmitField("ADD")


class Update(FlaskForm):
    rate = FloatField("Rating", validators=[DataRequired()])
    review = StringField("Overview", validators=[DataRequired()])
    update = SubmitField("Update")


# ---------------------- Databases --------------------------#
Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    ranking = Column(Integer, nullable=False)
    review = Column(Integer, nullable=False)
    img_url = Column(String, nullable=False)

    def __init__(self, title, year, description, rating, ranking, review, img_url):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url

    def __repr__(self):
        return f"{self.title} {self.year} {self.description} {self.rating} {self.img_url}"


engin = create_engine("sqlite:///movies.db", echo=True)
Base.metadata.create_all(bind=engin)
Session = sessionmaker(bind=engin)
session = Session()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )


# session.add(new_movie)
# session.commit()

# ---------------------- Routes -----------------------------#
@app.route("/")
def home():
    movies = session.query(Movie).order_by(asc("ranking")).all()

    return render_template("index.html", movies=movies)


@app.route("/update", methods=["POST", "GET"])
def update():
    form = Update()
    movie_id = request.args.get("id")
    edit_movie = session.query(Movie).get(movie_id)
    if form.validate_on_submit():
        edit_movie.rating = form.rate.data
        edit_movie.review = form.review.data
        session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=edit_movie)


@app.route("/add", methods=["POST", "GET"])
def add():
    movie_form = MovieForm()
    if movie_form.validate_on_submit():
        new_movie = Movie(
            title=movie_form.title.data,
            year=movie_form.year.data,
            description=movie_form.description.data,
            rating=movie_form.rating.data,
            ranking=movie_form.ranking.data,
            review=movie_form.review.data,
            img_url=movie_form.img_url.data
        )
        session.add(new_movie)
        session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=movie_form)


@app.route("/delete", methods=["POST", "GET"])
def delete():
    delete_id = request.args.get("id")
    if delete_id:
        delete_movie = session.query(Movie).get(delete_id)
        session.delete(delete_movie)
        session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
