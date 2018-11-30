#comment section
#author: Korbelz , AGB Corp
#Feedback: Discord: Korbelz#3504
#current scope: points of intrest menu for SC


def here():
    star = ['Stanton', 'Sun']

    star_sel = int(input(f"Select star system by #: 0 - {star[0]}: " ))

    print (f'You selected the {star[star_sel]} system')

    #planet_selction
    if star_sel == 0: 
        planet_list = ['Crusader', 'Hurston']
    else:
        planet_list = ['Earth', 'Mars']

    plan_sel = int(input(f"Select planetary system by #: 0 - {planet_list[0]}, 1 - {planet_list[1]}: " ))

    print (f'You selected the {planet_list[plan_sel]} planetary system')

    argument = planet_list[plan_sel]

    #moon selection

    Crusader_moons = ['Crusader', 'Yela', 'Daymar','Cellin','Delamar','CRU']

    Hurston_moons = ['Hurston', 'Aberdeen','Arial','Ita','Magda','HUR']

    Earth_moons = ['Hurston', 'Aberdeen','Arial','Ita','Magda','HUR']

    Mars_moons = ['Hurston', 'Aberdeen','Arial','Ita','Magda','HUR']

    def plan_to_moons(argument):
        switcher = {
            "Crusader": Crusader_moons,
            "Hurston": Hurston_moons,
            "Earth": Earth_moons,
            "Mars": Mars_moons,
        }
        return switcher.get(argument, "nothing")

    current_moon = (plan_to_moons(argument))

    moon_sel = int(input(f"Select planet or moon by #: 0 - {current_moon[0]}, 1 - {current_moon[1]}, 2 - {current_moon[2]}, 3 - {current_moon[3]}, 4 - {current_moon[4]}, 5 - {current_moon[5]}: " ))

    print (f'You selected the {current_moon[moon_sel]} planet or moon')

    argument = current_moon[moon_sel]
    #POI selction

    Crusader = ['Port Olisar', 'one', 'two', 'three', 'four', 'five', 'six' ]

    Yela = ['GrimHex', 'ArcCorp Mining Area 157', 'Benson Mining', 'Deakins Research', 'Jumptown', 'five', 'six' ]

    Daymar = ['Kudre Ore', 'ArcCorp Mining Area 141', 'Bountiful Harvest', 'Shubin Mining', 'four', 'five', 'six' ]

    Cellin = ['Tram and Myers', 'Gallete Family Farms', 'Terra Mills', 'Hickes Research Outpost', 'four', 'five', 'six' ]

    Delamar = ['Levski', 'one', 'two', 'three', 'four', 'five', 'six' ]

    CRU = ['CRU L2', 'CRU L4', 'CRU L5', 'three', 'four', 'five', 'six' ]

    Hurston = ['Lorville', 'HMC Edmond', 'HMC Hadley', 'HMC Oparei', 'HMC Pinewood', 'HMC Stanhope', 'HMC Thedus' ]

    Aberdeen = ['HMC Anderson', 'HMC Norgaard', 'two', 'three', 'four', 'five', 'six' ]

    Arial = ['HMC Bezdek', 'HMC Lathan', 'two', 'three', 'four', 'five', 'six' ]

    Ita = ['HMC Ryder', 'HMC Woodruff', 'two', 'three', 'four', 'five', 'six' ]

    Magda = ['HMC Hahn', 'HMC Periman', 'two', 'three', 'four', 'five', 'six' ]

    HUR = ['HUR L1', 'HUR L2', 'HUR L3', 'HUR L4', 'HUR L5', 'five', 'six' ]

    def moons_to_poi(argument):
        switcher = {
            "Crusader": Crusader,
            "Yela": Yela,
            "Daymar": Daymar,
            "Cellin": Cellin,
            "Delamar": Delamar,
            "CRU": CRU,
            "Hurston": Hurston,
            "Aberdeen": Aberdeen,
            "Arial": Arial,
            "Ita": Ita,
            "Magda": Magda,
            "HUR": HUR,
        }
        return switcher.get(argument, "nothing")

    current_poi = (moons_to_poi(argument))
    #print (current_poi)

    poi_sel = int(input(f"Select planet or moon by #: 0 - {current_poi[0]}, 1 - {current_poi[1]}, 2 - {current_poi[2]}, 3 - {current_poi[3]}, 4 - {current_poi[4]}, 5 - {current_poi[5]}, 6 - {current_poi[6]}: " ))

    #print (f'You selected the {current_poi[poi_sel]} point of trade')

    here_loc = current_poi[poi_sel] 
    return here_loc

#input('Press ENTER to exit')