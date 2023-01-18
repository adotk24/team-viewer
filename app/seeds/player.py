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
        firstName='Malcolm',
        lastName='Brogdon',
        height='76',
        number='13',
        teamId='5',
        year='Senior',
        position='PG'
    )
    player34 = Player(
        firstName='Jaylen',
        lastName='Brown',
        height='78',
        number='7',
        teamId='5',
        year='Sophomore',
        position='SG'
    )
    player35 = Player(
        firstName='Blake',
        lastName='Griffin',
        height='81',
        number='91',
        teamId='5',
        year='Senior',
        position='PF'
    )
    player36 = Player(
        firstName='Al',
        lastName='Horford',
        height='81',
        number='42',
        teamId='5',
        year='Senior',
        position='C'
    )
    player37 = Player(
        firstName='Payton',
        lastName='Pritchard',
        height='73',
        number='24',
        teamId='5',
        year='Freshman',
        position='PG'
    )
    player38 = Player(
        firstName='Marcus',
        lastName='Smart',
        height='76',
        number='36',
        teamId='5',
        year='Junior',
        position='PG'
    )
    player39 = Player(
        firstName='Jayson',
        lastName='Tatum',
        height='80',
        number='0',
        teamId='5',
        year='Sophomore',
        position='SF'
    )
    player40 = Player(
        firstName='Grant',
        lastName='Williams',
        height='78',
        number='12',
        teamId='5',
        year='Freshman',
        position='PF'
    )
    player41 = Player(
        firstName='Grayson',
        lastName='Allen',
        height='76',
        number='12',
        teamId='6',
        year='Sophomore',
        position='SG'
    )
    player42 = Player(
        firstName='Giannis',
        lastName='Antetokounmpo',
        height='83',
        number='34',
        teamId='6',
        year='Junior',
        position='PF'
    )
    player43 = Player(
        firstName='Pat',
        lastName='Connaughton',
        height='77',
        number='24',
        teamId='6',
        year='Junior',
        position='SG'
    )
    player44 = Player(
        firstName='George',
        lastName='Hill',
        height='76',
        number='3',
        teamId='6',
        year='Senior',
        position='PG'
    )
    player45 = Player(
        firstName='Jrue',
        lastName='Holiday',
        height='76',
        number='21',
        teamId='6',
        year='Junior',
        position='SG'
    )
    player46 = Player(
        firstName='Brook',
        lastName='Lopez',
        height='84',
        number='11',
        teamId='6',
        year='Senior',
        position='C'
    )
    player47 = Player(
        firstName='Serge',
        lastName='Ibaka',
        height='82',
        number='25',
        teamId='6',
        year='Senior',
        position='PF/C'
    )
    player48 = Player(
        firstName='Khris',
        lastName='Middleton',
        height='79',
        number='22',
        teamId='6',
        year='Junior',
        position='SF'
    )
    player49 = Player(
        firstName='Joel',
        lastName='Embiid',
        height='84',
        number='21',
        teamId='7',
        year='Junior',
        position='C'
    )
    player50 = Player(
        firstName='James',
        lastName='Harden',
        height='77',
        number='1',
        teamId='7',
        year='Junior',
        position='SG'
    )
    player51 = Player(
        firstName='Montrezl',
        lastName='Harrell',
        height='79',
        number='5',
        teamId='7',
        year='Sophomore',
        position='C'
    )
    player52 = Player(
        firstName='Tobias',
        lastName='Harris',
        height='79',
        number='12',
        teamId='7',
        year='Junior',
        position='PF'
    )
    player53 = Player(
        firstName='Furkan',
        lastName='Korkmaz',
        height='79',
        number='30',
        teamId='7',
        year='Sophomore',
        position='SG'
    )
    player54 = Player(
        firstName='Tyrese',
        lastName='Maxey',
        height='74',
        number='0',
        teamId='7',
        year='Freshman',
        position='PG'
    )
    player55 = Player(
        firstName='Matisse',
        lastName='Thybulle',
        height='77',
        number='22',
        teamId='7',
        year='Sophomore',
        position='SG'
    )
    player56 = Player(
        firstName='P.J.',
        lastName='Tucker',
        height='77',
        number='17',
        teamId='7',
        year='Senior',
        position='PF'
    )
    player57 = Player(
        firstName='Nic',
        lastName='Claxton',
        height='83',
        number='33',
        teamId='8',
        year='Freshman',
        position='C'
    )
    player58 = Player(
        firstName='Seth',
        lastName='Curry',
        height='73',
        number='30',
        teamId='8',
        year='Junior',
        position='SG'
    )
    player59 = Player(
        firstName='Kevin',
        lastName='Durant',
        height='82',
        number='35',
        teamId='8',
        year='Senior',
        position='PF'
    )
    player60 = Player(
        firstName='Kyrie',
        lastName='Irving',
        height='74',
        number='11',
        teamId='8',
        year='Junior',
        position='PG'
    )
    player61 = Player(
        firstName='Joe',
        lastName='Harris',
        height='78',
        number='12',
        teamId='8',
        year='Junior',
        position='SG'
    )
    player62 = Player(
        firstName='Ben',
        lastName='Simmons',
        height='82',
        number='10',
        teamId='8',
        year='Sophomore',
        position='PG'
    )
    player63 = Player(
        firstName='T.J.',
        lastName='Warren',
        height='80',
        number='1',
        teamId='8',
        year='Junior',
        position='SF'
    )
    player64 = Player(
        firstName='Yuta',
        lastName='Watanabe',
        height='80',
        number='18',
        teamId='8',
        year='Junior',
        position='SF'
    )
    player65 = Player(
        firstName='Christian',
        lastName='watanabe',
        height='78',
        number='0',
        teamId='9',
        year='Freshman',
        position='G'
    )
    player66 = Player(
        firstName='Kentavious',
        lastName='Caldwell',
        height='77',
        number='5',
        teamId='9',
        year='Junior',
        position='SG'
    )
    player67 = Player(
        firstName='Aaron',
        lastName='Gordon',
        height='80',
        number='50',
        teamId='9',
        year='Junior',
        position='PF'
    )
    player68 = Player(
        firstName='Nikola',
        lastName='Jokic',
        height='81',
        number='15',
        teamId='9',
        year='Junior',
        position='C'
    )
    player69 = Player(
        firstName='Jamal',
        lastName='Murray',
        height='76',
        number='27',
        teamId='9',
        year='Sophomore',
        position='PG'
    )
    player70 = Player(
        firstName='Michael',
        lastName='Porter Jr.',
        height='82',
        number='1',
        teamId='9',
        year='Freshman',
        position='SF'
    )
    player71 = Player(
        firstName='Deandre',
        lastName='Jordan',
        height='83',
        number='6',
        teamId='9',
        year='Senior',
        position='C'
    )
    player72 = Player(
        firstName='Bones',
        lastName='Hyland',
        height='74',
        number='3',
        teamId='9',
        year='Freshman',
        position='PG'
    )
    player73 = Player(
        firstName='RJ',
        lastName='Barrett',
        height='78',
        number='9',
        teamId='10',
        year='Freshman',
        position='SG'
    )
    player74 = Player(
        firstName='Jalen',
        lastName='Brunson',
        height='74',
        number='11',
        teamId='10',
        year='Sophomore',
        position='PG'
    )
    player75 = Player(
        firstName='Evan',
        lastName='fournier',
        height='78',
        number='13',
        teamId='10',
        year='Junior',
        position='SG'
    )
    player76 = Player(
        firstName='Quentin',
        lastName='Grimes',
        height='76',
        number='6',
        teamId='10',
        year='Freshman',
        position='SG'
    )
    player77 = Player(
        firstName='Immanuel',
        lastName='Quickley',
        height='75',
        number='5',
        teamId='10',
        year='Freshman',
        position='SG'
    )
    player78 = Player(
        firstName='Julius',
        lastName='Randle',
        height='80',
        number='30',
        teamId='10',
        year='Sophomore',
        position='PF'
    )
    player79 = Player(
        firstName='Cam',
        lastName='Reddish',
        height='80',
        number='0',
        teamId='10',
        year='Freshman',
        position='SF'
    )
    player80 = Player(
        firstName='Derrick',
        lastName='Rose',
        height='75',
        number='4',
        teamId='10',
        year='Senior',
        position='PG'
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
    db.session.add(player34)
    db.session.add(player35)
    db.session.add(player36)
    db.session.add(player37)
    db.session.add(player38)
    db.session.add(player39)
    db.session.add(player40)
    db.session.add(player41)
    db.session.add(player42)
    db.session.add(player43)
    db.session.add(player44)
    db.session.add(player45)
    db.session.add(player46)
    db.session.add(player47)
    db.session.add(player48)
    db.session.add(player49)
    db.session.add(player50)
    db.session.add(player51)
    db.session.add(player52)
    db.session.add(player53)
    db.session.add(player54)
    db.session.add(player55)
    db.session.add(player56)
    db.session.add(player57)
    db.session.add(player58)
    db.session.add(player59)
    db.session.add(player60)
    db.session.add(player61)
    db.session.add(player62)
    db.session.add(player63)
    db.session.add(player64)
    db.session.add(player65)
    db.session.add(player66)
    db.session.add(player67)
    db.session.add(player68)
    db.session.add(player69)
    db.session.add(player70)
    db.session.add(player71)
    db.session.add(player72)
    db.session.add(player73)
    db.session.add(player74)
    db.session.add(player75)
    db.session.add(player76)
    db.session.add(player77)
    db.session.add(player78)
    db.session.add(player79)
    db.session.add(player80)
    db.session.commit()

def undo_players():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM players")
    db.session.commit()
