from app.models import db, Player, environment, SCHEMA

def seed_players():
    player1 = Player(
        firstName = 'Timmy',
        lastName = 'Allen',
        height = '78',
        number = '0',
        teamId = '1',
        year = 'Senior',
        position = 'F'
    )
    player2 = Player(
        firstName = 'Dylan',
        lastName = 'Disu',
        height = '81',
        number = '1',
        teamId = '1',
        year = 'Senior',
        position = 'F'
    )
    player3 = Player(
        firstName = 'Arterio',
        lastName = 'Morris',
        height = '75',
        number = '2',
        teamId = '1',
        year = 'Freshman',
        position = 'G'
    )
    player4 = Player(
        firstName = 'Tyrese',
        lastName = 'Hunter',
        height = '72',
        number = '4',
        teamId = '1',
        year = 'Sophomore',
        position = 'G'
    )
    player5 = Player(
        firstName = 'Marcus',
        lastName = 'Carr',
        height = '74',
        number = '5',
        teamId = '1',
        year = 'Senior',
        position = 'G'
    )
    player6 = Player(
        firstName="Sir'Jabari",
        lastName = 'Rice',
        height = '76',
        number = '10',
        teamId = '1',
        year = 'Senior',
        position = 'G'
    )
    player7 = Player(
        firstName="Dillon",
        lastName = 'Mitchell',
        height = '80',
        number = '23',
        teamId = '1',
        year = 'Freshman',
        position = 'F'
    )
    player8 = Player(
        firstName="Christian",
        lastName = 'Bishop',
        height = '79',
        number = '32',
        teamId = '1',
        year = 'Senior',
        position = 'F'
    )

    player9 = Player(
        firstName="Luka",
        lastName = 'Doncic',
        height = '79',
        number = '77',
        teamId = '2',
        year = 'Freshman',
        position = 'PG'
    )
    player10 = Player(
        firstName="Spencer",
        lastName = 'Dinwiddie',
        height = '78',
        number = '26',
        teamId = '2',
        year = 'Junior',
        position = 'PG'
    )
    player11 = Player(
        firstName="Dorian",
        lastName = 'Finney-Smith',
        height = '79',
        number = '10',
        teamId = '2',
        year = 'Junior',
        position = 'PF'
    )
    player12 = Player(
        firstName="Josh",
        lastName = 'Green',
        height = '77',
        number = '8',
        teamId = '2',
        year = 'Freshman',
        position = 'SG'
    )
    player13 = Player(
        firstName="Tim",
        lastName = 'Hardaway Jr.',
        height = '77',
        number = '11',
        teamId = '2',
        year = 'Junior',
        position = 'SF'
    )
    player14 = Player(
        firstName="Maxi",
        lastName = 'Kleber',
        height = '82',
        number = '42',
        teamId = '2',
        year = 'Junior',
        position = 'PF'
    )
    player15 = Player(
        firstName="Javale",
        lastName = 'McGee',
        height = '84',
        number = '0',
        teamId = '2',
        year = 'Senior',
        position = 'C'
    )
    player16 = Player(
        firstName="Christian",
        lastName = 'Wood',
        height = '81',
        number = '35',
        teamId = '2',
        year = 'Sophomore',
        position = 'F'
    )
    player17 = Player(
        firstName="Lebron",
        lastName = 'James',
        height = '80',
        number = '6',
        teamId = '3',
        year = 'Freshman',
        position = 'F'
    )
    player18 = Player(
        firstName="Deron",
        lastName = 'Williams',
        height = '75',
        number = '7',
        teamId = '3',
        year = 'Freshman',
        position = 'G'
    )
    player19 = Player(
        firstName="Jason",
        lastName = 'Kidd',
        height = '76',
        number = '5',
        teamId = '3',
        year = 'Senior',
        position = 'G'
    )
    player20 = Player(
        firstName="Kobe",
        lastName = 'Bryant',
        height = '78',
        number = '10',
        teamId = '3',
        year = 'Junior',
        position = 'G'
    )
    player21 = Player(
        firstName="Dwight",
        lastName = 'Howard',
        height = '83',
        number = '11',
        teamId = '3',
        year = 'Freshman',
        position = 'C'
    )
    player22 = Player(
        firstName="Chris",
        lastName = 'Bosh',
        height = '83',
        number = '12',
        teamId = '3',
        year = 'Freshman',
        position = 'F/C'
    )
    player23 = Player(
        firstName="Chris",
        lastName = 'Paul',
        height = '72',
        number = '13',
        teamId = '3',
        year = 'Freshman',
        position = 'F'
    )
    player24 = Player(
        firstName="Carmelo",
        lastName = 'Anthony',
        height ='79',
        number = '15',
        teamId = '3',
        year = 'Freshman',
        position = 'F'
    )
    player25 = Player(
        firstName="Joe",
        lastName = 'Brown',
        height ='76',
        number = '0',
        teamId = '4',
        year = 'Senior',
        position = 'PF/C'
    )
    player26 = Player(
        firstName="Quantrez",
        lastName = 'Cooper',
        height ='71',
        number = '1',
        teamId = '4',
        year = 'Senior',
        position = 'PG'
    )
    player27 = Player(
        firstName="Milton",
        lastName = 'Turner',
        height ='72',
        number = '2',
        teamId = '4',
        year = 'Junior',
        position = 'SF'
    )
    player28 = Player(
        firstName="Tamarcus",
        lastName = 'Smith',
        height ='72',
        number = '3',
        teamId = '4',
        year = 'Junior',
        position = 'PG'
    )
    player29 = Player(
        firstName="Dre",
        lastName = 'Martin',
        height ='71',
        number = '5',
        teamId = '4',
        year = 'Senior',
        position = 'G'
    )
    player30 = Player(
        firstName="Braylon",
        lastName = 'Sanders',
        height ='75',
        number = '12',
        teamId = '4',
        year = 'Junior',
        position = 'G'
    )
    player31 = Player(
        firstName="Andrew",
        lastName = 'Kim',
        height ='73',
        number = '13',
        teamId = '4',
        year = 'Senior',
        position = 'G'
    )
    player32 = Player(
        firstName="Kedrick",
        lastName = 'Ramsey',
        height ='75',
        number = '15',
        teamId = '4',
        year = 'Sophomore',
        position = 'SF'
    )
    player33 = Player(
        firstName='Richard',
        lastName='Kwon',
        height='65',
        number='1',
        teamId='5',
        year='Senior',
        position='C'
    )



    db.session.add(player1)
    db.session.add(player2)
    db.session.add(player3)
    db.session.add(player4)
    db.session.add(player5)
    db.session.add(player6)
    db.session.add(player7)
    db.session.add(player8)
    db.session.add(player9)
    db.session.add(player10)
    db.session.add(player11)
    db.session.add(player12)
    db.session.add(player13)
    db.session.add(player14)
    db.session.add(player15)
    db.session.add(player16)
    db.session.add(player17)
    db.session.add(player18)
    db.session.add(player19)
    db.session.add(player20)
    db.session.add(player21)
    db.session.add(player22)
    db.session.add(player23)
    db.session.add(player24)
    db.session.add(player25)
    db.session.add(player26)
    db.session.add(player27)
    db.session.add(player28)
    db.session.add(player29)
    db.session.add(player30)
    db.session.add(player31)
    db.session.add(player32)
    db.session.add(player33)
    db.session.commit()

def undo_players():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM players")
    db.session.commit()
