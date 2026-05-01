from flask import Flask, render_template, request
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/029e2aed2baa7ed9f2cc").json()


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
        print(username, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
