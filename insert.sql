-- Active: 1671688956478@@127.0.0.1@3308@badminton
show tables;



select * from game;
INSERT into game  values(1,"Badminton");
INSERT into game  values(2,"Football");


select * from player;
INSERT into player  values(101,"Sameer","+916362410598");
INSERT into player  values(102,"Saleem","+916362410655");
INSERT into player  values(103,"Devanshu","+917030732152"); 
INSERT into player  values(104,"Devayush","+918095176737");
INSERT into player  values(105,"Aniket","+918073225704");
INSERT into player  values(106,"Teja","+918310236428");
INSERT into player  values(107,"Vismay","+918792819255");
INSERT into player  values(108,"Ayush","+917907185150 ");
INSERT into player  values(109,"Shabeer","");
INSERT into player  values(110,"Rathee","+919602111040");
INSERT into player  values(111,"Deepu","+917019179846");
INSERT into player  values(112,"Nitin","");
INSERT into player  values(113,"Shukla","");
INSERT into player  values(114,"Alok","+917892107857");
INSERT into player  values(115,"Navneet","+919606583361");
INSERT into player  values(116,"Yajath","+919980536425");
INSERT into player  values(117,"Sharfarz","");
INSERT into player  values(118,"Rishikesh","");
INSERT into player  values(119,"Arfan","");


select * from playtime;

INSERT into playtime (player_id,game_id)  values(101,1);
INSERT into playtime (player_id,game_id)  values(102,1);
INSERT into playtime (player_id,game_id)  values(104,1);
INSERT into playtime (player_id,game_id)  values(105,1);
INSERT into playtime (player_id,game_id)  values(106,1);
INSERT into playtime (player_id,game_id)  values(107,1);
INSERT into playtime (player_id,game_id)  values(108,1);
INSERT into playtime (player_id,game_id)  values(109,1);
INSERT into playtime (player_id,game_id)  values(110,1);
INSERT into playtime (player_id,game_id)  values(111,1);
INSERT into playtime (player_id,game_id)  values(112,1);
INSERT into playtime (player_id,game_id)  values(113,1);
INSERT into playtime (player_id,game_id)  values(114,1);
INSERT into playtime (player_id,game_id)  values(115,1);
INSERT into playtime (player_id,game_id)  values(116,1);
INSERT into playtime (player_id,game_id)  values(117,1);
INSERT into playtime (player_id,game_id)  values(118,1);
INSERT into playtime (player_id,game_id)  values(119,1);


select * from player;

DELETE from player where player_id = 101 and name="sameer";

TRUNCATE TABLE player;
