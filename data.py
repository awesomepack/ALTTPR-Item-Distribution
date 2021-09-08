import json
import pprint

filepath = 'resources/seeds/alttpr_none_standard_ganon_bJqPVL0byeOBX2K.json'

with open(filepath) as file:
    seed_json = json.load(file)

seed_metadata = seed_json["meta"]
seed_number = seed_metadata['world_id']

pp = pprint.PrettyPrinter(indent=2)
bosses = seed_json['Bosses']
castle_tower = seed_json["Castle Tower"]
dark_palace = seed_json["Dark Palace"]
dark_overworld = seed_json["Dark World"]
death_mountain = seed_json["Death Mountain"]
desert_palace = seed_json["Desert Palace"]
eastern_palace = seed_json["Eastern Palace"]
ganons_tower = seed_json["Ganons Tower"]
hyrule_castle = seed_json["Hyrule Castle"]
ice_palace = seed_json["Ice Palace"]
light_overworld = seed_json["Light World"]
misery_mire = seed_json["Misery Mire"]
skull_woods = seed_json["Skull Woods"]
swamp_palace = seed_json["Swamp Palace"]
thieves_town = seed_json["Thieves Town"]
hera = seed_json["Tower Of Hera"]
turtle_rock = seed_json["Turtle Rock"]

item_dicts = [castle_tower, dark_palace, dark_overworld, death_mountain, desert_palace, \
    eastern_palace, ganons_tower, hyrule_castle, ice_palace, light_overworld, misery_mire, \
    skull_woods, swamp_palace, thieves_town, hera, turtle_rock]

items = {}
locations = {}
for dict in item_dicts:
    items.update(dict)

def remid(oldkey : str):
    test = oldkey.replace(f':{seed_number}', '', -1)
    return test

for dic in item_dicts:
    for key, value in dic.items():
        locations[remid(key)] = remid(value)
        items[remid(value)] = remid(key)



playthrough = seed_json["playthrough"]

shops_l = seed_json["Shops"]
starting_gear = seed_json["Equipped"]

other_stuff = seed_json["Special"]

