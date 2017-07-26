-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c i tournament

CREATE TABLE Players (ID serial primary key, fullname text);

CREATE TABLE Matches (match_ID serial primary key,
	winner integer references Players(ID),
	loser integer references Players(ID));

CREATE VIEW number_of_wins AS SELECT Players.id, Players.fullname,
	(SELECT Count(Matches.winner)
	FROM Matches
	WHERE Matches.winner = Players.id) AS wins,
	(SELECT Count(Matches.match_ID)
	FROM Matches
	WHERE Matches.loser = Players.id OR Matches.winner = Players.id)
	AS Matches FROM Players;

