from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(posts_url).json()
    return render_template("index.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
