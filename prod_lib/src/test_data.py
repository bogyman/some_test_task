#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import User, Author, Book
from database import db_session


def load_test_data():
	entities = []
	entities.append(User(login="admin", password="admin", is_admin=True))
	entities.append(User(login="bbb", password="bbb"))
	entities.append(User(login="ccc", password="ccc"))

	books = []
	book1 = Book(title="book1")
	books.append(book1)
	entities.append(book1)
	book2 = Book(title="book2")
	entities.append(book2)
	book3 = Book(title="book3")
	entities.append(book3)

	entities.append(Book(title="book5"))
	entities.append(Book(title="book6"))
	entities.append(Book(title="book7"))
	entities.append(Book(title="book8"))
	entities.append(Book(title="book9"))
	entities.append(Book(title="book10"))
	entities.append(Book(title="book11"))
	entities.append(Book(title="book12"))
	entities.append(Book(title="book13"))
	entities.append(Book(title="book14"))
	entities.append(Book(title="book15"))
	entities.append(Book(title="book16"))
	entities.append(Book(title="book17"))
	entities.append(Book(title="book18"))


	entities.append(Author(name="Author1", books = books ))
	entities.append(Author(name="Author3"))
	entities.append(Author(name="Author2"))

	authors = []
	author4 = Author(name="Author4")
	authors.append(author4)
	entities.append(author4)

	author5 = Author(name="Author5")
	authors.append(author5)
	entities.append(author5)

	author6 = Author(name="Author6")
	authors.append(author6)
	entities.append(author4)

	entities.append(Book(title="Book4", authors = authors ))

	for e in entities:
		db_session.add(e)
	db_session.commit()