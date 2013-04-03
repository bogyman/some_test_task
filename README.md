Test Task
================

According to the Task, has been implemented next:

1. Created two entities: Book(has 'title' field) and Author(has 'name' field). The reletionship is M2M.
2. Addition entity User was used to authorize user. The entity has 'login', 'password', 'is_authorized' and 'is_admin' fields. 'is_admin' property was used for authorize users to edite list of users. Users 'is_authorized' property  can searching books and viewing the list of books.
3. Anonymous  users can register himselfs or log in. After registration can do nothing during Admin set user`s 'is_authorized' to "True". 
4. Searching the books by keyword. The searching occurs in books` titles and authors` names. If keyword is empty, whole list of books is shown. Every lists has paginations.
5. Admin interface is available for users, who have 'is_admin' in 'True'
6. Forms fields are validated for empty value.



For run project please do the next steps
--------------
    cd ./prod_lib/src
    sudo pip install -r requirements.txt # installing requirement packages
    python manage.py run_init_db # create database file and create tables
    python manage.py post_test_data # insert test data into the db
    python manage.py runserver 