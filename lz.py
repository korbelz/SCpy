#comment section
#author: Korbelz , AGB Corp
#Feedback: Discord: Korbelz#3504
#current scope: Landing zone info

import poi

i_loop = 0 
print ('*** This app gives basic info on Landing Zones in star citizen ***')
print ('*** Written by Korbelz, AGB Corp ***')
print ('*** Feedback/Bugs: Discord: Korbelz#3504 ***')
input('Press ENTER to continue')


while i_loop < 24:
    lz = poi.here()
    print ('')
    print ('***')
    print (f'Landing at {lz}')
    #input('Press ENTER to continue')

    argument = lz
    #LZ date here

    Port_Olisar = ['Space', 'Yes all sizes', 'Yes', 'Yes', 'No nav notes']

    GrimHex = ['Space', 'Yes 1 medium 2 small', 'Yes', 'Yes', 'Asteroids IVO']

    ArcCorp_Mining_Area_157 = ['-92', 'Yes 1 small', 'No', 'Yes', '20m tall towers']

    Benson_Mining = ['-278', 'No', 'No', 'No', '20m Tall towers at LZ, One 200m AGL peak 800m from LZ']

    Deakins_Research = ['-116', 'Yes 1 medium 1 small', 'No', 'Yes', '20m Tall towers at LZ']

    Jumptown = ['Unknown', 'Unknown', 'Unknown', 'Unknown', 'first rule of jumptown is you dont talk about jumptown']

    Kudre_ore = ['67', 'No', 'No', 'No', '20m Tall towers at LZ, LZ on plateau, Low level haze']

    ArcCorp_Mining_Area_141 = ['114', 'Yes 1 small', 'No', 'Yes', '15m tall towers at LZ, LZ on large plateau. low level haze']

    Bountiful_Harvest = ['43', 'No', 'No', 'No', '15m tall towers at LZ, LZ inside a large crater, low level haze']

    Shubin_Mining = ['-171', 'Yes 1 medium 1 small', 'No', 'Yes', '15m tall towers at LZ, LZ in slight crater with high terrain IVO, low level haze']

    Tram_and_Myers = ['160', 'No', 'No', 'No', '15m Tall towers at LZ']

    Gallete_Family_Farms = ['-117', 'No', 'No', 'No', '15m Tall towers at LZ, LZ in a valley with high terrain IVO']

    Terra_Mills = ['-320', 'Yes 1 medium', 'No', 'Yes', '15m Tall towers at LZ']

    Hickes_Research_Outpost = ['-61', 'Yes 1 medium 1 small', 'No', 'Yes', '15m Tall towers at LZ, mountainous terrian near LZ']

    Levski = ['-345', 'Yes 4 medium', 'Yes', 'Yes', 'Steep terrain and towers IVO 350m MSL']

    CRU_L2 = ['Space', 'Yes 4 medium 2 small', 'Yes', 'Yes', 'Asteroids IVO']

    CRU_L4 = ['Space', 'Yes 4 medium 2 small', 'Yes', 'Yes', 'Asteroids IVO']

    CRU_L5 = ['Space', 'Yes 4 medium 2 small', 'Yes', 'Yes', 'Asteroids IVO']

    Lorville = ['Space', 'Yes all sizes', 'Yes', 'Yes', '3000 MSL no-fly zone around city, Landing zones are inside the hangers']

    HMC_Edmond = ['406', 'Yes 1 medium 1 small', 'No', 'Yes', '15m tall poles at LZ, Water near LZ']

    HMC_Hadley = ['959', 'Yes 1 medium 1 small', 'No', 'Yes', '15m tall poles at LZ, LZ on plateau']

    HMC_Oparei = ['2172', 'Yes 1 medium 1 small', 'No', 'Yes', '15m tall poles at LZ, LZ in Savanna biome, 15m trees within 100m']

    HMC_Pinewood = ['1318', 'Yes 1 medium 1 small', 'No', 'Yes', '15m tall poles at LZ, raising terrian in all directions from LZ']

    HMC_Stanhope = ['428', 'Yes 1 medium 1 small', 'No', 'Yes', '15m tall poles at LZ, Ocean on 1 side, raising terrain on 3 other sides.']

    HMC_Thedus = ['-92', 'Yes 1 medium 1 small', 'No', 'Yes', '15m tall towers']

    HMC_Anderson = ['2570', 'Yes 1 medium 1 small', 'No', 'Yes', 'Nothing here, Mountainous terrian in all directions, 15m tall poles at LZ']

    HMC_Norgaard = ['1280', 'Yes 1 medium 1 small', 'No', 'Yes', '15m tall towers']

    HMC_Bezdek = ['-26', 'Yes 1 medium 1 small', 'No', 'Yes', ' Heat haze limits vis at low level, 15m tall poles at LZ']

    HMC_Lathan = ['1', 'Yes 1 medium 1 small', 'No', 'Yes', 'Heat haze limits vis at low level, 1m tall poles around LZ']

    HMC_Ryder = ['113', 'Yes 1 medium 1 small', 'No', 'Yes', 'LZ offset 920m from waypoint, 15m Poles at LZ, 100m+ Rock towers multiple directions']

    HMC_Woodruff = ['64', 'Yes 1 medium 1 small', 'No', 'Yes', 'LZ on plateau, 15m poles at LZ, 100m Rock towers within 1700m']

    HMC_Hahn = ['360', 'Yes 1 medium 1 small', 'No', 'Yes', '15m poles at LZ, Deep craters within 500m']

    HMC_Periman = ['330', 'Yes 1 medium 1 small', 'No', 'Yes', 'Deep craters within 500m, 15m poles at LZ']

    HUR_L1 = ['Space', 'Yes 4 medium 2 small', 'Yes', 'Yes', 'Asteroids IVO']

    HUR_L2 = ['Space', 'Yes 4 medium 2 small', 'Yes', 'Yes', 'Asteroids IVO']

    HUR_L3 = ['Space', 'Yes 4 medium 2 small', 'Yes', 'Yes', 'Asteroids IVO']

    HUR_L4 = ['Space', 'Yes 4 medium 2 small', 'Yes', 'Yes', 'Asteroids IVO']

    HUR_L5 = ['Space', 'Yes 4 medium 2 small', 'Yes', 'Yes', 'Asteroids IVO']

    def lz_to_print(argument):
        switcher = {
                "Port Olisar": Port_Olisar,
                "GrimHex": GrimHex,
                "ArcCorp Mining Area 157": ArcCorp_Mining_Area_157,
                "Benson Mining": Benson_Mining,
                "Deakins Research": Deakins_Research,
                "Jumptown": Jumptown,
                "Kudre Ore": Kudre_ore,
                "ArcCorp Mining Area 141": ArcCorp_Mining_Area_141,
                "Bountiful Harvest": Bountiful_Harvest,
                "Shubin Mining": Shubin_Mining,
                "Tram and Myers": Tram_and_Myers,
                "Gallete Family Farms": Gallete_Family_Farms,
                "Terra Mills": Terra_Mills,
                "Hickes Research Outpost": Hickes_Research_Outpost,
                "Levski": Levski,
                "CRU L2": CRU_L2,
                "CRU L4": CRU_L4,
                "CRU L5": CRU_L5,
                "Lorville": Lorville,
                "HMC Edmond": HMC_Edmond,
                "HMC Hadley": HMC_Hadley,
                "HMC Oparei": HMC_Oparei,
                "HMC Pinewood": HMC_Pinewood,
                "HMC Stanhope": HMC_Stanhope,
                "HMC Thedus": HMC_Thedus,
                "HMC Anderson": HMC_Anderson,
                "HMC Norgaard": HMC_Norgaard,
                "HMC Bezdek": HMC_Bezdek,
                "HMC Lathan": HMC_Lathan,
                "HMC Ryder": HMC_Ryder,
                "HMC Woodruff": HMC_Woodruff,
                "HMC Hahn": HMC_Hahn,
                "HMC Periman": HMC_Periman,
                "HUR L1": HUR_L1,
                "HUR L2": HUR_L2,
                "HUR L3": HUR_L3,
                "HUR L4": HUR_L4,
                "HUR L5": HUR_L5,
        }
        return switcher.get(argument, "nothing")

    lz_print = (lz_to_print(argument))

    print (f"Alt, MSL: {lz_print[0]} meters")
    print (f"Landing Pads: {lz_print[1]}")
    print (f"Clearance required: {lz_print[2]}")
    print (f"Armstice zone: {lz_print[3]}")
    print (f"Navigation Notes/Hazards: {lz_print[4]}")
    print ('***')
    print ('')

    input('Press ENTER to look up a new Landing Zone or CLOSE terminal to exit')
    i_loop += 1

print ("frankie is a homo :P")


