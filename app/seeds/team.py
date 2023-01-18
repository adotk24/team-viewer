from app.models import db, Team, environment, SCHEMA

def seed_teams():
    team1 = Team(
        name="Texas",
        mascot='Longhorns',
        city='Austin',
        state='Texas',
        userId='1'
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
        name='Boston',
        mascot='Celtics',
        city='Boston',
        state="Massachusetts",
        userId='3'
    )
    team6 = Team(
        name='Milwaukee',
        mascot='Bucks',
        city='Milwaukee',
        state='Wisconsin',
        userId='3'
    )
    team7 = Team(
        name='Philadelphia',
        mascot='76ers',
        city='Philadelphia',
        state='Pennsylvania',
        userId='3'
    )
    team8 = Team(
        name='Brooklyn',
        mascot='Nets',
        city='Bed Stuy',
        state='New York',
        userId='3'
    )
    team9 = Team(
        name='Denver',
        mascot='Nuggets',
        city='Boulder',
        state='Colorado',
        userId='3'
    )
    team10 = Team(
        name='New York',
        mascot='Knicks',
        city='New York City',
        state='New York',
        userId='3'
    )
    # team11 = Team(
    #     name='New Orleans',
    #     mascot='Pelicans',
    #     city='Baton Route',
    #     state='Louisiana',
    #     userId='3'
    # )
    # team12 = Team(
    #     name='Sacramento',
    #     mascot='Kings',
    #     city='Sacramento',
    #     state='California',
    #     userId='3'
    # )


    db.session.add(team1)
    db.session.add(team2)
    db.session.add(team3)
    db.session.add(team4)
    db.session.add(team5)
    db.session.add(team6)
    db.session.add(team7)
    db.session.add(team8)
    db.session.add(team9)
    db.session.add(team10)
    # db.session.add(team11)
    # db.session.add(team12)
    db.session.commit()

def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.teams RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM teams")
    db.session.commit()
