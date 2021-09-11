from collections import defaultdict
import re
import json

##########
# Start Sample Data
##########


filepath = 'resources/seeds/alttpr_none_standard_ganon_bJqPVL0byeOBX2K.json'

pattern = 'ganon_(.+)\.json'
seed_guid = re.search(pattern, filepath).group(1)

with open(filepath) as file:
    seed_json : dict = json.load(file)

seed_metadata = seed_json.pop("meta")
seed_number = seed_metadata['world_id']


###
# pop the parts of the spoiler log not relevant to item locations
###
playthrough = seed_json.pop("playthrough")
shops = seed_json.pop("Shops")
starting_gear = seed_json.pop("Equipped")
other_stuff = seed_json.pop("Special")
bosses = seed_json.pop('Bosses')

special = {}.update(playthrough= playthrough)
###
#
###

items = defaultdict(list)
locations = {}

def remid(oldkey : str):
    test = oldkey.split(':')[0]
    return test


for region, dic in seed_json.items():
    
    for key, value in dic.items():
        locations[remid(key)] = remid(value)
        items[remid(value)].append([remid(key)])


location_map = {}
reverse_map = {}

for item in locations.keys():
    trimmed = re.sub('\W','', item)
    # print (f'{trimmed} = Column(String)')
    location_map[item] = trimmed
    reverse_map[trimmed] = item
