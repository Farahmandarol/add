from flask import Flask, render_template
import requests

blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_api)
data = response.json()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", blogs=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<num>")
def get_blog(num):
    for blog in data:
        if int(blog["id"]) == int(num):
            return render_template("post.html", post=blog, image_url=f"{num}.jpg")


if __name__ == "__main__":
    app.run(debug=True)
