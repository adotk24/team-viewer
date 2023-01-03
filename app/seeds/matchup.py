from app.models import Matchup, db, environment, SCHEMA


def seed_matchup():
    # insert_stment1 = matchup.insert().values(team1id = 1, team2id = 2)
    # insert_stment2 = matchup.insert().values(team1id = 2, team2id = 3)
    # insert_stment3 = matchup.insert().values(team1id = 3, team2id = 4)
    # insert_stment4 = matchup.insert().values(team1id = 4, team2id = 5)
    # insert_stment5 = matchup.insert().values(team1id= 5, team2id = 1)

    # db.session.execute(insert_stment1)
    # db.session.execute(insert_stment2)
    # db.session.execute(insert_stment3)
    # db.session.execute(insert_stment4)
    # db.session.execute(insert_stment5)
    matchup1 = Matchup(
        team1id = 1,
        team2id = 2
    )
    matchup2 = Matchup(
        team1id = 2,
        team2id = 3
    )
    matchup3 = Matchup(
        team1id = 3,
        team2id = 4
    )
    matchup4 = Matchup(
        team1id = 4,
        team2id = 5
    )
    matchup5 = Matchup(
        team1id = 5,
        team2id = 1
    )
    db.session.add(matchup1)
    db.session.add(matchup2)
    db.session.add(matchup3)
    db.session.add(matchup4)
    db.session.add(matchup5)
    db.session.commit()






def undo_matchup():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.matchup RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM matchup")

    db.session.commit()
