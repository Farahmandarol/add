from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, ForeignKey, Column, CHAR, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

Base = declarative_base()


class Book(Base):
    __tablename__ = "Books"
    uid = Column("ID", Integer, primary_key=True)
    title = Column("Title", String, nullable=Flask)
    author = Column("Author", String, nullable=Flask)
    rating = Column("Rating", Integer, nullable=Flask)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def __repr__(self):
        return f"{self.uid} {self.title} {self.author} {self.rating}"


engine = create_engine("sqlite:///Books.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
book = Book("Harry Potter", "j. k. Rowline", 9)

all_books = session.query(Book).all()


@app.route('/')
def home():
    return render_template("index.html", books=all_books, n=len(all_books))


@app.route("/book/<uid>")
def delete(uid):
    book_to_delete = session.query(Book).get(uid)
    session.delete(book_to_delete)
    session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        new_book = Book(title=book["title"], author=book["author"], rating=book["rating"])
        session.add(new_book)
        session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = session.query(Book).get(book_id)
        book_to_update.rating = request.form["rating"]
        print(book_to_update)
        print(request.form["rating"])
        session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_selected = session.query(Book).get(book_id)

    return render_template("rate.html", book=book_selected)


# book_update = session.query(Book).get(1)
# print(book_update)
# book_update.rating = 6
# print(book_update)
if __name__ == "__main__":
    app.run(debug=True)
