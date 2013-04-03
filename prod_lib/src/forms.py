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

    # def validate(self):
    #     if self.login is None:
    #         self.login.errors = ('Login field is required',)
    #         return False

    #     if self.password is None:
    #         self.password.errors = ('Password field is required',)
    #         return False

    #     user = User.query.filter_by(login=self.login.data).first()
    #     if user is not None:
    #         self.login.errors = ('User with the same login is already exists',)
    #         return False

    #     return True


class BookSearchForm(wtf.Form):
    q = wtf.StringField(' or ', validators=[validators.Required()])
