CREATE DATABASE IF NOT EXISTS `Users`;
GRANT ALL ON Users.* TO 'user'@'%';

USE Users;

create table Users(
  user_id text not null,
  user_name text not null,
  user_email text,
  user_profile_pic text not null,
  primary key(user_id(254)),
  INDEX(user_email(254))
)DEFAULT CHARACTER SET=utf8;
