Test Task
================

According to the Task, has been implemented next:

1. Created two entities: Book(has 'title' field) and Author(has 'name' field). The reletionship is M2M.
2. Addition entity User was used to authorize user. The entity has 'login', 'password', 'is_authorized' and 'is_admin' fields. 'is_admin' property was used for authorize users to edite list of users. 'is_authorized' users can searching books and viewing the list of books.




For run project please do the next steps
--------------
cd ./prod_lib/src
sudo pip install -r requirements.txt
python manage.py run_init_db
python manage.py post_test_data
python manage.py runserver