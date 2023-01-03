from app.models import db, Game, environment, SCHEMA
from datetime import datetime

def seed_games():
    game1 = Game(
        datetime = datetime(2022, 12, 31, 12, 0),
        matchupId = 1,
        # team2id = 2
    )
    game2 = Game(
        datetime = datetime(2023, 1, 1, 12, 0),
        matchupId = 2
    )
    game3 = Game(
        datetime = datetime(2023, 1, 2, 12, 0),
        matchupId = 3
    )
    game4 = Game(
        datetime = datetime(2023, 1, 1, 12, 0),
        matchupId = 4
    )
    game5 = Game(
        datetime = datetime(2022, 12, 31, 12, 0),
        matchupId = 5
    )


    db.session.add(game1)
    db.session.add(game2)
    db.session.add(game3)
    db.session.add(game4)
    db.session.add(game5)
    db.session.commit()

def undo_games():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.games RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM games")
    db.session.commit()
