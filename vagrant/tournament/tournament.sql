-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
drop database if exists tournament;
create database tournament;
\c tournament

create table players
(
  name text,
  id serial primary key
);

create table matches
(
  winner int references players (id),
  loser int references players (id),
  id serial primary key
);

create view wins as
  select players.id,count(matches.winner) as wins
  from players
  left join matches
  on players.id=matches.winner
  group by players.id;

create view losses as
  select players.id,count(matches.loser) as losses
  from players
  left join matches
  on players.id=matches.loser
  group by players.id;

create view total_matches as
  select wins.id, wins.wins+losses.losses as matches
  from wins join losses on wins.id = losses.id;
