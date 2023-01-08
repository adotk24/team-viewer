from app.models import db, Stat, environment, SCHEMA

def seed_stats():
    stat1 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '1',
        points = '25',
        assists = '11',
        rebounds = '8'
    )

    db.session.add(stat1)
    db.session.commit()

def undo_stats():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.stats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM stats")
    db.session.commit()
