#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import User, Author, Book
from database import db_session


def load_test_data():
    entities = []
    entities.append(User(login="admin", password="admin", is_admin=True, is_authorized=True))
    entities.append(User(login="bbb", password="bbb"))
    entities.append(User(login="ccc", password="ccc"))

    books = []
    authors = []

    

















































































    books.append(Book(title="Мастер и Маргарита"))
    books.append(Book(title="Преступление и наказание"))
    books.append(Book(title="Евгений Онегин"))
    books.append(Book(title="Приключения Шерлока Холмса"))
    books.append(Book(title="Собачье сердце"))
    books.append(Book(title="Двенадцать стульев"))
    books.append(Book(title="Война и мир"))
    books.append(Book(title="Герой нашего времени"))
    books.append(Book(title="Маленький принц"))
    books.append(Book(title="Граф Монте-Кристо"))
    books.append(Book(title="Рассказы"))
    books.append(Book(title="Три товарища"))
    books.append(Book(title="Портрет Дориана Грея"))
    books.append(Book(title="Идиот"))
    books.append(Book(title="Горе от ума"))
    books.append(Book(title="Унесённые ветром"))
    books.append(Book(title="Мёртвые души"))
    books.append(Book(title="Ромео и Джульетта"))
    books.append(Book(title="Анна Каренина"))
    books.append(Book(title="Вечера на хуторе близ Диканьки"))
    books.append(Book(title="Рассказы"))
    books.append(Book(title="Братья Карамазовы"))
    books.append(Book(title="Три мушкетера"))
    books.append(Book(title="Тихий Дон"))
    books.append(Book(title="Гордость и предубеждение"))
    books.append(Book(title="Приключения Тома Сойера"))
    books.append(Book(title="Капитанская дочка"))
    books.append(Book(title="Золотой теленок"))
    books.append(Book(title="Робинзон Крузо"))
    books.append(Book(title="Фауст"))
    books.append(Book(title="Отцы и дети"))
    books.append(Book(title="Собака Баскервилей"))
    books.append(Book(title="А зори здесь тихие"))
    books.append(Book(title="Тарас Бульба"))
    books.append(Book(title="Мартин Иден"))
    books.append(Book(title="Повести Белкина"))
    books.append(Book(title="Винни-Пух"))
    books.append(Book(title="Пикник на обочине"))
    books.append(Book(title="Похождения бравого солдата Швейка во время мировой войны"))
    books.append(Book(title="Отверженные"))
    books.append(Book(title="Человек-амфибия"))
    books.append(Book(title="Приключения Эраста Фандорина"))
    books.append(Book(title="Солярис"))
    books.append(Book(title="Парфюмер История одного убийцы"))
    books.append(Book(title="Пётр Первый"))
    books.append(Book(title="Сказка о рыбаке и рыбке"))
    books.append(Book(title="Грозовой перевал"))
    books.append(Book(title="Поющие в терновнике"))
    books.append(Book(title="Трудно быть богом"))
    books.append(Book(title="Рассказы"))
    books.append(Book(title="Американская трагедия"))
    books.append(Book(title="Принц и нищий"))
    books.append(Book(title="Красное и чёрное"))
    books.append(Book(title="Вишневый сад"))
    books.append(Book(title="Хитроумный идальго Дон Кихот Ламанчский"))
    books.append(Book(title="Жизнь взаймы"))
    books.append(Book(title="Тёмные аллеи"))
    books.append(Book(title="Судьба человека"))
    books.append(Book(title="Пятнадцатилетний капитан"))
    books.append(Book(title="Гранатовый браслет"))
    books.append(Book(title="Всадник без головы"))
    books.append(Book(title="Понедельник начинается в субботу"))
    books.append(Book(title="Нерв"))
    books.append(Book(title="Доктор Живаго"))
    books.append(Book(title="Трое в лодке, не считая собаки"))
    books.append(Book(title="Цветы для Элджернона"))
    books.append(Book(title="Великий Гэтсби"))
    books.append(Book(title="Король Лир"))
    books.append(Book(title="Обыкновенное чудо"))

    books_iter = iter(books)

    





























    
    
    authors.append(Author(name="Михаил Булгаков", books=[books[4], books[1]]))
    
    
    authors.append(Author(name="Михаил Лермонтов", books=[books[7]]))
    authors.append(Author(name="Антуан де Сент-Экзюпери", books=[books[8]]))
    
    
    
    authors.append(Author(name="Оскар Уайльд", books=[books[12]]))
    
    authors.append(Author(name="Александр Грибоедов", books=[books[14]]))
    authors.append(Author(name="Маргарет Митчелл", books=[books[15]]))
    
    
    
    
    authors.append(Author(name="ОГенри", books=[books[20]]))
    authors.append(Author(name="Федор Достоевский", books=[books[21], books[0], books[13]]))
    authors.append(Author(name="Александр Дюма", books=[books[22], books[9]]))

    authors.append(Author(name="Джейн Остин", books=[books[24]]))
    
    
    authors.append(Author(name="Илья Ильф, Евгений Петров", books=[books[27], books[5]]))
    authors.append(Author(name="Даниель Дефо", books=[books[28]]))
    authors.append(Author(name="Иоганн Вольфганг фон Гёте", books=[books[29]]))
    authors.append(Author(name="Иван Тургенев", books=[books[30]]))
    authors.append(Author(name="Артур Конан Дойль", books=[books[31], books[3]]))
    authors.append(Author(name="Борис Васильев", books=[books[32]]))
    authors.append(Author(name="Николай Гоголь", books=[books[33], books[16], books[19]]))
    authors.append(Author(name="Джек Лондон", books=[books[34]]))
     
    authors.append(Author(name="Алан Александр Милн", books=[books[36]]))
    
    authors.append(Author(name="Ярослав Гашек", books=[books[38]]))
    authors.append(Author(name="Виктор Гюго", books=[books[39]]))
    authors.append(Author(name="Александр Беляев", books=[books[40]]))
    authors.append(Author(name="Борис Акунин", books=[books[41]]))
    authors.append(Author(name="Станислав Лем", books=[books[42]]))
    authors.append(Author(name="Патрик Зюскинд", books=[books[43]]))
    authors.append(Author(name="Алексей Толстой", books=[books[44], books[6], books[18]]))
    authors.append(Author(name="Александр Пушкин", books=[books[45], books[2], books[26]]))
    authors.append(Author(name="Эмили Бронте", books=[books[46]]))
    authors.append(Author(name="Колин Маккалоу", books=[books[47]]))
    
    authors.append(Author(name="Эдгар По", books=[books[49]]))
    authors.append(Author(name="Теодор Драйзер", books=[books[50]]))
    authors.append(Author(name="Марк Твен", books=[books[51], books[25]]))
    authors.append(Author(name="Стендаль", books=[books[52]]))
    authors.append(Author(name="Антон Чехов", books=[books[53], books[10]]))
    authors.append(Author(name="Мигель Сервантес", books=[books[54]]))
    authors.append(Author(name="Эрих Мария Ремарк", books=[books[55], books[11]]))
    authors.append(Author(name="Иван Бунин", books=[books[56]]))
    authors.append(Author(name="Михаил Шолохов", books=[books[57], books[23]]))
    authors.append(Author(name="Жюль Верн", books=[books[58]]))
    authors.append(Author(name="Александр Куприн", books=[books[59]]))
    authors.append(Author(name="Томас Майн Рид", books=[books[60]]))
    authors.append(Author(name="Аркадий и Борис Стругацкие", books=[books[61], books[48], books[37]]))
    authors.append(Author(name="Владимир Высоцкий", books=[books[62]]))
    authors.append(Author(name="Борис Пастернак", books=[books[63]]))
    authors.append(Author(name="Джером К Джером", books=[books[64]]))
    authors.append(Author(name="Дэниел Киз", books=[books[65]]))
    authors.append(Author(name="Фрэнсис Скотт Фицджеральд", books=[books[66]]))
    authors.append(Author(name="Уильям Шекспир", books=[books[67], books[17]]))
    authors.append(Author(name="Евгений Шварц", books=[books[68]]))

    entities.extend(books)
    entities.extend(authors)

    for e in entities:
        db_session.add(e)
    db_session.commit()
