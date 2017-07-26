#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2

def connect(db_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:"""suggested by reviewer"""
        db = psycopg2.connect("dbname={}".format(db_name))
        c = db.cursor()
        return db, c
    except:
        print("Database not found")

def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("TRUNCATE Matches")"""faster than DELETE"""
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("TRUNCATE Players")"""suggested by reviewer"""
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    query = 'SELECT count(*) FROM Players;'
    c.execute(query)
    db.commit()
    db.close()

def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)  
    Args:
      name: the player's full name (need not be unique).
    """
    """suggested by reviewer"""
    db, c = connect()
    query = 'INSERT INTO players(name) VALUES(%s);'
    parameter = (name,)
    c.execute(query, parameter)
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    query = 'SELECT * FROM number_of_wins ORDER by wins;'
    c.execute(query)
    db.commit()
    db.close()

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    query = "INSERT INTO Matches(winner, loser) VALUES(%s, %s);"
    param = (content,)
    c.execute(query, param)
    db.commit()
    db.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db = connect()
    c = db.cursor()
    temp = []
    c.execute("SELECT id, fullname FROM number_of_wins Order by wins DESC")
    value = c.fetchall()
    for i in range(1, len(value), 2):
        one = value[i - 1]
        two = value[i]
        temp.append((one[0], one[1], two[0], two[1]))
    for pairs in temp:
        db.commit()
        db.close()
        return temp
