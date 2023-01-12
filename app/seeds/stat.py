from app.models import db, Stat, environment, SCHEMA

def seed_stats():
    stat1 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '4',
        points = '25',
        assists = '11',
        rebounds = '8'
    )
    stat2 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '4',
        points = '1',
        assists = '1',
        rebounds = '1'
    )
    stat3 = Stat(
        teamid = '5',
        playerid = '1',
        gameid = '4',
        points = '1',
        assists = '19',
        rebounds = '15'
    )

    db.session.add(stat1)
    db.session.add(stat2)
    db.session.add(stat3)
    db.session.commit()

def undo_stats():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.stats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM stats")
    db.session.commit()
