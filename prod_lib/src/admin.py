#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import url_for, redirect

from flask.ext.admin.contrib.sqlamodel import ModelView
from flask.ext import admin
from flask.ext import wtf, login


def formatter_authors(context, model, name):
    authors = []
    for a in model.authors:
        authors.append(a.name)
    return ", ".join(authors)


def formatter_books(context, model, name):
    books = []
    for a in model.books:
        books.append(a.title)
    return ", ".join(books)


class BooksAdminView(ModelView):
    can_create = True
    column_list = ('title', 'authors',)
    column_formatters = {
        'authors': formatter_authors,
    }
    form_args = {
        'authors': dict(validators=[wtf.Optional()]),
    }

    def __init__(self, entity, session, **kwargs):
        super(BooksAdminView, self).__init__(entity, session, **kwargs)


class AuthorsAdminView(ModelView):
    can_create = True
    column_list = ('name', 'books',)
    column_formatters = {
        'books': formatter_books,
    }
    form_args = {
        'books': dict(validators=[wtf.Optional()]),
    }

    def __init__(self, entity, session, **kwargs):
       super(AuthorsAdminView, self).__init__(entity, session, **kwargs)


class UsersAdminView(ModelView):
    can_create = True
    column_list = ('login', 'is_admin')

    def is_accessible(self):
        return login.current_user.is_authenticated() and login.current_user.is_admin

    def __init__(self, entity, session, **kwargs):
       super(UsersAdminView, self).__init__(entity, session, **kwargs)


class AdminIndexView(admin.AdminIndexView):
    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('do_login', redirect_to="admin"))

    def is_accessible(self):
        return not login.current_user.is_anonymous()
