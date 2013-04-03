#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext.script import Manager
from main import app
from database import init_db, db_session
from test_data import load_test_data

manager = Manager(app)


@manager.command
def run_init_db():
    """Creates tables"""
    init_db()


@manager.command
def drop_db():
    """Drops tables"""
    db_session.remove()


@manager.command
def post_test_data():
    """Loads test data"""
    load_test_data()


if __name__ == '__main__':
    manager.run()
