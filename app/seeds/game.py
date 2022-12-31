from app.models import db, Game, environment, SCHEMA
import datetime

def seed_games():
    game1 = Game(
        date = datetime.date(2022, 12, 31),
        time = datetime.time(17, 0, 0),
        team1id = 1,
        team2id = 2
    )


    db.session.add(game1)
    db.session.commit()

def undo_games():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.games RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM games")
    db.session.commit()
