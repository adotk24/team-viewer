from app.models import db, Team, environment, SCHEMA

def seed_teams():
    team1 = Team(
        name="Hebron",
        mascot='Hawks',
        city='Carrollton',
        state='Texas',
        year='2022'
    )
    team2 = Team(
        name='Lewisville',
        mascot="Fighting Farmers",
        city='Lewisville',
        state='Texas',
        year='2022'
    )
    team3 = Team(
        name='Callaway',
        mascot='Cavaliers',
        city='Hogansville',
        state='Georgia',
        year='2022'
    )
    team4 = Team(
        name='Midlothian',
        mascot='Trojans',
        city='Midlothian',
        state='Virginia',
        year='2022'
    )
    team5 = Team(
        name='Swift Creek',
        mascot='Cougars',
        city='Chesterfield',
        state='Virginia',
        year='2022'
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
