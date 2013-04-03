#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sqlalchemy as db
from werkzeug.security import generate_password_hash

from database import Base

authors_books = db.Table(
    'authors_books',
    Base.metadata,
    db.Column('i_author', db.Integer, db.ForeignKey('authors.id')),
    db.Column('i_book', db.Integer, db.ForeignKey('books.id'))
)


class Book(Base):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    authors = db.orm.relationship('Author',
                                  secondary="authors_books",
                                  )

    def __init__(self, title="", authors=None):
        self.title = title
        if authors:
            self.authors = authors

    def __repr__(self):
        return self.title


class Author(Base):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    books = db.orm.relationship('Book',
                                secondary="authors_books",
                                )

    def __init__(self, name="", books=None):
        self.name = name
        if books:
            self.books = books

    def __repr__(self):
        return self.name


class User(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), )
    password = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean)
    is_authorized = db.Column(db.Boolean)

    def __init__(self, login="", password="", is_admin=False, is_authorized=False):
        self.is_admin = is_admin
        self.is_authorized = is_authorized
        self.login = login
        self.password = generate_password_hash(password)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
