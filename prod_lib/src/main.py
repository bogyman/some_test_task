#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sqlalchemy import or_
from werkzeug.security import check_password_hash
from flask import Flask, request, render_template, flash, url_for, redirect
from flask.ext import login
from flask.ext.admin import Admin
from flask.ext.sqlalchemy import Pagination

from forms import LoginForm, BookSearchForm, RegistrationForm
from admin import BooksAdminView, AuthorsAdminView, UsersAdminView, AdminIndexView
from models import User, Author, Book


from database import db_session

app = Flask(__name__)
app.config.from_pyfile('settings.py')

admin = Admin(app, "The LibRARy", index_view=AdminIndexView(template="admin/index.html"))
admin.add_view(BooksAdminView(Book, db_session))
admin.add_view(AuthorsAdminView(Author, db_session))
admin.add_view(UsersAdminView(User, db_session))


@app.route('/')
def index():
    return render_template('index.html', form=BookSearchForm())


@app.route('/books/', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/books/page/<int:page>', methods=['GET', 'POST'],)
@login.login_required
def list_books(page):
    if login.current_user.is_authorized:
        per_page = 15
        form = BookSearchForm()
        books_query = None
        if request.method == 'POST' and form.q.data and form.validate_on_submit():
            books_query = Book.query.filter(
                                            or_(
                                                Book.authors.any(
                                                    Author.name.like("%{0}%".format(form.q.data))
                                                    ),
                                                Book.title.like("%{0}%".format(form.q.data))
                                                )
                                            )
        else:
            books_query = Book.query
        items = books_query.limit(per_page).offset((page - 1) * per_page).all()
        books = Pagination(books_query, page, per_page, books_query.count(), items)
        return render_template('books.html', books=books, form=form)
    else:
        return redirect(url_for("index"))


@app.route('/registration/', methods=["GET", "POST"])
def registration():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User(form.login.data, form.password.data)
        db_session.add(user)
        db_session.commit()
        flash('Thanks for registering')
        login.login_user(user)
        flash("Logged in successfully.")
        return redirect(url_for("index"))
    return render_template('registration.html', form=form)


@app.route("/login/<redirect_to>", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def do_login(redirect_to=""):
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login.login_user(user)
            flash("Logged in successfully.")
            if redirect_to:
                return redirect(redirect_to)
            return redirect(url_for("index"))
        else:
            flash("bad login info")
    return render_template("login.html", form=form)


@app.route("/logout")
@login.login_required
def do_logout():
    login.logout_user()
    return redirect(url_for("index"))


# Initialize flask-login
login_manager = login.LoginManager()
login_manager.setup_app(app)


# Create user loader function
@login_manager.user_loader
def load_user(user_id):
    return db_session.query(User).get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    flash("Please log in first.")
    return redirect(url_for("index"))

def is_logined():
    if not login.current_user.is_anonymous():
        return login.current_user.is_authenticated()
    return False

def is_authorized():
    if not login.current_user.is_anonymous():
        return login.current_user.is_authorized
    return False    

app.jinja_env.globals.update(is_logined=is_logined)
app.jinja_env.globals.update(is_authorized=is_authorized)