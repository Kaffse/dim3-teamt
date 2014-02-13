#Team T Distributed Information Management 3 Project
##Collaborative Requirement Tracker

Tasked to create a collaborative system to sort, prioritise and organise requirements ala Trello. To be made in Django.


Link to project's presentation:https://docs.google.com/presentation/d/17wDcwCy9t_2nMox4KuVBKrv8DJ6ueVUaXi3OrerJYH4/edit?usp=sharing

Team Members: Alastair Weir (110682w), Keir Smith, Peter Yordanov, Gordon Adam, Georgi Dimitrov


Installation instructions (UNIX)

Clone this repo
Install mysql mysql-server mysql-python
pip install south
mysql -u root -p
CREATE DATABASE dim3;
CREATE USER 'root'@'localhost' IDENTIFIED BY 'dim3';
GRANT ALL PRIVILEGES ON mdrsDatabase.* TO 'mdrs'@'localhost';
quit
python manage.py syncdb
python manage.py runserver

Installation instructions (Windows)

Clone this repo
Install mysql mysql-server mysql-python
pip install south
Set up Xampp  - Apache + MySQL (user root no password on localhost)
Start services > Create dim3 database in phpMyAdmin
python manage.py syncdb
python manage.py runserver
