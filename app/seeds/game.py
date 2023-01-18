from app.models import db, Game, environment, SCHEMA
from datetime import datetime

def seed_games():
    game1 = Game(
        datetime = datetime(2022, 12, 31, 12, 0),
        team1id = 1,
        team2id = 2
    )
    game2 = Game(
        datetime = datetime(2023, 1, 1, 12, 0),
        team1id = 1,
        team2id = 3
    )
    game3 = Game(
        datetime = datetime(2023, 1, 7, 12, 0),
        team1id = 1,
        team2id = 4
    )
    game4 = Game(
        datetime = datetime(2023, 1, 14, 12, 0),
        team1id = 1,
        team2id = 5
    )
    game5 = Game(
        datetime = datetime(2023, 1, 21, 12, 0),
        team1id = 1,
        team2id = 6
    )
    game6 = Game(
        datetime = datetime(2023, 2, 7, 12, 0),
        team1id = 1,
        team2id = 7
    )
    game7 = Game(
        datetime = datetime(2023, 2, 14, 12, 0),
        team1id = 1,
        team2id = 8
    )
    game8 = Game(
        datetime = datetime(2023, 2, 21, 12, 0),
        team1id = 1,
        team2id = 9
    )
    game9 = Game(
        datetime = datetime(2023, 2, 28, 12, 0),
        team1id = 1,
        team2id = 10
    )
    game10 = Game(
        datetime = datetime(2023, 2, 28, 12, 0),
        team1id = 2,
        team2id = 3
    )
    game11 = Game(
        datetime = datetime(2023, 1, 2, 12, 0),
        team1id = 2,
        team2id = 4
    )
    game12 = Game(
        datetime = datetime(2023, 1, 9, 12, 0),
        team1id = 2,
        team2id = 5
    )
    game13 = Game(
        datetime = datetime(2023, 1, 16, 12, 0),
        team1id = 2,
        team2id = 6
    )
    game14 = Game(
        datetime = datetime(2023, 1, 23, 12, 0),
        team1id = 2,
        team2id = 7
    )
    game15 = Game(
        datetime = datetime(2023, 1, 30, 12, 0),
        team1id = 2,
        team2id = 8
    )
    game16 = Game(
        datetime = datetime(2023, 2, 7, 12, 0),
        team1id = 2,
        team2id = 9
    )
    game17 = Game(
        datetime = datetime(2023, 2, 14, 12, 0),
        team1id = 2,
        team2id = 10
    )
    game18 = Game(
        datetime = datetime(2023, 1, 3, 12, 0),
        team1id = 3,
        team2id = 4
    )
    game19 = Game(
        datetime = datetime(2023, 1, 10, 12, 0),
        team1id = 3,
        team2id = 5
    )
    game20 = Game(
        datetime = datetime(2023, 1, 17, 12, 0),
        team1id = 3,
        team2id = 6
    )
    game21 = Game(
        datetime = datetime(2023, 1, 24, 12, 0),
        team1id = 3,
        team2id = 7
    )
    game22 = Game(
        datetime = datetime(2023, 2, 1, 12, 0),
        team1id = 3,
        team2id = 8
    )
    game23 = Game(
        datetime = datetime(2023, 2, 8, 12, 0),
        team1id = 3,
        team2id = 9
    )
    game24 = Game(
        datetime = datetime(2023, 2, 15, 12, 0),
        team1id = 3,
        team2id = 10
    )
    game25 = Game(
        datetime = datetime(2023, 1, 4, 12, 0),
        team1id = 4,
        team2id = 5
    )
    game26 = Game(
        datetime = datetime(2023, 1, 11, 12, 0),
        team1id = 4,
        team2id = 6
    )
    game27 = Game(
        datetime = datetime(2023, 1, 18, 12, 0),
        team1id = 4,
        team2id = 7
    )
    game28 = Game(
        datetime = datetime(2023, 1, 26, 12, 0),
        team1id = 4,
        team2id = 8
    )
    game29 = Game(
        datetime = datetime(2023, 2, 4, 12, 0),
        team1id = 4,
        team2id = 9
    )
    game30 = Game(
        datetime = datetime(2023, 2, 11, 12, 0),
        team1id = 4,
        team2id = 10
    )
    game31 = Game(
        datetime = datetime(2023, 1, 5, 12, 0),
        team1id = 5,
        team2id = 6
    )
    game32 = Game(
        datetime = datetime(2023, 1, 12, 12, 0),
        team1id = 5,
        team2id = 7
    )
    game33 = Game(
        datetime = datetime(2023, 1, 19, 12, 0),
        team1id = 5,
        team2id = 8
    )
    game34 = Game(
        datetime = datetime(2023, 1, 26, 12, 0),
        team1id = 5,
        team2id = 9
    )
    game35 = Game(
        datetime = datetime(2023, 2, 3, 12, 0),
        team1id = 5,
        team2id = 10
    )
    game36 = Game(
        datetime = datetime(2023, 1, 6, 12, 0),
        team1id = 6,
        team2id = 7
    )
    game37 = Game(
        datetime = datetime(2023, 1, 13, 12, 0),
        team1id = 6,
        team2id = 8
    )
    game38 = Game(
        datetime = datetime(2023, 1, 20, 12, 0),
        team1id = 6,
        team2id = 9
    )
    game39 = Game(
        datetime = datetime(2023, 1, 27, 12, 0),
        team1id = 6,
        team2id = 10
    )
    game40 = Game(
        datetime = datetime(2023, 1, 7, 12, 0),
        team1id = 7,
        team2id = 8
    )
    game41 = Game(
        datetime = datetime(2023, 1, 14, 12, 0),
        team1id = 7,
        team2id = 9
    )
    game42 = Game(
        datetime = datetime(2023, 1, 21, 12, 0),
        team1id = 7,
        team2id = 10
    )
    game43 = Game(
        datetime = datetime(2023, 12, 21, 12, 0),
        team1id = 8,
        team2id = 9
    )
    game44 = Game(
        datetime = datetime(2023, 12, 29, 12, 0),
        team1id = 8,
        team2id = 10
    )
    game45 = Game(
        datetime = datetime(2023, 12, 21, 12, 0),
        team1id = 9,
        team2id = 10
    )





    db.session.add(game1)
    db.session.add(game2)
    db.session.add(game3)
    db.session.add(game4)
    db.session.add(game5)
    db.session.add(game6)
    db.session.add(game7)
    db.session.add(game8)
    db.session.add(game9)
    db.session.add(game10)
    db.session.add(game11)
    db.session.add(game12)
    db.session.add(game13)
    db.session.add(game14)
    db.session.add(game15)
    db.session.add(game16)
    db.session.add(game17)
    db.session.add(game18)
    db.session.add(game19)
    db.session.add(game20)
    db.session.add(game21)
    db.session.add(game22)
    db.session.add(game23)
    db.session.add(game24)
    db.session.add(game25)
    db.session.add(game26)
    db.session.add(game27)
    db.session.add(game28)
    db.session.add(game29)
    db.session.add(game30)
    db.session.add(game31)
    db.session.add(game32)
    db.session.add(game33)
    db.session.add(game34)
    db.session.add(game35)
    db.session.add(game36)
    db.session.add(game37)
    db.session.add(game38)
    db.session.add(game39)
    db.session.add(game40)
    db.session.add(game41)
    db.session.add(game42)
    db.session.add(game43)
    db.session.add(game44)
    db.session.add(game45)

    db.session.commit()

def undo_games():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.games RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM games")
    db.session.commit()
