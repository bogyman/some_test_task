#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext import wtf
from flask.ext.wtf import validators
from models import User


class LoginForm(wtf.Form):
    login = wtf.StringField('Login', validators=[validators.Required()])
    password = wtf.PasswordField('Password', validators=[validators.Required()])


class RegistrationForm(wtf.Form):
    login = wtf.StringField('Login', validators=[validators.Required()])
    password = wtf.PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = wtf.PasswordField('Repeat Password', validators=[validators.Required()])

    def validate_login(self, field):
        user = User.query.filter_by(login=field.data).first()
        if user is not None:
            raise wtf.ValidationError("User with the same login is already exists")


class BookSearchForm(wtf.Form):
    q = wtf.StringField(' or ', validators=[validators.Required()])
