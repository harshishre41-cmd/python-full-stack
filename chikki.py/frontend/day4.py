Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password for user postgres:

psql (18.7)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=# CREATE DATABASE collage;
CREATE DATABASE
postgres=# \l
                                                                    List of databases
   Name    |  Owner   | Encoding | Locale Provider |          Collate           |           Ctype            | Locale | ICU Rules |   Access privileges
-----------+----------+----------+-----------------+----------------------------+----------------------------+--------+-----------+-----------------------
 collage   | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 postgres  | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 student   | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 template0 | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           | =c/postgres          +
           |          |          |                 |                            |                            |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           | =c/postgres          +
           |          |          |                 |                            |                            |        |           | postgres=CTc/postgres
(5 rows)


postgres=# CREATE TABLE student (
postgres(# id SERIAL PRIMARY KEY ,
postgres(# name VARCHAR(100),
postgres(# age INT,
postgres(# course VARCHAR(50),
postgres(# marks INT );
CREATE TABLE
postgres=# \l
                                                                    List of databases
   Name    |  Owner   | Encoding | Locale Provider |          Collate           |           Ctype            | Locale | ICU Rules |   Access privileges
-----------+----------+----------+-----------------+----------------------------+----------------------------+--------+-----------+-----------------------
 collage   | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 postgres  | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 student   | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 template0 | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           | =c/postgres          +
           |          |          |                 |                            |                            |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           | =c/postgres          +
           |          |          |                 |                            |                            |        |           | postgres=CTc/postgres
(5 rows)


postgres=# \c collage
You are now connected to database "collage" as user "postgres".
collage=# CREATE TABLE student (
collage(# id SERIAL PRIMARY KEY,
collage(# name VARCHAR(100),
collage(# age INT,
collage(# course VARCHAR(50),
collage(# marks INT );
CREATE TABLE
collage=# \dt
           List of tables
 Schema |  Name   | Type  |  Owner
--------+---------+-------+----------
 public | student | table | postgres
(1 row)


collage=# INSERT INTO students (name, age, course, marks)
collage-# VALUES
collage-# ('Rahul', 21, 'BCA', 85),
collage-# ('Priya', 20, 'BCA', 90),
collage-# ('Arun', 22, 'NCA',  70)
collage-# FVFEFC
collage-# INSERT INTO students (name, age, course, marks)
collage-# VALUES
collage-# ('Rahul', 21, 'BCA', 85),
collage-# ('Priya', 20, 'BCA', 90),
collage-# ('Arun', 22, 'NCA',  70),
collage-# ('Siri', 24, 'DSA', 86);
ERROR:  syntax error at or near "FVFEFC"
LINE 6: FVFEFC
        ^
collage=# INSERT INTO students (name, age, course, marks)
collage-# VALUES
collage-# ('Rahul', 21, 'BCA', 85),
collage-# ('Priya', 20, 'BCA', 90),
collage-# ('Arun', 22, 'NCA',  70),
collage-# ('Rahul', 21, 'BCA', 85),
collage-# ;
ERROR:  syntax error at or near ";"
LINE 7: ;
        ^
collage=# INSERT INTO students (name, age, course, marks)
collage-# VALUES
collage-# (1,'Rahul', 21, 'BCA', 85),
collage-# (2,'Priya', 20, 'BCA', 90),
collage-# (3,'Arun', 22, 'NCA',  70),
collage-# (4,'Siri', 22, 'DSA',  86);
ERROR:  relation "students" does not exist
LINE 1: INSERT INTO students (name, age, course, marks)
                    ^
collage=# INSERT INTO student (name, age, course, marks)
collage-# VALUES
collage-# (1,'Rahul', 21, 'BCA', 85),
collage-# (2,'Priya', 20, 'BCA', 90),
collage-# (3,'Arun', 22, 'NCA',  70),
collage-# (4,'Siri', 22, 'DSA',  86);
ERROR:  INSERT has more expressions than target columns
LINE 3: (1,'Rahul', 21, 'BCA', 85),
                               ^
collage=# INSERT INTO student (name, age, course, marks)
collage-# ;
ERROR:  syntax error at or near ";"
LINE 2: ;
        ^
collage=# INSERT INTO student (name, age, course, marks)
collage-# VALUES
collage-# (1,'Rahul', 21, 'BCA',85),
collage-# (2,'Priya', 20, 'BCA',90),
collage-# (3,'Arun', 22, 'NCA',70),
collage-# (4,'Siri', 22, 'DSA',86);
ERROR:  INSERT has more expressions than target columns
LINE 3: (1,'Rahul', 21, 'BCA',85),
                              ^
collage=# SELECT * FROM student
collage-# ORDER BY mark asc;
ERROR:  column "mark" does not exist
LINE 2: ORDER BY mark asc;
                 ^
HINT:  Perhaps you meant to reference the column "student.marks".
collage=# update student
collage-# set marks=100
collage-# where id=1;
UPDATE 0
collage=# INSERT INTO student (id,name, age, course, marks)
collage-# VALUES
collage-# (1,'Rahul', 21, 'BCA', 85),
collage-# (2,'Priya', 20, 'BCA', 90),
collage-# (3,'Arun', 22, 'NCA',  70),
collage-# (4,'Siri', 22, 'DSA',86);
INSERT 0 4
collage=# SELECT * FROM student;
 id | name  | age | course | marks
----+-------+-----+--------+-------
  1 | Rahul |  21 | BCA    |    85
  2 | Priya |  20 | BCA    |    90
  3 | Arun  |  22 | NCA    |    70
  4 | Siri  |  22 | DSA    |    86
(4 rows)


collage=# SELECT * FROM student
collage-# WHERE marks=90;
 id | name  | age | course | marks
----+-------+-----+--------+-------
  2 | Priya |  20 | BCA    |    90
(1 row)


collage=# SELECT * FROM student
collage-# ORDER BY mark asc;
ERROR:  column "mark" does not exist
LINE 2: ORDER BY mark asc;
                 ^
HINT:  Perhaps you meant to reference the column "student.marks".
collage=# SELECT * FROM student
collage-# ORDER BY marks asc;
 id | name  | age | course | marks
----+-------+-----+--------+-------
  3 | Arun  |  22 | NCA    |    70
  1 | Rahul |  21 | BCA    |    85
  4 | Siri  |  22 | DSA    |    86
  2 | Priya |  20 | BCA    |    90
(4 rows)


collage=# update student
collage-# set marks=100
collage-# where id=1;
UPDATE 1
collage=# SELECT * FROM student;
 id | name  | age | course | marks
----+-------+-----+--------+-------
  2 | Priya |  20 | BCA    |    90
  3 | Arun  |  22 | NCA    |    70
  4 | Siri  |  22 | DSA    |    86
  1 | Rahul |  21 | BCA    |   100
(4 rows)


collage=# update student
collage-# set marks=100
collage-# where id=1;
UPDATE 1
collage=# SELECT * FROM student;
 id | name  | age | course | marks
----+-------+-----+--------+-------
  2 | Priya |  20 | BCA    |    90
  3 | Arun  |  22 | NCA    |    70
  4 | Siri  |  22 | DSA    |    86
  1 | Rahul |  21 | BCA    |   100
(4 rows)


collage=# update student
collage-# set marks=100
collage-# where id in(1.,2,3);
UPDATE 3
collage=# delete student
collage-# where id=3;
ERROR:  syntax error at or near "student"
LINE 1: delete student
               ^
collage=# delete from student where id=3;
DELETE 1
collage=#
collage=#
collage=#
collage=# create table student_card(
collage(# card_id serial primary key,
collage(# card_number varchar(50),
collage(# id int unique references students(id)
collage(# );
ERROR:  relation "students" does not exist
collage=# create table student_card(
collage(# card_id serial primary key,
collage(# card_number varchar(50),
collage(# id int unique references student(id)
collage(# );
CREATE TABLE
collage=# insert into student_card(card_number,id)
collage-# values
collage-# ('card101',1),
collage-# ;
ERROR:  syntax error at or near ";"
LINE 4: ;
        ^
collage=# insert into student_card(card_name,id)
collage-# values
collage-# ('card101',1)
collage-# ;
ERROR:  column "card_name" of relation "student_card" does not exist
LINE 1: insert into student_card(card_name,id)
                                 ^
collage=# insert into student_card(card_name,id)
collage-# values
collage-# ('card101',1),
collage-# ('card102',2);
ERROR:  column "card_name" of relation "student_card" does not exist
LINE 1: insert into student_card(card_name,id)
                                 ^
collage=# insert into student_card(card_number,id)
collage-# values
collage-# ('card101',1),
collage-# ('card102',2);
INSERT 0 2
collage=#
collage=#
collage=#
collage=#
collage=# insert into student_card(card_name,id)
collage-# ;
ERROR:  syntax error at or near ";"
LINE 2: ;
        ^
collage=# insert into student_card(card_number,id)
collage-# values
collage-# ('card104',4);
INSERT 0 1
collage=# SELECT * FROM student
collage-# _card;
 id | name  | age | course | marks
----+-------+-----+--------+-------
  4 | Siri  |  22 | DSA    |    86
  2 | Priya |  20 | BCA    |   100
  1 | Rahul |  21 | BCA    |   100
(3 rows)


collage=# SELECT * FROM student_card;
 card_id | card_number | id
---------+-------------+----
       1 | card101     |  1
       2 | card102     |  2
       3 | card104     |  4
(3 rows)


collage=# insert into student
collage-# values
collage-# (5,'keerthi',20,99);
INSERT 0 1
collage=# insert into student_card(card_number,id)
collage-# values
collage-# ('card105',5);
INSERT 0 1
collage=# SELECT * FROM student_card;
 card_id | card_number | id
---------+-------------+----
       1 | card101     |  1
       2 | card102     |  2
       3 | card104     |  4
       4 | card105     |  5
(4 rows)


collage=# create table departments(
collage(# department_id serial primary key,
collage(# department_name varchar(100) );
CREATE TABLE
collage=#
collage=#
collage=# insert into departments (departments_name)
collage-# values
collage-# ('aiml')
collage-# ('cse')
collage-# ('ise')
collage-# ('aero');
ERROR:  syntax error at or near "("
LINE 4: ('cse')
        ^
collage=# insert into departments (departments_name)
collage-# values
collage-# ('aiml'),
collage-# ('cse'),
collage-# ('ise'),
collage-# ('aero');
ERROR:  column "departments_name" of relation "departments" does not exist
LINE 1: insert into departments (departments_name)
                                 ^
collage=# insert into departments (department_name)
collage-# values
collage-# ('aiml'),
collage-# ('cse'),
collage-# ('ise'),
collage-# ('aero');
INSERT 0 4
collage=#
collage=#
collage=# create table employee(
collage(# employee_id serial primary key,
collage(# employee_name varchar(100),
collage(# salary int,
collage(# department_id int refrences department(department_id)
collage(# );
ERROR:  syntax error at or near "refrences"
LINE 5: department_id int refrences department(department_id)
                          ^
collage=# create table employee(
collage(# employee_id serial primary key,
collage(# employee_name varchar(100),
collage(# salary int,
collage(# department_id int references department(department_id)
collage(# );
ERROR:  relation "department" does not exist
collage=# create table employee(
collage(# employee_id serial primary key,
collage(# employee_name varchar(100),
collage(# salary int,
collage(# department_id int references departments(department_id)
collage(# );
CREATE TABLE
collage=#
collage=#
collage=# insert into employee(employee_name,salary,department_id)
collage-# values
collage-# ('rahul',25000,2),
collage-# ('devi',30000,1),
collage-# ('venkat',40000,3);
INSERT 0 3
collage=#