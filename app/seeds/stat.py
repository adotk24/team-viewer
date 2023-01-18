from app.models import db, Stat, environment, SCHEMA

def seed_stats():
    stat1 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '1',
        points = '23',
        assists = '3',
        rebounds = '9'
    )
    stat2 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '1',
        points = '5',
        assists = '2',
        rebounds = '3'
    )
    stat3 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '1',
        points = '14',
        assists = '5',
        rebounds = '13'
    )
    stat4 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '1',
        points = '39',
        assists = '7',
        rebounds = '9'
    )
    stat5 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '1',
        points = '28',
        assists = '2',
        rebounds = '3'
    )
    stat6 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '1',
        points = '0',
        assists = '1',
        rebounds = '5'
    )
    stat7 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '1',
        points = '2',
        assists = '0',
        rebounds = '1'
    )
    stat8 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '1',
        points = '11',
        assists = '0',
        rebounds = '7'
    )
    stat9 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '2',
        points = '12',
        assists = '1',
        rebounds = '12'
    )
    stat10 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '2',
        points = '19',
        assists = '1',
        rebounds = '1'
    )
    stat11 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '2',
        points = '37',
        assists = '7',
        rebounds = '6'
    )
    stat12 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '2',
        points = '10',
        assists = '3',
        rebounds = '8'
    )
    stat13 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '2',
        points = '25',
        assists = '1',
        rebounds = '5'
    )
    stat14 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '2',
        points = '7',
        assists = '0',
        rebounds = '3'
    )
    stat15 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '2',
        points = '5',
        assists = '1',
        rebounds = '0'
    )
    stat16 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '2',
        points = '0',
        assists = '0',
        rebounds = '1'
    )
    stat17 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '3',
        points = '5',
        assists = '0',
        rebounds = '2'
    )
    stat18 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '3',
        points = '0',
        assists = '1',
        rebounds = '1'
    )
    stat19 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '3',
        points = '15',
        assists = '4',
        rebounds = '11'
    )
    stat20 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '3',
        points = '10',
        assists = '11',
        rebounds = '10'
    )
    stat21 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '3',
        points = '16',
        assists = '2',
        rebounds = '7'
    )
    stat22 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '3',
        points = '4',
        assists = '2',
        rebounds = '3'
    )
    stat23 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '3',
        points = '19',
        assists = '0',
        rebounds = '5'
    )
    stat24 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '2',
        points = '15',
        assists = '1',
        rebounds = '2'
    )
    stat25 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '4',
        points = '16',
        assists = '2',
        rebounds = '4'
    )
    stat26 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '4',
        points = '36',
        assists = '11',
        rebounds = '10'
    )
    stat27 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '4',
        points = '12',
        assists = '3',
        rebounds = '8'
    )
    stat28 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '4',
        points = '13',
        assists = '5',
        rebounds = '4'
    )
    stat29 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '4',
        points = '2',
        assists = '2',
        rebounds = '4'
    )
    stat30 = Stat(
        teamid = '1',
        playerid = '6',
        gameid = '4',
        points = '6',
        assists = '2',
        rebounds = '7'
    )
    stat31 = Stat(
        teamid = '1',
        playerid = '7',
        gameid = '4',
        points = '4',
        assists = '3',
        rebounds = '4'
    )
    stat32 = Stat(
        teamid = '1',
        playerid = '8',
        gameid = '4',
        points = '2',
        assists = '2',
        rebounds = '2'
    )
    stat33 = Stat(
        teamid = '1',
        playerid = '1',
        gameid = '5',
        points = '18',
        assists = '2',
        rebounds = '4'
    )
    stat34 = Stat(
        teamid = '1',
        playerid = '2',
        gameid = '5',
        points = '6',
        assists = '2',
        rebounds = '10'
    )
    stat35 = Stat(
        teamid = '1',
        playerid = '3',
        gameid = '5',
        points = '44',
        assists = '8',
        rebounds = '3'
    )
    stat36 = Stat(
        teamid = '1',
        playerid = '4',
        gameid = '5',
        points = '4',
        assists = '4',
        rebounds = '6'
    )
    stat37 = Stat(
        teamid = '1',
        playerid = '5',
        gameid = '5',
        points = '14',
        assists = '2',
        rebounds = '2'
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
    db.session.add(stat24)
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
    db.session.add(stat136)



    db.session.commit()

def undo_stats():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.stats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM stats")
    db.session.commit()
