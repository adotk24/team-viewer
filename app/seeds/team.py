from app.models import db, Team, environment, SCHEMA

def seed_teams():
    team1 = Team(
        name="Texas",
        mascot='Longhorns',
        city='Austin',
        state='Texas',
        userId='2'
    )
    team2 = Team(
        name='Dallas',
        mascot='Mavericks',
        city='Dallas',
        state='Texas',
        userId = '1'
    )
    team3 = Team(
        name='Team USA',
        mascot='Redeem',
        city='Washington D.C.',
        state='Virginia',
        userId='2'
    )
    team4 = Team(
        name='Callaway',
        mascot='Cavaliers',
        city='Hogansville',
        state='Georgia',
        userId='1'
    )
    team5 = Team(
        name='Swift Creek',
        mascot='Cougars',
        city='Chesterfield',
        state='Virginia',
        userId='3'
    )

    db.session.add(team1)
    db.session.add(team2)
    db.session.add(team3)
    db.session.add(team4)
    db.session.add(team5)
    db.session.commit()

def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.teams RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM teams")
    db.session.commit()
