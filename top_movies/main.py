import os
from flask import Flask, render_template, redirect, url_for, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv

load_dotenv()

MOVIE_API_KEY = os.getenv("MOVIE_API_KEY")
if MOVIE_API_KEY is None:
    raise ValueError("MOVIE_API_KEY environment variable not set")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    __tablename__ = 'movie'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tmdb_id: Mapped[int] = mapped_column(Integer, unique=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# CREATE FORM
class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10')
    review = StringField('Your Review', validators=[DataRequired()])


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])


def get_movies(title):
    url = f"https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {MOVIE_API_KEY}"
    }
    params = {
        "query": title,
        "page": 1,
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    movies = data["results"]
    return movies


def get_movie_details(tmdb_id):
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {MOVIE_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


def add_movie(movie):
    new_movie = Movie(
        tmdb_id=movie['tmdb_id'],
        title=movie["title"],
        year=int(movie["release_date"].split("-")[0]),
        description=movie["overview"],
        rating=round(movie["vote_average"], 2),
        img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
    )
    db.session.add(new_movie)
    db.session.commit()
    return new_movie


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars().all()

    for movie in all_movies:
        movie.ranking = all_movies.index(movie) + 1

    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()

    if form.validate_on_submit():
        movie_id = request.args.get('id')

        if movie_id is None:
            abort(400)

        movie_to_update = db.get_or_404(Movie, int(movie_id))

        if form.rating.data:
            movie_to_update.rating = float(form.rating.data)

        if form.review.data:
            movie_to_update.review = form.review.data

        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    if movie_id is None:
        abort(400)
    movie_to_delete = db.get_or_404(Movie, int(movie_id))
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        movies = get_movies(title)
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)


@app.route("/select")
def select():
    tmdb_id = request.args.get('tmdb_id', type=int)
    movie_details = get_movie_details(tmdb_id)
    movie_details['tmdb_id'] = tmdb_id
    new_movie = add_movie(movie_details)
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
