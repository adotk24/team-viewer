from app.models import db, Stat, environment, SCHEMA

def seed_stats():
    stat1 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '1',
        points = '18',
        assists = '4',
        rebounds = '14'
    )
    stat2 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '1',
        points = '16',
        assists = '1',
        rebounds = '5'
    )
    stat3 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '1',
        points = '10',
        assists = '1',
        rebounds = '3'
    )
    stat4 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '1',
        points = '19',
        assists = '6',
        rebounds = '4'
    )
    stat5 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '1',
        points = '7',
        assists = '2',
        rebounds = '5'
    )
    stat6 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '1',
        points = '18',
        assists = '3',
        rebounds = '5'
    )
    stat7 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '1',
        points = '2',
        assists = '1',
        rebounds = '0'
    )
    stat8 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '1',
        points = '7',
        assists = '2',
        rebounds = '5'
    )
    stat9 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '2',
        points = '14',
        assists = '2',
        rebounds = '7'
    )
    stat10 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '2',
        points = '15',
        assists = '1',
        rebounds = '2'
    )
    stat11 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '2',
        points = '1',
        assists = '3',
        rebounds = '23'
    )
    stat12 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '2',
        points = '35',
        assists = '5',
        rebounds = '7'
    )
    stat13 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '2',
        points = '12',
        assists = '2',
        rebounds = '6'
    )
    stat14 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '2',
        points = '4',
        assists = '0',
        rebounds = '1'
    )
    stat15 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '2',
        points = '5',
        assists = '2',
        rebounds = '4'
    )
    stat16 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '2',
        points = '18',
        assists = '8',
        rebounds = '6'
    )
    stat17 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '3',
        points = '10',
        assists = '11',
        rebounds = '13'
    )
    stat18 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '3',
        points = '12',
        assists = '1',
        rebounds = '6'
    )
    stat19 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '3',
        points = '22',
        assists = '0',
        rebounds = '5'
    )
    stat20 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '3',
        points = '17',
        assists = '4',
        rebounds = '4'
    )
    stat21 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '3',
        points = '7',
        assists = '4',
        rebounds = '3'
    )
    stat22 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '3',
        points = '2',
        assists = '0',
        rebounds = '0'
    )
    stat23 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '3',
        points = '26',
        assists = '3',
        rebounds = '4'
    )
    # stat24 = Stat(
    #     teamid = '1',
    #     playerid = '8',
    #     gameid = '2',
    #     points = '15',
    #     assists = '1',
    #     rebounds = '2'
    # )
    stat25 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '4',
        points = '1',
        assists = '3',
        rebounds = '12'
    )
    stat26 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '4',
        points = '19',
        assists = '2',
        rebounds = '10'
    )
    stat27 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '4',
        points = '8',
        assists = '0',
        rebounds = '10'
    )
    stat28 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '4',
        points = '14',
        assists = '3',
        rebounds = '3'
    )
    stat29 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '4',
        points = '10',
        assists = '0',
        rebounds = '3'
    )
    stat30 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '4',
        points = '13',
        assists = '8',
        rebounds = '5'
    )
    stat31 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '4',
        points = '2',
        assists = '3',
        rebounds = '4'
    )
    stat32 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '4',
        points = '10',
        assists = '3',
        rebounds = '3'
    )
    stat33 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '5',
        points = '11',
        assists = '1',
        rebounds = '4'
    )
    stat34 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '5',
        points = '25',
        assists = '6',
        rebounds = '7'
    )
    stat35 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '5',
        points = '8',
        assists = '3',
        rebounds = '6'
    )
    stat36 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '5',
        points = '4',
        assists = '7',
        rebounds = '5'
    )
    stat37 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '5',
        points = '13',
        assists = '3',
        rebounds = '1'
    )
    stat38 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '5',
        points = '6',
        assists = '3',
        rebounds = '2'
    )
    stat39 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '5',
        points = '13',
        assists = '2',
        rebounds = '1'
    )
    stat40 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '5',
        points = '4',
        assists = '1',
        rebounds = '0'
    )
    stat41 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '6',
        points = '11',
        assists = '8',
        rebounds = '7'
    )
    stat42 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '6',
        points = '23',
        assists = '0',
        rebounds = '4'
    )
    stat43 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '6',
        points = '36',
        assists = '10',
        rebounds = '12'
    )
    stat44 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '6',
        points = '17',
        assists = '7',
        rebounds = '5'
    )
    stat45 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '6',
        points = '9',
        assists = '3',
        rebounds = '1'
    )
    stat46 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '6',
        points = '7',
        assists = '0',
        rebounds = '6'
    )
    stat47 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '6',
        points = '12',
        assists = '1',
        rebounds = '4'
    )
    stat48 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '6',
        points = '5',
        assists = '1',
        rebounds = '2'
    )
    stat49 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '7',
        points = '6',
        assists = '4',
        rebounds = '2'
    )
    stat50 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '7',
        points = '20',
        assists = '5',
        rebounds = '6'
    )
    stat51 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '7',
        points = '41',
        assists = '3',
        rebounds = '9'
    )
    stat52 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '7',
        points = '17',
        assists = '7',
        rebounds = '5'
    )
    stat53 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '7',
        points = '7',
        assists = '5',
        rebounds = '4'
    )
    stat54 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '7',
        points = '22',
        assists = '2',
        rebounds = '2'
    )
    stat55 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '7',
        points = '0',
        assists = '1',
        rebounds = '4'
    )
    stat56 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '7',
        points = '5',
        assists = '0',
        rebounds = '2'
    )
    stat57 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '8',
        points = '27',
        assists = '1',
        rebounds = '4'
    )
    stat58 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '8',
        points = '9',
        assists = '2',
        rebounds = '1'
    )
    stat59 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '8',
        points = '12',
        assists = '1',
        rebounds = '9'
    )
    stat60 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '8',
        points = '13',
        assists = '4',
        rebounds = '8'
    )
    stat61 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '8',
        points = '12',
        assists = '4',
        rebounds = '4'
    )
    stat62 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '8',
        points = '8',
        assists = '1',
        rebounds = '0'
    )
    stat63 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '8',
        points = '16',
        assists = '0',
        rebounds = '0'
    )
    stat64 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '8',
        points = '7',
        assists = '4',
        rebounds = '1'
    )
    stat65 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '9',
        points = '51',
        assists = '5',
        rebounds = '9'
    )
    stat66 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '9',
        points = '8',
        assists = '3',
        rebounds = '3'
    )
    stat67 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '9',
        points = '8',
        assists = '3',
        rebounds = '9'
    )
    stat68 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '9',
        points = '10',
        assists = '6',
        rebounds = '4'
    )
    stat69 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '9',
        points = '19',
        assists = '8',
        rebounds = '3'
    )
    stat70 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '9',
        points = '9',
        assists = '6',
        rebounds = '9'
    )
    stat71 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '9',
        points = '0',
        assists = '1',
        rebounds = '3'
    )
    stat72 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '9',
        points = '6',
        assists = '0',
        rebounds = '3'
    )
    stat73 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '1',
        points = '7',
        assists = '0',
        rebounds = '1'
    )
    stat74 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '1',
        points = '30',
        assists = '2',
        rebounds = '8'
    )
    stat75 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '1',
        points = '7',
        assists = '9',
        rebounds = '2'
    )
    stat76 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '1',
        points = '18',
        assists = '5',
        rebounds = '5'
    )
    stat77 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '1',
        points = '12',
        assists = '1',
        rebounds = '8'
    )
    stat78 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '1',
        points = '2',
        assists = '0',
        rebounds = '1'
    )
    stat79 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '1',
        points = '5',
        assists = '1',
        rebounds = '7'
    )
    stat80 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '1',
        points = '3',
        assists = '0',
        rebounds = '0'
    )
    stat81 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '10',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat82 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '10',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat83 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '10',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat84 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '10',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat85 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '10',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat86 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '10',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat87 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '10',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat88 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '10',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat89 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '11',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat90 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '11',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat91 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '11',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat92 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '11',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat93 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '11',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat94 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '11',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat95 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '11',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat96 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '11',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat97 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '12',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat98 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '12',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat99 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '12',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat100 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '12',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat101 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '12',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat102 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '12',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat103 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '12',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat104 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '12',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat105 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '13',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat106 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '13',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat107 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '13',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat108 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '13',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat109 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '13',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat110 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '13',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat111 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '13',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat112 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '13',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat113 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '14',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat114 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '14',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat115 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '14',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat116 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '14',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat117 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '14',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat118 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '14',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat119 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '14',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat120 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '14',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat113 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '15',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat114 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '15',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat115 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '15',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat116 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '15',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat117 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '15',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat118 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '15',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat119 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '15',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat120 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '15',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat121 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '16',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat122 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '16',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat123 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '16',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat124 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '16',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat125 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '16',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat126 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '16',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat127 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '16',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat128 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '16',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat129 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '17',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat130 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '17',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat131 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '17',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat132 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '17',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat133 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '17',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat134 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '17',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat135 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '17',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat136 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '17',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat137 = Stat(
        teamid = '3',
        playerid = '17',
        gameid = '2',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat138 = Stat(
        teamid = '3',
        playerid = '18',
        gameid = '2',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat139 = Stat(
        teamid = '3',
        playerid = '19',
        gameid = '2',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat140 = Stat(
        teamid = '3',
        playerid = '20',
        gameid = '2',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat141 = Stat(
        teamid = '3',
        playerid = '21',
        gameid = '2',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat142 = Stat(
        teamid = '3',
        playerid = '22',
        gameid = '2',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat143 = Stat(
        teamid = '3',
        playerid = '23',
        gameid = '2',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat144 = Stat(
        teamid = '3',
        playerid = '24',
        gameid = '2',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat145 = Stat(
        teamid = '3',
        playerid = '17',
        gameid = '10',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat146 = Stat(
        teamid = '3',
        playerid = '18',
        gameid = '10',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat147 = Stat(
        teamid = '3',
        playerid = '19',
        gameid = '10',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat148 = Stat(
        teamid = '3',
        playerid = '20',
        gameid = '10',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat149 = Stat(
        teamid = '3',
        playerid = '21',
        gameid = '10',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat150 = Stat(
        teamid = '3',
        playerid = '22',
        gameid = '10',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat151 = Stat(
        teamid = '3',
        playerid = '23',
        gameid = '10',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat152 = Stat(
        teamid = '3',
        playerid = '24',
        gameid = '10',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat153 = Stat(
        teamid = '3',
        playerid = '17',
        gameid = '18',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat154 = Stat(
        teamid = '3',
        playerid = '18',
        gameid = '18',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat155 = Stat(
        teamid = '3',
        playerid = '19',
        gameid = '18',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat156 = Stat(
        teamid = '3',
        playerid = '20',
        gameid = '18',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat157 = Stat(
        teamid = '3',
        playerid = '21',
        gameid = '18',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat158 = Stat(
        teamid = '3',
        playerid = '22',
        gameid = '18',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat159 = Stat(
        teamid = '3',
        playerid = '23',
        gameid = '18',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat160 = Stat(
        teamid = '3',
        playerid = '24',
        gameid = '18',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat161 = Stat(
        teamid = '3',
        playerid = '17',
        gameid = '19',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat162 = Stat(
        teamid = '3',
        playerid = '18',
        gameid = '19',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat163 = Stat(
        teamid = '3',
        playerid = '19',
        gameid = '19',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat164 = Stat(
        teamid = '3',
        playerid = '20',
        gameid = '19',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat165 = Stat(
        teamid = '3',
        playerid = '21',
        gameid = '19',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat166 = Stat(
        teamid = '3',
        playerid = '22',
        gameid = '19',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat167 = Stat(
        teamid = '3',
        playerid = '23',
        gameid = '19',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat168 = Stat(
        teamid = '3',
        playerid = '24',
        gameid = '19',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat169 = Stat(
        teamid = '3',
        playerid = '17',
        gameid = '20',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat170 = Stat(
        teamid = '3',
        playerid = '18',
        gameid = '20',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat171 = Stat(
        teamid = '3',
        playerid = '19',
        gameid = '20',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat172 = Stat(
        teamid = '3',
        playerid = '20',
        gameid = '20',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat173 = Stat(
        teamid = '3',
        playerid = '21',
        gameid = '20',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat174 = Stat(
        teamid = '3',
        playerid = '22',
        gameid = '20',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat175 = Stat(
        teamid = '3',
        playerid = '23',
        gameid = '20',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat176 = Stat(
        teamid = '3',
        playerid = '24',
        gameid = '20',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat177 = Stat(
        teamid = '3',
        playerid = '17',
        gameid = '21',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat178 = Stat(
        teamid = '3',
        playerid = '18',
        gameid = '21',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat179 = Stat(
        teamid = '3',
        playerid = '19',
        gameid = '21',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat180 = Stat(
        teamid = '3',
        playerid = '20',
        gameid = '21',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat181 = Stat(
        teamid = '3',
        playerid = '21',
        gameid = '21',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat182 = Stat(
        teamid = '3',
        playerid = '22',
        gameid = '21',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat183 = Stat(
        teamid = '3',
        playerid = '23',
        gameid = '21',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat184 = Stat(
        teamid = '3',
        playerid = '24',
        gameid = '21',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat185 = Stat(
        teamid = '3',
        playerid = '17',
        gameid = '22',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat186 = Stat(
        teamid = '3',
        playerid = '18',
        gameid = '22',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat187 = Stat(
        teamid = '3',
        playerid = '19',
        gameid = '22',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat188 = Stat(
        teamid = '3',
        playerid = '20',
        gameid = '22',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat189 = Stat(
        teamid = '3',
        playerid = '21',
        gameid = '22',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat190 = Stat(
        teamid = '3',
        playerid = '22',
        gameid = '22',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat191 = Stat(
        teamid = '3',
        playerid = '23',
        gameid = '22',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat192 = Stat(
        teamid = '3',
        playerid = '24',
        gameid = '22',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat193 = Stat(
        teamid = '3',
        playerid = '17',
        gameid = '23',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat194 = Stat(
        teamid = '3',
        playerid = '18',
        gameid = '23',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat195 = Stat(
        teamid = '3',
        playerid = '19',
        gameid = '23',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat196 = Stat(
        teamid = '3',
        playerid = '20',
        gameid = '23',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat197 = Stat(
        teamid = '3',
        playerid = '21',
        gameid = '23',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat198 = Stat(
        teamid = '3',
        playerid = '22',
        gameid = '23',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat199 = Stat(
        teamid = '3',
        playerid = '23',
        gameid = '23',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat200 = Stat(
        teamid = '3',
        playerid = '24',
        gameid = '23',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat201 = Stat(
        teamid = '3',
        playerid = '17',
        gameid = '24',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat202 = Stat(
        teamid = '3',
        playerid = '18',
        gameid = '24',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat203 = Stat(
        teamid = '3',
        playerid = '19',
        gameid = '24',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat204 = Stat(
        teamid = '3',
        playerid = '20',
        gameid = '24',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat205 = Stat(
        teamid = '3',
        playerid = '21',
        gameid = '24',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat206 = Stat(
        teamid = '3',
        playerid = '22',
        gameid = '24',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat207 = Stat(
        teamid = '3',
        playerid = '23',
        gameid = '24',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat208 = Stat(
        teamid = '3',
        playerid = '24',
        gameid = '24',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat209 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '3',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat210 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '3',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat211 = Stat(
        teamid = '4',
        playerid = '27',
        gameid = '3',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat212 = Stat(
        teamid = '4',
        playerid = '28',
        gameid = '3',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat213 = Stat(
        teamid = '4',
        playerid = '29',
        gameid = '3',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat214 = Stat(
        teamid = '4',
        playerid = '30',
        gameid = '3',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat215 = Stat(
        teamid = '4',
        playerid = '31',
        gameid = '3',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat216 = Stat(
        teamid = '4',
        playerid = '32',
        gameid = '3',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat217 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '11',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat218 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '11',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat219 = Stat(
        teamid = '4',
        playerid = '27',
        gameid = '11',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat220 = Stat(
        teamid = '4',
        playerid = '28',
        gameid = '11',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat221 = Stat(
        teamid = '4',
        playerid = '29',
        gameid = '11',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat222 = Stat(
        teamid = '4',
        playerid = '30',
        gameid = '11',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat223 = Stat(
        teamid = '4',
        playerid = '31',
        gameid = '11',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat224 = Stat(
        teamid = '4',
        playerid = '32',
        gameid = '11',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat225 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '18',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat226 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '18',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat227 = Stat(
        teamid = '4',
        playerid = '27',
        gameid = '18',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat228 = Stat(
        teamid = '4',
        playerid = '28',
        gameid = '18',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat229 = Stat(
        teamid = '4',
        playerid = '29',
        gameid = '18',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat230 = Stat(
        teamid = '4',
        playerid = '30',
        gameid = '18',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat231 = Stat(
        teamid = '4',
        playerid = '31',
        gameid = '18',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat232 = Stat(
        teamid = '4',
        playerid = '32',
        gameid = '18',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat233 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '25',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat234 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '25',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat235 = Stat(
        teamid = '4',
        playerid = '27',
        gameid = '25',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat236 = Stat(
        teamid = '4',
        playerid = '28',
        gameid = '25',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat237 = Stat(
        teamid = '4',
        playerid = '29',
        gameid = '25',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat238 = Stat(
        teamid = '4',
        playerid = '30',
        gameid = '25',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat239 = Stat(
        teamid = '4',
        playerid = '31',
        gameid = '25',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat240 = Stat(
        teamid = '4',
        playerid = '32',
        gameid = '25',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat241 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '26',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat242 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '26',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat243 = Stat(
        teamid = '4',
        playerid = '27',
        gameid = '26',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat244 = Stat(
        teamid = '4',
        playerid = '28',
        gameid = '26',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat245 = Stat(
        teamid = '4',
        playerid = '29',
        gameid = '26',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat246 = Stat(
        teamid = '4',
        playerid = '30',
        gameid = '26',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat247 = Stat(
        teamid = '4',
        playerid = '31',
        gameid = '26',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat248 = Stat(
        teamid = '4',
        playerid = '32',
        gameid = '26',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat249 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '27',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat250 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '27',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat251 = Stat(
        teamid = '4',
        playerid = '27',
        gameid = '27',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat252 = Stat(
        teamid = '4',
        playerid = '28',
        gameid = '27',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat253 = Stat(
        teamid = '4',
        playerid = '29',
        gameid = '27',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat254 = Stat(
        teamid = '4',
        playerid = '30',
        gameid = '27',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat255 = Stat(
        teamid = '4',
        playerid = '31',
        gameid = '27',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat256 = Stat(
        teamid = '4',
        playerid = '32',
        gameid = '27',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat257 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '28',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat258 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '28',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat259 = Stat(
        teamid = '4',
        playerid = '27',
        gameid = '28',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat260 = Stat(
        teamid = '4',
        playerid = '28',
        gameid = '28',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat261 = Stat(
        teamid = '4',
        playerid = '29',
        gameid = '28',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat262 = Stat(
        teamid = '4',
        playerid = '30',
        gameid = '28',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat263 = Stat(
        teamid = '4',
        playerid = '31',
        gameid = '28',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat264 = Stat(
        teamid = '4',
        playerid = '32',
        gameid = '28',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat265 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '29',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat266 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '29',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat267 = Stat(
        teamid = '4',
        playerid = '27',
        gameid = '29',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat268 = Stat(
        teamid = '4',
        playerid = '28',
        gameid = '29',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat269 = Stat(
        teamid = '4',
        playerid = '29',
        gameid = '29',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat270 = Stat(
        teamid = '4',
        playerid = '30',
        gameid = '29',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat271 = Stat(
        teamid = '4',
        playerid = '31',
        gameid = '29',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat272 = Stat(
        teamid = '4',
        playerid = '32',
        gameid = '29',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat273 = Stat(
        teamid = '4',
        playerid = '25',
        gameid = '30',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat274 = Stat(
        teamid = '4',
        playerid = '26',
        gameid = '30',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat275 = Stat(
        teamid = '4',
        playerid = '27',
        gameid = '30',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat276 = Stat(
        teamid = '4',
        playerid = '28',
        gameid = '30',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat277 = Stat(
        teamid = '4',
        playerid = '29',
        gameid = '30',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat278 = Stat(
        teamid = '4',
        playerid = '30',
        gameid = '30',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat279 = Stat(
        teamid = '4',
        playerid = '31',
        gameid = '30',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat280 = Stat(
        teamid = '4',
        playerid = '32',
        gameid = '30',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat281 = Stat(
        teamid = '5',
        playerid = '33',
        gameid = '4',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat282 = Stat(
        teamid = '5',
        playerid = '34',
        gameid = '4',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat283 = Stat(
        teamid = '5',
        playerid = '35',
        gameid = '4',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat284 = Stat(
        teamid = '5',
        playerid = '36',
        gameid = '4',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat285 = Stat(
        teamid = '5',
        playerid = '37',
        gameid = '4',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat286 = Stat(
        teamid = '5',
        playerid = '38',
        gameid = '4',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat287 = Stat(
        teamid = '5',
        playerid = '39',
        gameid = '4',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat288 = Stat(
        teamid = '5',
        playerid = '40',
        gameid = '4',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat289 = Stat(
        teamid = '5',
        playerid = '33',
        gameid = '12',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat290 = Stat(
        teamid = '5',
        playerid = '34',
        gameid = '12',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat291 = Stat(
        teamid = '5',
        playerid = '35',
        gameid = '12',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat292 = Stat(
        teamid = '5',
        playerid = '36',
        gameid = '12',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat293 = Stat(
        teamid = '5',
        playerid = '37',
        gameid = '12',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat294 = Stat(
        teamid = '5',
        playerid = '38',
        gameid = '12',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat295 = Stat(
        teamid = '5',
        playerid = '39',
        gameid = '12',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat296 = Stat(
        teamid = '5',
        playerid = '40',
        gameid = '12',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat297 = Stat(
        teamid = '5',
        playerid = '33',
        gameid = '19',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat298 = Stat(
        teamid = '5',
        playerid = '34',
        gameid = '19',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat299 = Stat(
        teamid = '5',
        playerid = '35',
        gameid = '19',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat300 = Stat(
        teamid = '5',
        playerid = '36',
        gameid = '19',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat301 = Stat(
        teamid = '5',
        playerid = '37',
        gameid = '19',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat302 = Stat(
        teamid = '5',
        playerid = '38',
        gameid = '19',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat303 = Stat(
        teamid = '5',
        playerid = '39',
        gameid = '19',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat304 = Stat(
        teamid = '5',
        playerid = '40',
        gameid = '19',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat305 = Stat(
        teamid = '5',
        playerid = '33',
        gameid = '25',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat306 = Stat(
        teamid = '5',
        playerid = '34',
        gameid = '25',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat307 = Stat(
        teamid = '5',
        playerid = '35',
        gameid = '25',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat308 = Stat(
        teamid = '5',
        playerid = '36',
        gameid = '25',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat309 = Stat(
        teamid = '5',
        playerid = '37',
        gameid = '25',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat310 = Stat(
        teamid = '5',
        playerid = '38',
        gameid = '25',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat311 = Stat(
        teamid = '5',
        playerid = '39',
        gameid = '25',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat312 = Stat(
        teamid = '5',
        playerid = '40',
        gameid = '25',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat313 = Stat(
        teamid = '5',
        playerid = '33',
        gameid = '31',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat314 = Stat(
        teamid = '5',
        playerid = '34',
        gameid = '31',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat315 = Stat(
        teamid = '5',
        playerid = '35',
        gameid = '31',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat316 = Stat(
        teamid = '5',
        playerid = '36',
        gameid = '31',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat317 = Stat(
        teamid = '5',
        playerid = '37',
        gameid = '31',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat318 = Stat(
        teamid = '5',
        playerid = '38',
        gameid = '31',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat319 = Stat(
        teamid = '5',
        playerid = '39',
        gameid = '31',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat320 = Stat(
        teamid = '5',
        playerid = '40',
        gameid = '31',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat321 = Stat(
        teamid = '5',
        playerid = '33',
        gameid = '32',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat322 = Stat(
        teamid = '5',
        playerid = '34',
        gameid = '32',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat323 = Stat(
        teamid = '5',
        playerid = '35',
        gameid = '32',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat324 = Stat(
        teamid = '5',
        playerid = '36',
        gameid = '32',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat325 = Stat(
        teamid = '5',
        playerid = '37',
        gameid = '32',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat326 = Stat(
        teamid = '5',
        playerid = '38',
        gameid = '32',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat327 = Stat(
        teamid = '5',
        playerid = '39',
        gameid = '32',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat328 = Stat(
        teamid = '5',
        playerid = '40',
        gameid = '32',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat329 = Stat(
        teamid = '5',
        playerid = '33',
        gameid = '33',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat330 = Stat(
        teamid = '5',
        playerid = '34',
        gameid = '33',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat331 = Stat(
        teamid = '5',
        playerid = '35',
        gameid = '33',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat332 = Stat(
        teamid = '5',
        playerid = '36',
        gameid = '33',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat333 = Stat(
        teamid = '5',
        playerid = '37',
        gameid = '33',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat334 = Stat(
        teamid = '5',
        playerid = '38',
        gameid = '33',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat335 = Stat(
        teamid = '5',
        playerid = '39',
        gameid = '33',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat336 = Stat(
        teamid = '5',
        playerid = '40',
        gameid = '33',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat337 = Stat(
        teamid = '5',
        playerid = '33',
        gameid = '34',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat338 = Stat(
        teamid = '5',
        playerid = '34',
        gameid = '34',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat339 = Stat(
        teamid = '5',
        playerid = '35',
        gameid = '34',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat340 = Stat(
        teamid = '5',
        playerid = '36',
        gameid = '34',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat341 = Stat(
        teamid = '5',
        playerid = '37',
        gameid = '34',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat342 = Stat(
        teamid = '5',
        playerid = '38',
        gameid = '34',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat343 = Stat(
        teamid = '5',
        playerid = '39',
        gameid = '34',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat344 = Stat(
        teamid = '5',
        playerid = '40',
        gameid = '34',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat345 = Stat(
        teamid = '5',
        playerid = '33',
        gameid = '35',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat346 = Stat(
        teamid = '5',
        playerid = '34',
        gameid = '35',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat347 = Stat(
        teamid = '5',
        playerid = '35',
        gameid = '35',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat348 = Stat(
        teamid = '5',
        playerid = '36',
        gameid = '35',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat349 = Stat(
        teamid = '5',
        playerid = '37',
        gameid = '35',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat350 = Stat(
        teamid = '5',
        playerid = '38',
        gameid = '35',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat351 = Stat(
        teamid = '5',
        playerid = '39',
        gameid = '35',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat352 = Stat(
        teamid = '5',
        playerid = '40',
        gameid = '35',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat353 = Stat(
        teamid = '6',
        playerid = '41',
        gameid = '5',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat354 = Stat(
        teamid = '6',
        playerid = '42',
        gameid = '5',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat355 = Stat(
        teamid = '6',
        playerid = '43',
        gameid = '5',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat356 = Stat(
        teamid = '6',
        playerid = '44',
        gameid = '5',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat357 = Stat(
        teamid = '6',
        playerid = '45',
        gameid = '5',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat358 = Stat(
        teamid = '6',
        playerid = '46',
        gameid = '5',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat359 = Stat(
        teamid = '6',
        playerid = '47',
        gameid = '5',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat360 = Stat(
        teamid = '6',
        playerid = '48',
        gameid = '5',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat361 = Stat(
        teamid = '6',
        playerid = '41',
        gameid = '13',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat362 = Stat(
        teamid = '6',
        playerid = '42',
        gameid = '13',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat363 = Stat(
        teamid = '6',
        playerid = '43',
        gameid = '13',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat364 = Stat(
        teamid = '6',
        playerid = '44',
        gameid = '13',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat365 = Stat(
        teamid = '6',
        playerid = '45',
        gameid = '13',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat366 = Stat(
        teamid = '6',
        playerid = '46',
        gameid = '13',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat367 = Stat(
        teamid = '6',
        playerid = '47',
        gameid = '13',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat368 = Stat(
        teamid = '6',
        playerid = '48',
        gameid = '13',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat369 = Stat(
        teamid = '6',
        playerid = '41',
        gameid = '20',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat370 = Stat(
        teamid = '6',
        playerid = '42',
        gameid = '20',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat371 = Stat(
        teamid = '6',
        playerid = '43',
        gameid = '20',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat372 = Stat(
        teamid = '6',
        playerid = '44',
        gameid = '20',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat373 = Stat(
        teamid = '6',
        playerid = '45',
        gameid = '20',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat374 = Stat(
        teamid = '6',
        playerid = '46',
        gameid = '20',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat375 = Stat(
        teamid = '6',
        playerid = '47',
        gameid = '20',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat376 = Stat(
        teamid = '6',
        playerid = '48',
        gameid = '20',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat377 = Stat(
        teamid = '6',
        playerid = '41',
        gameid = '26',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat378 = Stat(
        teamid = '6',
        playerid = '42',
        gameid = '26',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat379 = Stat(
        teamid = '6',
        playerid = '43',
        gameid = '26',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat380 = Stat(
        teamid = '6',
        playerid = '44',
        gameid = '26',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat381 = Stat(
        teamid = '6',
        playerid = '45',
        gameid = '26',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat382 = Stat(
        teamid = '6',
        playerid = '46',
        gameid = '26',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat383 = Stat(
        teamid = '6',
        playerid = '47',
        gameid = '26',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat384 = Stat(
        teamid = '6',
        playerid = '48',
        gameid = '26',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat385 = Stat(
        teamid = '6',
        playerid = '41',
        gameid = '31',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat386 = Stat(
        teamid = '6',
        playerid = '42',
        gameid = '31',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat387 = Stat(
        teamid = '6',
        playerid = '43',
        gameid = '31',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat388 = Stat(
        teamid = '6',
        playerid = '44',
        gameid = '31',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat389 = Stat(
        teamid = '6',
        playerid = '45',
        gameid = '31',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat390 = Stat(
        teamid = '6',
        playerid = '46',
        gameid = '31',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat391 = Stat(
        teamid = '6',
        playerid = '47',
        gameid = '31',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat392 = Stat(
        teamid = '6',
        playerid = '48',
        gameid = '31',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat393 = Stat(
        teamid = '6',
        playerid = '41',
        gameid = '36',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat394 = Stat(
        teamid = '6',
        playerid = '42',
        gameid = '36',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat395 = Stat(
        teamid = '6',
        playerid = '43',
        gameid = '36',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat396 = Stat(
        teamid = '6',
        playerid = '44',
        gameid = '36',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat397 = Stat(
        teamid = '6',
        playerid = '45',
        gameid = '36',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat398 = Stat(
        teamid = '6',
        playerid = '46',
        gameid = '36',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat399 = Stat(
        teamid = '6',
        playerid = '47',
        gameid = '36',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat400 = Stat(
        teamid = '6',
        playerid = '48',
        gameid = '36',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat401 = Stat(
        teamid = '6',
        playerid = '41',
        gameid = '37',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat402 = Stat(
        teamid = '6',
        playerid = '42',
        gameid = '37',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat403 = Stat(
        teamid = '6',
        playerid = '43',
        gameid = '37',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat404 = Stat(
        teamid = '6',
        playerid = '44',
        gameid = '37',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat405 = Stat(
        teamid = '6',
        playerid = '45',
        gameid = '37',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat406 = Stat(
        teamid = '6',
        playerid = '46',
        gameid = '37',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat407 = Stat(
        teamid = '6',
        playerid = '47',
        gameid = '37',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat408 = Stat(
        teamid = '6',
        playerid = '48',
        gameid = '37',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat409 = Stat(
        teamid = '6',
        playerid = '41',
        gameid = '38',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat410 = Stat(
        teamid = '6',
        playerid = '42',
        gameid = '38',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat411 = Stat(
        teamid = '6',
        playerid = '43',
        gameid = '38',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat412 = Stat(
        teamid = '6',
        playerid = '44',
        gameid = '38',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat413 = Stat(
        teamid = '6',
        playerid = '45',
        gameid = '38',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat414 = Stat(
        teamid = '6',
        playerid = '46',
        gameid = '38',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat415 = Stat(
        teamid = '6',
        playerid = '47',
        gameid = '38',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat416 = Stat(
        teamid = '6',
        playerid = '48',
        gameid = '38',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat417 = Stat(
        teamid = '6',
        playerid = '41',
        gameid = '39',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat418 = Stat(
        teamid = '6',
        playerid = '42',
        gameid = '39',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat419 = Stat(
        teamid = '6',
        playerid = '43',
        gameid = '39',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat420 = Stat(
        teamid = '6',
        playerid = '44',
        gameid = '39',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat421 = Stat(
        teamid = '6',
        playerid = '45',
        gameid = '39',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat422 = Stat(
        teamid = '6',
        playerid = '46',
        gameid = '39',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat423 = Stat(
        teamid = '6',
        playerid = '47',
        gameid = '39',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat424 = Stat(
        teamid = '6',
        playerid = '48',
        gameid = '39',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat425 = Stat(
        teamid = '7',
        playerid = '49',
        gameid = '6',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat426 = Stat(
        teamid = '7',
        playerid = '50',
        gameid = '6',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat427 = Stat(
        teamid = '7',
        playerid = '51',
        gameid = '6',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat428 = Stat(
        teamid = '7',
        playerid = '52',
        gameid = '6',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat429 = Stat(
        teamid = '7',
        playerid = '53',
        gameid = '5',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat430 = Stat(
        teamid = '7',
        playerid = '54',
        gameid = '6',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat431 = Stat(
        teamid = '7',
        playerid = '55',
        gameid = '6',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat432 = Stat(
        teamid = '7',
        playerid = '56',
        gameid = '6',
        points = '1',
        assists = '1',
        rebounds = '0'
    )

    stat433 = Stat(
        teamid = '7',
        playerid = '49',
        gameid = '14',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat434 = Stat(
        teamid = '7',
        playerid = '50',
        gameid = '14',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat435 = Stat(
        teamid = '7',
        playerid = '51',
        gameid = '14',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat436 = Stat(
        teamid = '7',
        playerid = '52',
        gameid = '14',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat437 = Stat(
        teamid = '7',
        playerid = '53',
        gameid = '14',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat438 = Stat(
        teamid = '7',
        playerid = '54',
        gameid = '14',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat439 = Stat(
        teamid = '7',
        playerid = '55',
        gameid = '14',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat440 = Stat(
        teamid = '7',
        playerid = '56',
        gameid = '14',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat441 = Stat(
        teamid = '7',
        playerid = '49',
        gameid = '21',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat442 = Stat(
        teamid = '7',
        playerid = '50',
        gameid = '21',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat443 = Stat(
        teamid = '7',
        playerid = '51',
        gameid = '21',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat444 = Stat(
        teamid = '7',
        playerid = '52',
        gameid = '21',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat445 = Stat(
        teamid = '7',
        playerid = '53',
        gameid = '21',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat446 = Stat(
        teamid = '7',
        playerid = '54',
        gameid = '21',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat447 = Stat(
        teamid = '7',
        playerid = '55',
        gameid = '21',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat448 = Stat(
        teamid = '7',
        playerid = '56',
        gameid = '21',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat449 = Stat(
        teamid = '7',
        playerid = '49',
        gameid = '27',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat450 = Stat(
        teamid = '7',
        playerid = '50',
        gameid = '27',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat451 = Stat(
        teamid = '7',
        playerid = '51',
        gameid = '27',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat452 = Stat(
        teamid = '7',
        playerid = '52',
        gameid = '27',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat453 = Stat(
        teamid = '7',
        playerid = '53',
        gameid = '27',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat454 = Stat(
        teamid = '7',
        playerid = '54',
        gameid = '27',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat455 = Stat(
        teamid = '7',
        playerid = '55',
        gameid = '27',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat456 = Stat(
        teamid = '7',
        playerid = '56',
        gameid = '27',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat457 = Stat(
        teamid = '7',
        playerid = '49',
        gameid = '32',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat458 = Stat(
        teamid = '7',
        playerid = '50',
        gameid = '32',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat459 = Stat(
        teamid = '7',
        playerid = '51',
        gameid = '32',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat460 = Stat(
        teamid = '7',
        playerid = '52',
        gameid = '32',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat461 = Stat(
        teamid = '7',
        playerid = '53',
        gameid = '32',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat462 = Stat(
        teamid = '7',
        playerid = '54',
        gameid = '32',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat463 = Stat(
        teamid = '7',
        playerid = '55',
        gameid = '32',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat464 = Stat(
        teamid = '7',
        playerid = '56',
        gameid = '32',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat465 = Stat(
        teamid = '7',
        playerid = '49',
        gameid = '36',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat466 = Stat(
        teamid = '7',
        playerid = '50',
        gameid = '36',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat467 = Stat(
        teamid = '7',
        playerid = '51',
        gameid = '36',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat468 = Stat(
        teamid = '7',
        playerid = '52',
        gameid = '36',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat469 = Stat(
        teamid = '7',
        playerid = '53',
        gameid = '36',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat470 = Stat(
        teamid = '7',
        playerid = '54',
        gameid = '36',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat471 = Stat(
        teamid = '7',
        playerid = '55',
        gameid = '36',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat472 = Stat(
        teamid = '7',
        playerid = '56',
        gameid = '36',
        points = '1',
        assists = '1',
        rebounds = '0'
    )


    stat497 = Stat(
        teamid = '8',
        playerid = '57',
        gameid = '7',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat498 = Stat(
        teamid = '8',
        playerid = '58',
        gameid = '7',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat499 = Stat(
        teamid = '8',
        playerid = '59',
        gameid = '7',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat500 = Stat(
        teamid = '8',
        playerid = '60',
        gameid = '7',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat501 = Stat(
        teamid = '8',
        playerid = '61',
        gameid = '7',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat502 = Stat(
        teamid = '8',
        playerid = '62',
        gameid = '7',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat503 = Stat(
        teamid = '8',
        playerid = '63',
        gameid = '7',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat504 = Stat(
        teamid = '8',
        playerid = '64',
        gameid = '7',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat505 = Stat(
        teamid = '8',
        playerid = '57',
        gameid = '15',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat506 = Stat(
        teamid = '8',
        playerid = '58',
        gameid = '15',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat507 = Stat(
        teamid = '8',
        playerid = '59',
        gameid = '15',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat508 = Stat(
        teamid = '8',
        playerid = '60',
        gameid = '15',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat509 = Stat(
        teamid = '8',
        playerid = '61',
        gameid = '15',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat510 = Stat(
        teamid = '8',
        playerid = '62',
        gameid = '15',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat511 = Stat(
        teamid = '8',
        playerid = '63',
        gameid = '15',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat512 = Stat(
        teamid = '8',
        playerid = '64',
        gameid = '15',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat513 = Stat(
        teamid = '8',
        playerid = '57',
        gameid = '22',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat514 = Stat(
        teamid = '8',
        playerid = '58',
        gameid = '22',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat515 = Stat(
        teamid = '8',
        playerid = '59',
        gameid = '22',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat516 = Stat(
        teamid = '8',
        playerid = '60',
        gameid = '22',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat517 = Stat(
        teamid = '8',
        playerid = '61',
        gameid = '22',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat518 = Stat(
        teamid = '8',
        playerid = '62',
        gameid = '22',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat519 = Stat(
        teamid = '8',
        playerid = '63',
        gameid = '22',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat520 = Stat(
        teamid = '8',
        playerid = '64',
        gameid = '22',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat521 = Stat(
        teamid = '8',
        playerid = '57',
        gameid = '28',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat522 = Stat(
        teamid = '8',
        playerid = '58',
        gameid = '28',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat523 = Stat(
        teamid = '8',
        playerid = '59',
        gameid = '28',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat524 = Stat(
        teamid = '8',
        playerid = '60',
        gameid = '28',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat525 = Stat(
        teamid = '8',
        playerid = '61',
        gameid = '28',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat526 = Stat(
        teamid = '8',
        playerid = '62',
        gameid = '28',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat527 = Stat(
        teamid = '8',
        playerid = '63',
        gameid = '28',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat528 = Stat(
        teamid = '8',
        playerid = '64',
        gameid = '28',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat529 = Stat(
        teamid = '8',
        playerid = '57',
        gameid = '33',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat530 = Stat(
        teamid = '8',
        playerid = '58',
        gameid = '33',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat531 = Stat(
        teamid = '8',
        playerid = '59',
        gameid = '33',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat532 = Stat(
        teamid = '8',
        playerid = '60',
        gameid = '33',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat533 = Stat(
        teamid = '8',
        playerid = '61',
        gameid = '33',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat534 = Stat(
        teamid = '8',
        playerid = '62',
        gameid = '33',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat535 = Stat(
        teamid = '8',
        playerid = '63',
        gameid = '33',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat536 = Stat(
        teamid = '8',
        playerid = '64',
        gameid = '33',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat537 = Stat(
        teamid = '8',
        playerid = '57',
        gameid = '37',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat538 = Stat(
        teamid = '8',
        playerid = '58',
        gameid = '37',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat539 = Stat(
        teamid = '8',
        playerid = '59',
        gameid = '37',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat540 = Stat(
        teamid = '8',
        playerid = '60',
        gameid = '37',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat541 = Stat(
        teamid = '8',
        playerid = '61',
        gameid = '37',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat542 = Stat(
        teamid = '8',
        playerid = '62',
        gameid = '37',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat543 = Stat(
        teamid = '8',
        playerid = '63',
        gameid = '37',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat544 = Stat(
        teamid = '8',
        playerid = '64',
        gameid = '37',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat545 = Stat(
        teamid = '8',
        playerid = '57',
        gameid = '40',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat546 = Stat(
        teamid = '8',
        playerid = '58',
        gameid = '40',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat547 = Stat(
        teamid = '8',
        playerid = '59',
        gameid = '40',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat548 = Stat(
        teamid = '8',
        playerid = '60',
        gameid = '40',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat549 = Stat(
        teamid = '8',
        playerid = '61',
        gameid = '40',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat550 = Stat(
        teamid = '8',
        playerid = '62',
        gameid = '40',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat551 = Stat(
        teamid = '8',
        playerid = '63',
        gameid = '40',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat552 = Stat(
        teamid = '8',
        playerid = '64',
        gameid = '40',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat553 = Stat(
        teamid = '8',
        playerid = '57',
        gameid = '43',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat554 = Stat(
        teamid = '8',
        playerid = '58',
        gameid = '43',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat555 = Stat(
        teamid = '8',
        playerid = '59',
        gameid = '43',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat556 = Stat(
        teamid = '8',
        playerid = '60',
        gameid = '43',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat557 = Stat(
        teamid = '8',
        playerid = '61',
        gameid = '43',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat558 = Stat(
        teamid = '8',
        playerid = '62',
        gameid = '43',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat559 = Stat(
        teamid = '8',
        playerid = '63',
        gameid = '43',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat560 = Stat(
        teamid = '8',
        playerid = '64',
        gameid = '43',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat561 = Stat(
        teamid = '8',
        playerid = '57',
        gameid = '44',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat562 = Stat(
        teamid = '8',
        playerid = '58',
        gameid = '44',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat563 = Stat(
        teamid = '8',
        playerid = '59',
        gameid = '44',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat564 = Stat(
        teamid = '8',
        playerid = '60',
        gameid = '44',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat565 = Stat(
        teamid = '8',
        playerid = '61',
        gameid = '44',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat566 = Stat(
        teamid = '8',
        playerid = '62',
        gameid = '44',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat567 = Stat(
        teamid = '8',
        playerid = '63',
        gameid = '44',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat568 = Stat(
        teamid = '8',
        playerid = '64',
        gameid = '44',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat569 = Stat(
        teamid = '7',
        playerid = '49',
        gameid = '40',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat570 = Stat(
        teamid = '7',
        playerid = '50',
        gameid = '40',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat571 = Stat(
        teamid = '7',
        playerid = '51',
        gameid = '40',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat572 = Stat(
        teamid = '7',
        playerid = '52',
        gameid = '40',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat573 = Stat(
        teamid = '7',
        playerid = '53',
        gameid = '40',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat574 = Stat(
        teamid = '7',
        playerid = '54',
        gameid = '40',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat575 = Stat(
        teamid = '7',
        playerid = '55',
        gameid = '40',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat576 = Stat(
        teamid = '7',
        playerid = '56',
        gameid = '40',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat577 = Stat(
        teamid = '7',
        playerid = '49',
        gameid = '41',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat578 = Stat(
        teamid = '7',
        playerid = '50',
        gameid = '41',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat579 = Stat(
        teamid = '7',
        playerid = '51',
        gameid = '41',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat580 = Stat(
        teamid = '7',
        playerid = '52',
        gameid = '41',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat581 = Stat(
        teamid = '7',
        playerid = '53',
        gameid = '41',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat582 = Stat(
        teamid = '7',
        playerid = '54',
        gameid = '41',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat583 = Stat(
        teamid = '7',
        playerid = '55',
        gameid = '41',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat584 = Stat(
        teamid = '7',
        playerid = '56',
        gameid = '41',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat585 = Stat(
        teamid = '7',
        playerid = '49',
        gameid = '42',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat586 = Stat(
        teamid = '7',
        playerid = '50',
        gameid = '42',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat587 = Stat(
        teamid = '7',
        playerid = '51',
        gameid = '42',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat588 = Stat(
        teamid = '7',
        playerid = '52',
        gameid = '42',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat589 = Stat(
        teamid = '7',
        playerid = '53',
        gameid = '42',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat590 = Stat(
        teamid = '7',
        playerid = '54',
        gameid = '42',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat591 = Stat(
        teamid = '7',
        playerid = '55',
        gameid = '42',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat592 = Stat(
        teamid = '7',
        playerid = '56',
        gameid = '42',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat593 = Stat(
        teamid = '2',
        playerid = '9',
        gameid = '14',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat594 = Stat(
        teamid = '2',
        playerid = '10',
        gameid = '14',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat595 = Stat(
        teamid = '2',
        playerid = '11',
        gameid = '14',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat596 = Stat(
        teamid = '2',
        playerid = '12',
        gameid = '14',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat597 = Stat(
        teamid = '2',
        playerid = '13',
        gameid = '14',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat598 = Stat(
        teamid = '2',
        playerid = '14',
        gameid = '14',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat599 = Stat(
        teamid = '2',
        playerid = '15',
        gameid = '14',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat600 = Stat(
        teamid = '2',
        playerid = '16',
        gameid = '14',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat601 = Stat(
        teamid = '9',
        playerid = '65',
        gameid = '8',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat602 = Stat(
        teamid = '9',
        playerid = '66',
        gameid = '8',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat603 = Stat(
        teamid = '9',
        playerid = '67',
        gameid = '8',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat604 = Stat(
        teamid = '9',
        playerid = '68',
        gameid = '8',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat605 = Stat(
        teamid = '9',
        playerid = '69',
        gameid = '8',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat606 = Stat(
        teamid = '9',
        playerid = '70',
        gameid = '8',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat607 = Stat(
        teamid = '9',
        playerid = '71',
        gameid = '8',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat608 = Stat(
        teamid = '9',
        playerid = '72',
        gameid = '8',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat609 = Stat(
        teamid = '9',
        playerid = '65',
        gameid = '16',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat610 = Stat(
        teamid = '9',
        playerid = '66',
        gameid = '16',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat611 = Stat(
        teamid = '9',
        playerid = '67',
        gameid = '16',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat612 = Stat(
        teamid = '9',
        playerid = '68',
        gameid = '16',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat613 = Stat(
        teamid = '9',
        playerid = '69',
        gameid = '16',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat614 = Stat(
        teamid = '9',
        playerid = '70',
        gameid = '16',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat615 = Stat(
        teamid = '9',
        playerid = '71',
        gameid = '16',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat616 = Stat(
        teamid = '9',
        playerid = '72',
        gameid = '16',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat617 = Stat(
        teamid = '9',
        playerid = '65',
        gameid = '23',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat618 = Stat(
        teamid = '9',
        playerid = '66',
        gameid = '23',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat619 = Stat(
        teamid = '9',
        playerid = '67',
        gameid = '23',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat620 = Stat(
        teamid = '9',
        playerid = '68',
        gameid = '23',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat621 = Stat(
        teamid = '9',
        playerid = '69',
        gameid = '23',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat622 = Stat(
        teamid = '9',
        playerid = '70',
        gameid = '23',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat623 = Stat(
        teamid = '9',
        playerid = '71',
        gameid = '23',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat624 = Stat(
        teamid = '9',
        playerid = '72',
        gameid = '23',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat625 = Stat(
        teamid = '9',
        playerid = '65',
        gameid = '29',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat626 = Stat(
        teamid = '9',
        playerid = '66',
        gameid = '29',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat627 = Stat(
        teamid = '9',
        playerid = '67',
        gameid = '29',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat628 = Stat(
        teamid = '9',
        playerid = '68',
        gameid = '29',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat629 = Stat(
        teamid = '9',
        playerid = '69',
        gameid = '29',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat630 = Stat(
        teamid = '9',
        playerid = '70',
        gameid = '29',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat631 = Stat(
        teamid = '9',
        playerid = '71',
        gameid = '29',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat632 = Stat(
        teamid = '9',
        playerid = '72',
        gameid = '29',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat633 = Stat(
        teamid = '9',
        playerid = '65',
        gameid = '34',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat634 = Stat(
        teamid = '9',
        playerid = '66',
        gameid = '34',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat635 = Stat(
        teamid = '9',
        playerid = '67',
        gameid = '34',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat636 = Stat(
        teamid = '9',
        playerid = '68',
        gameid = '34',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat637 = Stat(
        teamid = '9',
        playerid = '69',
        gameid = '34',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat638 = Stat(
        teamid = '9',
        playerid = '70',
        gameid = '34',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat639 = Stat(
        teamid = '9',
        playerid = '71',
        gameid = '34',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat640 = Stat(
        teamid = '9',
        playerid = '72',
        gameid = '34',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat641 = Stat(
        teamid = '9',
        playerid = '65',
        gameid = '38',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat642 = Stat(
        teamid = '9',
        playerid = '66',
        gameid = '38',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat643 = Stat(
        teamid = '9',
        playerid = '67',
        gameid = '38',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat644 = Stat(
        teamid = '9',
        playerid = '68',
        gameid = '38',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat645 = Stat(
        teamid = '9',
        playerid = '69',
        gameid = '38',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat646 = Stat(
        teamid = '9',
        playerid = '70',
        gameid = '38',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat647 = Stat(
        teamid = '9',
        playerid = '71',
        gameid = '38',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat648 = Stat(
        teamid = '9',
        playerid = '72',
        gameid = '38',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat649 = Stat(
        teamid = '9',
        playerid = '65',
        gameid = '41',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat650 = Stat(
        teamid = '9',
        playerid = '66',
        gameid = '41',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat651 = Stat(
        teamid = '9',
        playerid = '67',
        gameid = '41',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat652 = Stat(
        teamid = '9',
        playerid = '68',
        gameid = '41',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat653 = Stat(
        teamid = '9',
        playerid = '69',
        gameid = '41',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat654 = Stat(
        teamid = '9',
        playerid = '70',
        gameid = '41',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat655 = Stat(
        teamid = '9',
        playerid = '71',
        gameid = '41',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat656 = Stat(
        teamid = '9',
        playerid = '72',
        gameid = '41',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat657 = Stat(
        teamid = '9',
        playerid = '65',
        gameid = '43',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat658 = Stat(
        teamid = '9',
        playerid = '66',
        gameid = '43',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat659 = Stat(
        teamid = '9',
        playerid = '67',
        gameid = '43',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat660 = Stat(
        teamid = '9',
        playerid = '68',
        gameid = '43',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat661 = Stat(
        teamid = '9',
        playerid = '69',
        gameid = '43',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat662 = Stat(
        teamid = '9',
        playerid = '70',
        gameid = '43',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat663 = Stat(
        teamid = '9',
        playerid = '71',
        gameid = '43',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat664 = Stat(
        teamid = '9',
        playerid = '72',
        gameid = '45',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat665 = Stat(
        teamid = '9',
        playerid = '65',
        gameid = '45',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat666 = Stat(
        teamid = '9',
        playerid = '66',
        gameid = '45',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat667 = Stat(
        teamid = '9',
        playerid = '67',
        gameid = '45',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat668 = Stat(
        teamid = '9',
        playerid = '68',
        gameid = '45',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat669 = Stat(
        teamid = '9',
        playerid = '69',
        gameid = '45',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat670 = Stat(
        teamid = '9',
        playerid = '70',
        gameid = '45',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat671 = Stat(
        teamid = '9',
        playerid = '71',
        gameid = '45',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat672 = Stat(
        teamid = '9',
        playerid = '72',
        gameid = '45',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat673 = Stat(
        teamid = '10',
        playerid = '73',
        gameid = '9',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat674 = Stat(
        teamid = '10',
        playerid = '74',
        gameid = '9',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat675 = Stat(
        teamid = '10',
        playerid = '75',
        gameid = '9',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat676 = Stat(
        teamid = '10',
        playerid = '76',
        gameid = '9',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat677 = Stat(
        teamid = '10',
        playerid = '77',
        gameid = '9',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat678 = Stat(
        teamid = '10',
        playerid = '78',
        gameid = '9',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat679 = Stat(
        teamid = '10',
        playerid = '79',
        gameid = '9',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat680 = Stat(
        teamid = '10',
        playerid = '80',
        gameid = '9',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat681 = Stat(
        teamid = '10',
        playerid = '73',
        gameid = '17',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat682 = Stat(
        teamid = '10',
        playerid = '74',
        gameid = '17',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat683 = Stat(
        teamid = '10',
        playerid = '75',
        gameid = '17',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat684 = Stat(
        teamid = '10',
        playerid = '76',
        gameid = '17',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat685 = Stat(
        teamid = '10',
        playerid = '77',
        gameid = '17',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat686 = Stat(
        teamid = '10',
        playerid = '78',
        gameid = '17',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat687 = Stat(
        teamid = '10',
        playerid = '79',
        gameid = '17',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat688 = Stat(
        teamid = '10',
        playerid = '80',
        gameid = '17',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat689 = Stat(
        teamid = '10',
        playerid = '73',
        gameid = '24',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat690 = Stat(
        teamid = '10',
        playerid = '74',
        gameid = '24',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat691 = Stat(
        teamid = '10',
        playerid = '75',
        gameid = '24',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat692 = Stat(
        teamid = '10',
        playerid = '76',
        gameid = '24',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat693 = Stat(
        teamid = '10',
        playerid = '77',
        gameid = '24',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat694 = Stat(
        teamid = '10',
        playerid = '78',
        gameid = '24',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat695 = Stat(
        teamid = '10',
        playerid = '79',
        gameid = '24',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat696 = Stat(
        teamid = '10',
        playerid = '80',
        gameid = '24',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat697 = Stat(
        teamid = '10',
        playerid = '73',
        gameid = '30',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat698 = Stat(
        teamid = '10',
        playerid = '74',
        gameid = '30',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat699 = Stat(
        teamid = '10',
        playerid = '75',
        gameid = '30',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat700 = Stat(
        teamid = '10',
        playerid = '76',
        gameid = '30',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat701 = Stat(
        teamid = '10',
        playerid = '77',
        gameid = '30',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat702 = Stat(
        teamid = '10',
        playerid = '78',
        gameid = '30',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat703 = Stat(
        teamid = '10',
        playerid = '79',
        gameid = '30',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat704 = Stat(
        teamid = '10',
        playerid = '80',
        gameid = '30',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat705 = Stat(
        teamid = '10',
        playerid = '73',
        gameid = '35',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat706 = Stat(
        teamid = '10',
        playerid = '74',
        gameid = '35',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat707 = Stat(
        teamid = '10',
        playerid = '75',
        gameid = '35',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat708 = Stat(
        teamid = '10',
        playerid = '76',
        gameid = '35',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat709 = Stat(
        teamid = '10',
        playerid = '77',
        gameid = '35',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat710 = Stat(
        teamid = '10',
        playerid = '78',
        gameid = '35',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat711 = Stat(
        teamid = '10',
        playerid = '79',
        gameid = '35',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat712 = Stat(
        teamid = '10',
        playerid = '80',
        gameid = '35',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat713 = Stat(
        teamid = '10',
        playerid = '73',
        gameid = '39',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat714 = Stat(
        teamid = '10',
        playerid = '74',
        gameid = '39',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat715 = Stat(
        teamid = '10',
        playerid = '75',
        gameid = '39',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat716 = Stat(
        teamid = '10',
        playerid = '76',
        gameid = '39',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat717 = Stat(
        teamid = '10',
        playerid = '77',
        gameid = '39',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat718 = Stat(
        teamid = '10',
        playerid = '78',
        gameid = '39',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat719 = Stat(
        teamid = '10',
        playerid = '79',
        gameid = '39',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat720 = Stat(
        teamid = '10',
        playerid = '80',
        gameid = '39',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat721 = Stat(
        teamid = '10',
        playerid = '73',
        gameid = '42',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat722 = Stat(
        teamid = '10',
        playerid = '74',
        gameid = '42',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat723 = Stat(
        teamid = '10',
        playerid = '75',
        gameid = '42',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat724 = Stat(
        teamid = '10',
        playerid = '76',
        gameid = '42',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat725 = Stat(
        teamid = '10',
        playerid = '77',
        gameid = '42',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat726 = Stat(
        teamid = '10',
        playerid = '78',
        gameid = '42',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat727 = Stat(
        teamid = '10',
        playerid = '79',
        gameid = '42',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat728 = Stat(
        teamid = '10',
        playerid = '80',
        gameid = '42',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat729 = Stat(
        teamid = '10',
        playerid = '73',
        gameid = '44',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat730 = Stat(
        teamid = '10',
        playerid = '74',
        gameid = '44',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat731 = Stat(
        teamid = '10',
        playerid = '75',
        gameid = '44',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat732 = Stat(
        teamid = '10',
        playerid = '76',
        gameid = '44',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat733 = Stat(
        teamid = '10',
        playerid = '77',
        gameid = '44',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat734 = Stat(
        teamid = '10',
        playerid = '78',
        gameid = '44',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat735 = Stat(
        teamid = '10',
        playerid = '79',
        gameid = '44',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat736 = Stat(
        teamid = '10',
        playerid = '80',
        gameid = '44',
        points = '9',
        assists = '3',
        rebounds = '6'
    )
    stat737 = Stat(
        teamid = '10',
        playerid = '73',
        gameid = '45',
        points = '1',
        assists = '1',
        rebounds = '0'
    )
    stat738 = Stat(
        teamid = '10',
        playerid = '74',
        gameid = '45',
        points = '21',
        assists = '4',
        rebounds = '11'
    )
    stat739 = Stat(
        teamid = '10',
        playerid = '75',
        gameid = '45',
        points = '19',
        assists = '1',
        rebounds = '6'
    )
    stat740 = Stat(
        teamid = '10',
        playerid = '76',
        gameid = '45',
        points = '35',
        assists = '11',
        rebounds = '4'
    )
    stat741 = Stat(
        teamid = '10',
        playerid = '77',
        gameid = '45',
        points = '8',
        assists = '1',
        rebounds = '8'
    )
    stat742 = Stat(
        teamid = '10',
        playerid = '78',
        gameid = '45',
        points = '17',
        assists = '4',
        rebounds = '5'
    )
    stat743 = Stat(
        teamid = '10',
        playerid = '79',
        gameid = '45',
        points = '14',
        assists = '2',
        rebounds = '6'
    )
    stat744 = Stat(
        teamid = '10',
        playerid = '80',
        gameid = '45',
        points = '9',
        assists = '3',
        rebounds = '6'
    )











    db.session.add(stat1)
    db.session.add(stat2)
    db.session.add(stat3)
    db.session.add(stat4)
    db.session.add(stat5)
    db.session.add(stat6)
    db.session.add(stat7)
    db.session.add(stat8)
    db.session.add(stat9)
    db.session.add(stat10)
    db.session.add(stat11)
    db.session.add(stat12)
    db.session.add(stat13)
    db.session.add(stat14)
    db.session.add(stat15)
    db.session.add(stat16)
    db.session.add(stat17)
    db.session.add(stat18)
    db.session.add(stat19)
    db.session.add(stat20)
    db.session.add(stat21)
    db.session.add(stat22)
    db.session.add(stat23)
    db.session.add(stat25)
    db.session.add(stat26)
    db.session.add(stat27)
    db.session.add(stat28)
    db.session.add(stat29)
    db.session.add(stat30)
    db.session.add(stat31)
    db.session.add(stat32)
    db.session.add(stat33)
    db.session.add(stat34)
    db.session.add(stat35)
    db.session.add(stat36)
    db.session.add(stat37)
    db.session.add(stat38)
    db.session.add(stat39)
    db.session.add(stat40)
    db.session.add(stat41)
    db.session.add(stat42)
    db.session.add(stat43)
    db.session.add(stat44)
    db.session.add(stat45)
    db.session.add(stat46)
    db.session.add(stat47)
    db.session.add(stat48)
    db.session.add(stat49)
    db.session.add(stat50)
    db.session.add(stat51)
    db.session.add(stat52)
    db.session.add(stat53)
    db.session.add(stat54)
    db.session.add(stat55)
    db.session.add(stat56)
    db.session.add(stat57)
    db.session.add(stat58)
    db.session.add(stat59)
    db.session.add(stat60)
    db.session.add(stat61)
    db.session.add(stat62)
    db.session.add(stat63)
    db.session.add(stat64)
    db.session.add(stat65)
    db.session.add(stat67)
    db.session.add(stat68)
    db.session.add(stat69)
    db.session.add(stat70)
    db.session.add(stat71)
    db.session.add(stat72)
    db.session.add(stat73)
    db.session.add(stat74)
    db.session.add(stat75)
    db.session.add(stat76)
    db.session.add(stat77)
    db.session.add(stat78)
    db.session.add(stat79)
    db.session.add(stat80)
    db.session.add(stat81)
    db.session.add(stat82)
    db.session.add(stat83)
    db.session.add(stat84)
    db.session.add(stat85)
    db.session.add(stat86)
    db.session.add(stat87)
    db.session.add(stat88)
    db.session.add(stat89)
    db.session.add(stat90)
    db.session.add(stat91)
    db.session.add(stat92)
    db.session.add(stat93)
    db.session.add(stat94)
    db.session.add(stat95)
    db.session.add(stat96)
    db.session.add(stat97)
    db.session.add(stat98)
    db.session.add(stat99)
    db.session.add(stat100)
    db.session.add(stat101)
    db.session.add(stat102)
    db.session.add(stat103)
    db.session.add(stat104)
    db.session.add(stat105)
    db.session.add(stat106)
    db.session.add(stat107)
    db.session.add(stat108)
    db.session.add(stat109)
    db.session.add(stat110)
    db.session.add(stat111)
    db.session.add(stat112)
    db.session.add(stat113)
    db.session.add(stat114)
    db.session.add(stat115)
    db.session.add(stat116)
    db.session.add(stat117)
    db.session.add(stat118)
    db.session.add(stat119)
    db.session.add(stat120)
    db.session.add(stat121)
    db.session.add(stat122)
    db.session.add(stat123)
    db.session.add(stat124)
    db.session.add(stat125)
    db.session.add(stat126)
    db.session.add(stat127)
    db.session.add(stat128)
    db.session.add(stat129)
    db.session.add(stat130)
    db.session.add(stat131)
    db.session.add(stat132)
    db.session.add(stat133)
    db.session.add(stat134)
    db.session.add(stat135)
    db.session.add(stat137)
    db.session.add(stat138)
    db.session.add(stat139)
    db.session.add(stat140)
    db.session.add(stat141)
    db.session.add(stat142)
    db.session.add(stat143)
    db.session.add(stat144)
    db.session.add(stat145)
    db.session.add(stat146)
    db.session.add(stat147)
    db.session.add(stat148)
    db.session.add(stat149)
    db.session.add(stat150)
    db.session.add(stat151)
    db.session.add(stat152)
    db.session.add(stat153)
    db.session.add(stat154)
    db.session.add(stat155)
    db.session.add(stat156)
    db.session.add(stat157)
    db.session.add(stat158)
    db.session.add(stat159)
    db.session.add(stat160)
    db.session.add(stat161)
    db.session.add(stat162)
    db.session.add(stat163)
    db.session.add(stat164)
    db.session.add(stat165)
    db.session.add(stat166)
    db.session.add(stat167)
    db.session.add(stat168)
    db.session.add(stat169)
    db.session.add(stat170)
    db.session.add(stat171)
    db.session.add(stat172)
    db.session.add(stat173)
    db.session.add(stat174)
    db.session.add(stat175)
    db.session.add(stat176)
    db.session.add(stat177)
    db.session.add(stat178)
    db.session.add(stat179)
    db.session.add(stat180)
    db.session.add(stat181)
    db.session.add(stat182)
    db.session.add(stat183)
    db.session.add(stat184)
    db.session.add(stat185)
    db.session.add(stat186)
    db.session.add(stat187)
    db.session.add(stat188)
    db.session.add(stat189)
    db.session.add(stat190)
    db.session.add(stat191)
    db.session.add(stat192)
    db.session.add(stat193)
    db.session.add(stat194)
    db.session.add(stat195)
    db.session.add(stat196)
    db.session.add(stat197)
    db.session.add(stat198)
    db.session.add(stat199)
    db.session.add(stat200)
    db.session.add(stat201)
    db.session.add(stat202)
    db.session.add(stat203)
    db.session.add(stat204)
    db.session.add(stat205)
    db.session.add(stat206)
    db.session.add(stat207)
    db.session.add(stat208)
    db.session.add(stat209)
    db.session.add(stat210)
    db.session.add(stat211)
    db.session.add(stat212)
    db.session.add(stat213)
    db.session.add(stat214)
    db.session.add(stat215)
    db.session.add(stat216)
    db.session.add(stat217)
    db.session.add(stat218)
    db.session.add(stat219)
    db.session.add(stat220)
    db.session.add(stat221)
    db.session.add(stat222)
    db.session.add(stat223)
    db.session.add(stat224)
    db.session.add(stat225)
    db.session.add(stat226)
    db.session.add(stat227)
    db.session.add(stat228)
    db.session.add(stat229)
    db.session.add(stat230)
    db.session.add(stat231)
    db.session.add(stat232)
    db.session.add(stat233)
    db.session.add(stat234)
    db.session.add(stat235)
    db.session.add(stat236)
    db.session.add(stat237)
    db.session.add(stat238)
    db.session.add(stat239)
    db.session.add(stat240)
    db.session.add(stat241)
    db.session.add(stat242)
    db.session.add(stat243)
    db.session.add(stat244)
    db.session.add(stat245)
    db.session.add(stat246)
    db.session.add(stat247)
    db.session.add(stat248)
    db.session.add(stat249)
    db.session.add(stat250)
    db.session.add(stat251)
    db.session.add(stat252)
    db.session.add(stat253)
    db.session.add(stat254)
    db.session.add(stat255)
    db.session.add(stat256)
    db.session.add(stat257)
    db.session.add(stat258)
    db.session.add(stat259)
    db.session.add(stat260)
    db.session.add(stat261)
    db.session.add(stat262)
    db.session.add(stat263)
    db.session.add(stat264)
    db.session.add(stat265)
    db.session.add(stat266)
    db.session.add(stat267)
    db.session.add(stat268)
    db.session.add(stat269)
    db.session.add(stat270)
    db.session.add(stat271)
    db.session.add(stat272)
    db.session.add(stat273)
    db.session.add(stat274)
    db.session.add(stat275)
    db.session.add(stat276)
    db.session.add(stat277)
    db.session.add(stat278)
    db.session.add(stat279)
    db.session.add(stat280)
    db.session.add(stat281)
    db.session.add(stat282)
    db.session.add(stat283)
    db.session.add(stat284)
    db.session.add(stat285)
    db.session.add(stat286)
    db.session.add(stat287)
    db.session.add(stat288)
    db.session.add(stat289)
    db.session.add(stat290)
    db.session.add(stat291)
    db.session.add(stat292)
    db.session.add(stat293)
    db.session.add(stat294)
    db.session.add(stat295)
    db.session.add(stat296)
    db.session.add(stat297)
    db.session.add(stat298)
    db.session.add(stat299)
    db.session.add(stat300)
    db.session.add(stat301)
    db.session.add(stat302)
    db.session.add(stat303)
    db.session.add(stat304)
    db.session.add(stat305)
    db.session.add(stat306)
    db.session.add(stat307)
    db.session.add(stat308)
    db.session.add(stat309)
    db.session.add(stat310)
    db.session.add(stat311)
    db.session.add(stat312)
    db.session.add(stat313)
    db.session.add(stat314)
    db.session.add(stat315)
    db.session.add(stat316)
    db.session.add(stat317)
    db.session.add(stat318)
    db.session.add(stat319)
    db.session.add(stat320)
    db.session.add(stat321)
    db.session.add(stat322)
    db.session.add(stat323)
    db.session.add(stat324)
    db.session.add(stat325)
    db.session.add(stat326)
    db.session.add(stat327)
    db.session.add(stat328)
    db.session.add(stat329)
    db.session.add(stat330)
    db.session.add(stat331)
    db.session.add(stat332)
    db.session.add(stat333)
    db.session.add(stat334)
    db.session.add(stat335)
    db.session.add(stat336)
    db.session.add(stat337)
    db.session.add(stat338)
    db.session.add(stat339)
    db.session.add(stat340)
    db.session.add(stat341)
    db.session.add(stat342)
    db.session.add(stat343)
    db.session.add(stat344)
    db.session.add(stat345)
    db.session.add(stat346)
    db.session.add(stat347)
    db.session.add(stat348)
    db.session.add(stat349)
    db.session.add(stat350)
    db.session.add(stat351)
    db.session.add(stat352)
    db.session.add(stat353)
    db.session.add(stat354)
    db.session.add(stat355)
    db.session.add(stat356)
    db.session.add(stat357)
    db.session.add(stat358)
    db.session.add(stat359)
    db.session.add(stat360)
    db.session.add(stat361)
    db.session.add(stat362)
    db.session.add(stat363)
    db.session.add(stat364)
    db.session.add(stat365)
    db.session.add(stat366)
    db.session.add(stat367)
    db.session.add(stat368)
    db.session.add(stat369)
    db.session.add(stat370)
    db.session.add(stat371)
    db.session.add(stat372)
    db.session.add(stat373)
    db.session.add(stat374)
    db.session.add(stat375)
    db.session.add(stat376)
    db.session.add(stat377)
    db.session.add(stat378)
    db.session.add(stat379)
    db.session.add(stat380)
    db.session.add(stat381)
    db.session.add(stat382)
    db.session.add(stat383)
    db.session.add(stat384)
    db.session.add(stat385)
    db.session.add(stat386)
    db.session.add(stat387)
    db.session.add(stat388)
    db.session.add(stat389)
    db.session.add(stat390)
    db.session.add(stat391)
    db.session.add(stat392)
    db.session.add(stat393)
    db.session.add(stat394)
    db.session.add(stat395)
    db.session.add(stat396)
    db.session.add(stat397)
    db.session.add(stat398)
    db.session.add(stat399)
    db.session.add(stat400)
    db.session.add(stat401)
    db.session.add(stat402)
    db.session.add(stat403)
    db.session.add(stat404)
    db.session.add(stat405)
    db.session.add(stat406)
    db.session.add(stat407)
    db.session.add(stat408)
    db.session.add(stat409)
    db.session.add(stat410)
    db.session.add(stat411)
    db.session.add(stat412)
    db.session.add(stat413)
    db.session.add(stat414)
    db.session.add(stat415)
    db.session.add(stat416)
    db.session.add(stat417)
    db.session.add(stat418)
    db.session.add(stat419)
    db.session.add(stat420)
    db.session.add(stat421)
    db.session.add(stat422)
    db.session.add(stat423)
    db.session.add(stat424)
    db.session.add(stat425)
    db.session.add(stat426)
    db.session.add(stat427)
    db.session.add(stat428)
    db.session.add(stat429)
    db.session.add(stat430)
    db.session.add(stat431)
    db.session.add(stat432)
    db.session.add(stat433)
    db.session.add(stat434)
    db.session.add(stat435)
    db.session.add(stat436)
    db.session.add(stat437)
    db.session.add(stat438)
    db.session.add(stat439)
    db.session.add(stat440)
    db.session.add(stat441)
    db.session.add(stat442)
    db.session.add(stat443)
    db.session.add(stat444)
    db.session.add(stat445)
    db.session.add(stat446)
    db.session.add(stat447)
    db.session.add(stat448)
    db.session.add(stat449)
    db.session.add(stat450)
    db.session.add(stat451)
    db.session.add(stat452)
    db.session.add(stat453)
    db.session.add(stat454)
    db.session.add(stat455)
    db.session.add(stat456)
    db.session.add(stat457)
    db.session.add(stat458)
    db.session.add(stat459)
    db.session.add(stat460)
    db.session.add(stat461)
    db.session.add(stat462)
    db.session.add(stat463)
    db.session.add(stat464)
    db.session.add(stat465)
    db.session.add(stat466)
    db.session.add(stat467)
    db.session.add(stat468)
    db.session.add(stat469)
    db.session.add(stat470)
    db.session.add(stat471)
    db.session.add(stat472)
    db.session.add(stat497)
    db.session.add(stat498)
    db.session.add(stat499)
    db.session.add(stat500)
    db.session.add(stat501)
    db.session.add(stat502)
    db.session.add(stat503)
    db.session.add(stat504)
    db.session.add(stat505)
    db.session.add(stat506)
    db.session.add(stat507)
    db.session.add(stat508)
    db.session.add(stat509)
    db.session.add(stat510)
    db.session.add(stat511)
    db.session.add(stat512)
    db.session.add(stat513)
    db.session.add(stat514)
    db.session.add(stat515)
    db.session.add(stat516)
    db.session.add(stat517)
    db.session.add(stat518)
    db.session.add(stat519)
    db.session.add(stat520)
    db.session.add(stat521)
    db.session.add(stat522)
    db.session.add(stat523)
    db.session.add(stat524)
    db.session.add(stat525)
    db.session.add(stat526)
    db.session.add(stat527)
    db.session.add(stat528)
    db.session.add(stat529)
    db.session.add(stat530)
    db.session.add(stat531)
    db.session.add(stat532)
    db.session.add(stat533)
    db.session.add(stat534)
    db.session.add(stat535)
    db.session.add(stat536)
    db.session.add(stat537)
    db.session.add(stat538)
    db.session.add(stat539)
    db.session.add(stat540)
    db.session.add(stat541)
    db.session.add(stat542)
    db.session.add(stat543)
    db.session.add(stat544)
    db.session.add(stat545)
    db.session.add(stat546)
    db.session.add(stat547)
    db.session.add(stat548)
    db.session.add(stat549)
    db.session.add(stat550)
    db.session.add(stat551)
    db.session.add(stat552)
    db.session.add(stat553)
    db.session.add(stat554)
    db.session.add(stat555)
    db.session.add(stat556)
    db.session.add(stat557)
    db.session.add(stat558)
    db.session.add(stat559)
    db.session.add(stat560)
    db.session.add(stat561)
    db.session.add(stat562)
    db.session.add(stat563)
    db.session.add(stat564)
    db.session.add(stat565)
    db.session.add(stat566)
    db.session.add(stat567)
    db.session.add(stat568)
    db.session.add(stat569)
    db.session.add(stat570)
    db.session.add(stat571)
    db.session.add(stat572)
    db.session.add(stat573)
    db.session.add(stat574)
    db.session.add(stat575)
    db.session.add(stat576)
    db.session.add(stat577)
    db.session.add(stat578)
    db.session.add(stat579)
    db.session.add(stat580)
    db.session.add(stat581)
    db.session.add(stat582)
    db.session.add(stat583)
    db.session.add(stat584)
    db.session.add(stat585)
    db.session.add(stat586)
    db.session.add(stat587)
    db.session.add(stat588)
    db.session.add(stat589)
    db.session.add(stat590)
    db.session.add(stat591)
    db.session.add(stat592)
    db.session.add(stat593)
    db.session.add(stat594)
    db.session.add(stat595)
    db.session.add(stat596)
    db.session.add(stat597)
    db.session.add(stat598)
    db.session.add(stat599)
    db.session.add(stat600)
    db.session.add(stat601)
    db.session.add(stat602)
    db.session.add(stat603)
    db.session.add(stat604)
    db.session.add(stat605)
    db.session.add(stat606)
    db.session.add(stat607)
    db.session.add(stat608)
    db.session.add(stat609)
    db.session.add(stat610)
    db.session.add(stat611)
    db.session.add(stat612)
    db.session.add(stat613)
    db.session.add(stat614)
    db.session.add(stat615)
    db.session.add(stat616)
    db.session.add(stat617)
    db.session.add(stat618)
    db.session.add(stat619)
    db.session.add(stat620)
    db.session.add(stat621)
    db.session.add(stat622)
    db.session.add(stat623)
    db.session.add(stat624)
    db.session.add(stat625)
    db.session.add(stat626)
    db.session.add(stat627)
    db.session.add(stat628)
    db.session.add(stat629)
    db.session.add(stat630)
    db.session.add(stat631)
    db.session.add(stat632)
    db.session.add(stat633)
    db.session.add(stat634)
    db.session.add(stat635)
    db.session.add(stat636)
    db.session.add(stat637)
    db.session.add(stat638)
    db.session.add(stat639)
    db.session.add(stat640)
    db.session.add(stat641)
    db.session.add(stat642)
    db.session.add(stat643)
    db.session.add(stat644)
    db.session.add(stat645)
    db.session.add(stat646)
    db.session.add(stat647)
    db.session.add(stat648)
    db.session.add(stat649)
    db.session.add(stat650)
    db.session.add(stat651)
    db.session.add(stat652)
    db.session.add(stat653)
    db.session.add(stat654)
    db.session.add(stat655)
    db.session.add(stat656)
    db.session.add(stat657)
    db.session.add(stat658)
    db.session.add(stat659)
    db.session.add(stat660)
    db.session.add(stat661)
    db.session.add(stat662)
    db.session.add(stat663)
    db.session.add(stat664)
    db.session.add(stat665)
    db.session.add(stat666)
    db.session.add(stat667)
    db.session.add(stat668)
    db.session.add(stat669)
    db.session.add(stat670)
    db.session.add(stat671)
    db.session.add(stat672)
    db.session.add(stat673)
    db.session.add(stat674)
    db.session.add(stat675)
    db.session.add(stat676)
    db.session.add(stat677)
    db.session.add(stat678)
    db.session.add(stat679)
    db.session.add(stat680)
    db.session.add(stat681)
    db.session.add(stat682)
    db.session.add(stat683)
    db.session.add(stat684)
    db.session.add(stat685)
    db.session.add(stat686)
    db.session.add(stat687)
    db.session.add(stat688)
    db.session.add(stat689)
    db.session.add(stat690)
    db.session.add(stat691)
    db.session.add(stat692)
    db.session.add(stat693)
    db.session.add(stat694)
    db.session.add(stat695)
    db.session.add(stat696)
    db.session.add(stat697)
    db.session.add(stat698)
    db.session.add(stat699)
    db.session.add(stat700)
    db.session.add(stat701)
    db.session.add(stat702)
    db.session.add(stat703)
    db.session.add(stat704)
    db.session.add(stat705)
    db.session.add(stat706)
    db.session.add(stat707)
    db.session.add(stat708)
    db.session.add(stat709)
    db.session.add(stat710)
    db.session.add(stat711)
    db.session.add(stat712)
    db.session.add(stat713)
    db.session.add(stat714)
    db.session.add(stat715)
    db.session.add(stat716)
    db.session.add(stat717)
    db.session.add(stat718)
    db.session.add(stat719)
    db.session.add(stat720)
    db.session.add(stat721)
    db.session.add(stat722)
    db.session.add(stat723)
    db.session.add(stat724)
    db.session.add(stat725)
    db.session.add(stat726)
    db.session.add(stat727)
    db.session.add(stat728)
    db.session.add(stat729)
    db.session.add(stat730)
    db.session.add(stat731)
    db.session.add(stat732)
    db.session.add(stat733)
    db.session.add(stat734)
    db.session.add(stat735)
    db.session.add(stat736)
    db.session.add(stat737)
    db.session.add(stat738)
    db.session.add(stat739)
    db.session.add(stat740)
    db.session.add(stat741)
    db.session.add(stat742)
    db.session.add(stat743)
    db.session.add(stat744)


    db.session.commit()

def undo_stats():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.stats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM stats")
    db.session.commit()
