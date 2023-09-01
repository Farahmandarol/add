from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from sqlalchemy import create_engine, String, Integer, Column, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# constant
movie_api = "0a7df81d1b945ca49717dafda58d2f96"
movie_api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYTdkZjgxZDFiOTQ1Y2E0OTcxN2RhZmRhNThkMmY5NiIsInN1YiI6IjY0ZjFiOGExOTdhNGU2MDEzODk2NGY5NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gBC3VUh2bgGZsrzk8hpeRWLU7VxOZLOA-wwI8rrIOpE"
url = "https://api.themoviedb.org/3/search/movie?"
movies = None
# Database
Base = declarative_base()


class Movie(Base):
    __tablename__ = "Movies"
    id = Column("ID", Integer, primary_key=True)
    title = Column("Title", String)
    year = Column("Year", Integer)
    description = Column("Description", String)
    rating = Column("Raring", Float)
    ranking = Column("Ranking", Integer)
    review = Column("Review", String)
    img_url = Column("URL", String)

    def __init__(self, title, year, description, rating, ranking, review, img_url):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url

    def __repr__(self):
        return f"{self.title} {self.year} {self.description} {self.rating} {self.ranking} {self.review} {self.img_url}"


engine = create_engine("sqlite:///Movie.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
new_movie = Movie(
    title="Phone Booth",
    year=2012,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=5.3,
    ranking=1,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)


# session.add(new_movie)
# session.commit()
# create form to edit rating and review

class RateMovieForm(FlaskForm):
    rate = FloatField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovie(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("ADD")


all_movies = session.query(Movie).all()


@app.route("/")
def home():
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["POST", "GET"])
def add():
    global movies
    add_form = AddMovie()
    if add_form.validate_on_submit():
        data = requests.get(url=url, params={"api_key": movie_api, "query": add_form.title.data})
        allMoviesInSearch = data.json()["results"]
        movies = allMoviesInSearch
        return redirect(url_for("select"))
    return render_template("add.html", form=add_form)


@app.route("/edit", methods=["POST", "GET"])
def rate_movie():
    edit_form = RateMovieForm()
    movie_id = request.args.get("id")
    movie_selected = session.query(Movie).get(movie_id)
    print(movie_id, movie_selected)
    if edit_form.validate_on_submit():
        movie_selected.rating = float(edit_form.rate.data)
        movie_selected.review = edit_form.review.data
        session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form, movie=movie_selected)


@app.route("/select")
def select():
    return render_template("select.html", movies=movies)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = session.query(Movie).get(movie_id)
    session.delete(movie_to_delete)
    session.commit()
    return redirect(url_for("home"))


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    print(movie_api_id)
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": movie_api, "language": "en-US"})
        data = response.json()
        print(data)
        to_add_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"https://api.themoviedb.org/3/movie/{movie_api_id}/images?api_key=0a7df81d1b945ca49717dafda58d2f96",
            description=data["overview"],
            ranking=data["popularity"],
            rating=float(data["popularity"]),
            review="Custome Review"
        )
        print(to_add_movie)
        session.add(to_add_movie)
        session.commit()
    return redirect(url_for("home"))


response = requests.get("https://api.themoviedb.org/3/movie/603/images",
                        params={"api_key": movie_api, "language": "en-US"})
print(response.json())

if __name__ == '__main__':
    app.run(debug=True)
