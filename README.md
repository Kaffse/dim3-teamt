#Team T Distributed Information Management 3 Project
##Aggressive Backpack

Tasked to create a collaborative system to sort, prioritise and organise requirements ala Trello. To be made in Django.


Link to project's presentation:https://docs.google.com/presentation/d/17wDcwCy9t_2nMox4KuVBKrv8DJ6ueVUaXi3OrerJYH4/edit?usp=sharing

Team Members: Alastair Weir (110682w), Keir Smith, Peter Yordanov (1103620y), Gordon Adam, Georgi Dimitrov


Installation instructions (UNIX)

1. Clone this repo
2. Install mysql mysql-server mysql-python
3. pip install south
4. mysql -u root -p
5. CREATE DATABASE dim3;
6. CREATE USER 'root'@'localhost' IDENTIFIED BY 'dim3';
7. GRANT ALL PRIVILEGES ON dim3.* TO 'dim3'@'localhost';
8. quit
9. python manage.py syncdb
10. python manage.py runserver

Installation instructions (Windows)

1. Clone this repo
2. Install mysql mysql-server mysql-python
3. pip install south
4. Set up Xampp  - Apache + MySQL (user root no password on localhost)
5. Start services > Create dim3 database in phpMyAdmin
6. python manage.py syncdb
7. python manage.py runserver
