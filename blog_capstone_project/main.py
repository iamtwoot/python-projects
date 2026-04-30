from flask import Flask, render_template
import requests

app = Flask(__name__)

posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(posts_url).json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    post = all_posts[post_id]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
