import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWFlYWk5MTI0ZTVuY25zdHpta2I1djNyN3Vya2w4NWcweWkyNjk0MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZqlvCTNHpqrio/giphy.gif'' width=300>")

@app.route("/<int:guess>")
def check_number(guess):
    if guess < number:
        return "<h1>Too low</h1>"
    elif guess > number:
        return "<h1>Too high</h1>"
    else:
        return "<h1>Correct!</h1>"

number = random.randint(0,9)

if __name__ == '__main__':
    app.run(debug=True)