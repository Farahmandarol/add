from flask import Flask, render_template, request
import requests
import smtplib

blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
email = "haniarol94@gmail.com"
password = "Farahmand@90"
response = requests.get(url=blog_api)
data = response.json()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", blogs=data)


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
    for blog in data:
        if int(blog["id"]) == int(num):
            return render_template("post.html", post=blog, image_url=f"{num}.jpg")


if __name__ == "__main__":
    app.run(debug=True)
