import json


filepath = 'resources/seeds/alttpr_none_standard_ganon_bJqPVL0byeOBX2K.json'

with open(filepath) as file:
    seed_json : dict = json.load(file)

seed_metadata = seed_json.pop("meta")
seed_number = seed_metadata['world_id']


###
# pop the parts of the spoiler log not relevant to item locations
###
playthrough = seed_json.pop("playthrough")
shops_l = seed_json.pop("Shops")
starting_gear = seed_json.pop("Equipped")
other_stuff = seed_json.pop("Special")
bosses = seed_json.pop('Bosses')
###
#
###


# castle_tower = seed_json["Castle Tower"]
# dark_palace = seed_json["Dark Palace"]
# dark_overworld = seed_json["Dark World"]
# death_mountain = seed_json["Death Mountain"]
# desert_palace = seed_json["Desert Palace"]
# eastern_palace = seed_json["Eastern Palace"]
# ganons_tower = seed_json["Ganons Tower"]
# hyrule_castle = seed_json["Hyrule Castle"]
# ice_palace = seed_json["Ice Palace"]
# light_overworld = seed_json["Light World"]
# misery_mire = seed_json["Misery Mire"]
# skull_woods = seed_json["Skull Woods"]
# swamp_palace = seed_json["Swamp Palace"]
# thieves_town = seed_json["Thieves Town"]
# hera = seed_json["Tower Of Hera"]
# turtle_rock = seed_json["Turtle Rock"]


items = {}
locations = {}

def remid(oldkey : str):
    test = oldkey.split(':')[0]
    return test

for region, dic in seed_json.items():
    
    for key, value in dic.items():
        locations[remid(key)] = remid(value)
        items[remid(value)] = remid(key)




