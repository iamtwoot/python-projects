import os
import smtplib
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_APP_PASSWORD")
posts = requests.get("https://api.npoint.io/029e2aed2baa7ed9f2cc").json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        username = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject: New Message\n\n"
                    f"Name: {username}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n"
                    f"Message: {message}",
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
