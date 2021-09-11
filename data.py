<<<<<<< HEAD
import json
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from login import postgres_username, postgres_password
import re
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from login import postgres_username, postgres_password
from tables import Special, Shops, Items, Locations
import sample_data


##########
# DB Info
##########
>>>>>>> 40dc24aaa1bda7d83da7168cbbc3afe9e270ba68

db_string = f'postgresql://{postgres_username}:{postgres_password}@localhost/alttpr'

db = create_engine(db_string, echo=True)
Session = sessionmaker(bind=db)

<<<<<<< HEAD
base = declarative_base()
class Location(base):
    __tablename__ = 'location-metadata'
    location = Column(String, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    map = Column(String)
    requirements = Column(ARRAY(String))
    region = Column(String)
    count = Column(Integer)

locations_filepath = 'resources/locations/overworld.json'

with open(locations_filepath, 'r') as lfile:
    content = lfile.read()
    cleaned_json = re.sub('\/\/.*\n','',str(content))
    overworld_locations : dict = json.loads(cleaned_json)

dlocations_filepath = 'resources/locations/dungeons.json'

with open(dlocations_filepath, 'r') as dfile:
    dcontent = dfile.read()
    dcleaned_json = re.sub('\/\/.*\n','',str(dcontent))
    dungeon_locations : dict = json.loads(dcleaned_json)

=======
>>>>>>> 40dc24aaa1bda7d83da7168cbbc3afe9e270ba68
###################
# Start of Session
###################
session = Session()

##########
<<<<<<< HEAD
# Location Data
##########
table = Location.__table__

# table.drop(db)
table.create(db)

def add_loc_from_region(region : dict):
    region_name = region['name']
    print(f'Region: {region_name}')
    if type(region) == dict and 'children' in region.keys(): 
        for child in region['children']:
            add_loc_from_region(child)
    elif 'map_locations' in region.keys(): 
        location = region['name']
        print(f'\t\tLocation: {location}')
        geography = region['map_locations']
        print(f'\t\tGeography: {geography}')
        point = geography[0]
        sections = region['sections']
        print(f'\t\tSections: {sections}')
        count = 0
        rules = []
        for section in sections:
            if 'item_count' in section.keys():
                count+= section['item_count']
            if 'access_rules' in section.keys(): 
                rules.extend(section['access_rules'])
        session.add(Location(location = location,
                                        x=point['x'], 
                                        y=point['y'], 
                                        map = point['map'],
                                        requirements = rules,
                                        region = region_name,
                                        count = count) )
    else:
        print(f"Bad Location? {region['name']}")

for region in overworld_locations:
    add_loc_from_region(region)
for region in dungeon_locations:
    add_loc_from_region(region)

session.commit()
##########
# Commit/End Location Data
##########


session.close()
###################
# Session Closed
###################


##########
# Start Seed Data
##########
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


items = {}
locations = {}

def remid(oldkey : str):
    test = oldkey.split(':')[0]
    return test


for region, dic in seed_json.items():
    
    for key, value in dic.items():
        locations[remid(key)] = remid(value)
        items[remid(value)] = remid(key)


=======
# Recreate Tables
##########

locations_table = Locations.__table__

locations_table.drop(db, checkfirst=True)
locations_table.create(db)

items_table = Items.__table__

items_table.drop(db, checkfirst=True)
items_table.create(db)

shops_table = Shops.__table__

shops_table.drop(db, checkfirst=True)
shops_table.create(db)

## Special used Dictionaries, but the fix using HSTORE isn't working 
## TODO: implement as an Enhancement for future development.
# special_table = Special.__table__

# special_table.drop(db, checkfirst=True)
# special_table.create(db)


##########
# Items by Locations Data
##########

session.add(Locations(seed_guid = sample_data.seed_guid, locations = sample_data.locations))
session.add(Items(seed_guid = sample_data.seed_guid, items = sample_data.items))
# session.add(Special(seed_guid = sample_data.seed_guid, special = sample_data.special))
for shop in sample_data.shops:
    shop_dict = {}
    shop_dict['name'] = shop['location']
    shop_dict['type'] = shop['type']
    shop_dict['item_1'] = shop['item_0']['item']
    shop_dict['price_1'] = shop['item_0']['price']
    if 'item_1' in shop.keys():
        shop_dict['item_2'] = shop['item_1']['item']
        shop_dict['price_2'] = shop['item_1']['price']
    if 'item_2' in shop.keys():
        shop_dict['item_3'] = shop['item_2']['item']
        shop_dict['price_3'] = shop['item_2']['price']
    session.add(Shops(seed_guid = sample_data.seed_guid, shops = shop_dict))

session.commit()
##########
# Commit/End Location Data
##########


session.close()
###################
# Session Closed
###################
>>>>>>> 40dc24aaa1bda7d83da7168cbbc3afe9e270ba68

