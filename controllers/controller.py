from flask import render_template, request, redirect
from app import app
from models.book_list import *
from models.book import *


@app.route("/books")
def index():
    return render_template("index.html", books=books)


@app.route("/books/<int:index>")
def show_details(index):
    book = books[index]
    return render_template("book_details.html", book=books[index])


@app.route("/books", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    checked_out = True if "checking" in request.form else False
    newbook = Book(title=title, author=author, genre=genre, checked_out=checked_out)
    add_new_book(newbook)
    return redirect("/books")


@app.route("/books/del/<index>", methods=["POST"])
def delete_by_index(index):
    delete_book_by_index(int(index))
    return redirect("/books")
