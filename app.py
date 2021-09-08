import json
import pprint

filepath = 'resources/seeds/alttpr_none_standard_ganon_bJqPVL0byeOBX2K.json'

with open(filepath) as file:
    seed_json = json.load(file)

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

seed_metadata = seed_json["meta"]

playthrough = seed_json["playthrough"]

shops_l = seed_json["Shops"]
starting_gear = seed_json["Equipped"]

other_stuff = seed_json["Special"]