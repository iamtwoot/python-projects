from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdukjfg7es7g7gh34w7i6fg'


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


@app.route('/')
def home():
    all_books = db.session.scalars(db.select(Book)).all()
    print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=int(request.form['rating']),
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = int(request.form['new_rating'])
        db.session.commit()
        flash('Rating updated successfully', 'success')
        return redirect(url_for('home'))
    else:
        book_id = request.args.get('id')
        book_selected = db.get_or_404(Book, book_id)
        return render_template('edit_rating.html', book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    flash('Book deleted successfully', 'success')
    return redirect(url_for('home'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
