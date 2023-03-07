-- Active: 1677903021603@@127.0.0.1@3306@badminton
alter table player add constraint PK_player  PRIMARY KEY(player_id);

alter table playtime add constraint PK_playtime  PRIMARY KEY(player_id);


