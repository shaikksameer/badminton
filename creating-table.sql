-- Active: 1677903021603@@127.0.0.1@3306@badminton
use badminton ;

show tables;

create table player(
    player_id int(10),
    name varchar(20),
    phoneno VARCHAR(20)
);

create table game(
    game_id int(10),
    game_name VARCHAR(20)
);

/* 
playtime table is made using python 
becuase we have to give dynamic date as a column name 
which is not possible in sql
*/

drop table playtime;
