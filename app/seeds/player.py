from app.models import db, Player, environment, SCHEMA

def seed_players():
    player1 = Player(
        firstName = 'Andrew',
        lastName = 'Kim',
        height = '73',
        number = '13',
        teamId = '1',
        year = 'Senior',
        position = 'SG'
    )
    player2 = Player(
        firstName = 'Joe',
        lastName = 'Brown',
        height = '75',
        number = '0',
        teamId = '1',
        year = 'Senior',
        position = 'C'
    )
    player3 = Player(
        firstName = 'Milton',
        lastName = 'Turner',
        height = '72',
        number = '2',
        teamId = '1',
        year = 'Junior',
        position = 'SF'
    )
    player4 = Player(
        firstName = 'Tamarcus',
        lastName = 'Smith',
        height = '72',
        number = '3',
        teamId = '1',
        year = 'Junior',
        position = 'PG'
    )
    player5 = Player(
        firstName = 'Dre',
        lastName = 'Martin',
        height = '71',
        number = '5',
        teamId = '1',
        year = 'Senior',
        position = 'SG'
    )
    player6 = Player(
        firstName='Lincoln',
        lastName = 'Chalmers',
        height = '76',
        number = '11',
        teamId = '4',
        year = 'Junior',
        position = 'PF'
    )


    db.session.add(player1)
    db.session.add(player2)
    db.session.add(player3)
    db.session.add(player4)
    db.session.add(player5)
    db.session.add(player6)
    db.session.commit()

def undo_players():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM players")
    db.session.commit()
