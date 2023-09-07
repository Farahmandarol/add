from flask import Flask, render_template, request
import requests
import smtplib
from flask import Flask, render_template, redirect, url_for
from sqlalchemy import Column, Integer, Text, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime, date

blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
email = "haniarol94@gmail.com"
password = "Farahmand@90"
response = requests.get(url=blog_api)
data = response.json()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])

    # Notice body's StringField changed to CKEditorField
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# CONFIGURE TABLE
Base = declarative_base()


class BlogPost(Base):
    __tablename__ = "blog_post"
    id = Column(Integer, primary_key=True)
    title = Column(String(250), unique=True, nullable=False)
    subtitle = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    body = Column(Text, nullable=False)
    author = Column(String(250), nullable=False)
    img_url = Column(String(250), nullable=False)

    def __init__(self, title, subtitle, date, body, author, img_url):
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.body = body
        self.author = author
        self.img_url = img_url

    def __repr__(self):
        return f"{self.id}  {self.title} {self.subtitle} {self.date} {self.body} {self.author} {self.img_url}"


engin = create_engine("sqlite:///posts.db", echo=True)
Base.metadata.create_all(bind=engin)
Session = sessionmaker(bind=engin)
session = Session()


@app.route("/")
def hello_world():
    blog_data = []
    all_blogs = session.query(BlogPost).all()
    for blog in all_blogs:
        blog_data.append(blog)
    return render_template("index.html", blogs=blog_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=request.form['email'],
                                msg=f"Name: {request.form['name']}\nPhone: {request.form['phone']} Message: {request.form['msg']}")
            return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")


@app.route("/post/<num>")
def get_blog(num):
    all_blogs = session.query(BlogPost).all()
    for blog in all_blogs:
        if blog.id == int(num):
            return render_template("post.html", post=blog, image_url=f"{num}.jpg")


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y"),
            body=form.body.data,
            img_url=form.img_url.data
        )
        session.add(new_post)
        session.commit()
        return redirect(url_for("hello_world"))
    return render_template("add_post.html", form=form)


@app.route("/edit", methods=["POST", 'GET'])
def edit():
    pos_id = request.args.get("id")
    post = session.query(BlogPost).get(pos_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        session.commit()
        return redirect(url_for("hello_world"))

    return render_template("edit.html", post=post, form=edit_form)


@app.route("/delete")
def delete():
    delete_id = request.args.get("id")
    to_delete_post = session.query(BlogPost).get(delete_id)
    print(delete_id)
    session.delete(to_delete_post)
    session.commit()
    return redirect(url_for("hello_world"))


if __name__ == "__main__":
    app.run(debug=True)
