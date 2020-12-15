use webdevsignup;
select * from student1;
alter table student1 add  id int NOT NULL AUTO_INCREMENT;
alter table student1 auto_increment=1000;
desc student1;
ALTER TABLE student1 ADD id int not null;
ALTER TABLE student1 ADD id int NOT NULL AUTO_INCREMENT primary key FIRST;
select * from users;
alter table users add id int;
alter table users add foreign key(id) references student1(id);
alter table users 
  DROP COLUMN userid;
 ALTER TABLE users ADD userid int NOT NULL AUTO_INCREMENT primary key FIRST; 
  