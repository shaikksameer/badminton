-- Active: 1671688956478@@127.0.0.1@3308@badminton
alter table playtime 
add column `01_03_2023` DECIMAL(4,2);


select * from playtime;

insert into playtime(`03_03_2023`) values(1);

delete from playtime where 03_03_2023 = 1;

select * from player;



show tables;

CREATE table rough(
    player_id int(10),
    game_id int(10),
    01_02_2023 DECIMAL(4,2)
);


select * from rough;

alter table rough
add column `03_03_2023` decimal(4,2);




update rough
set 
`03_03_2023`=1.5
where player_id=102;

CREATE table rough_name(
    player_id int(10),
    name varchar(10)
);
insert into rough_name 
values (101,"sameer"),
(102,"saleem"),
(103,"vro");

select * from  rough_name;


select * from playtime;
select * from rough;

update  playtime set 03_03_2023=1.0 where player_id =101;
