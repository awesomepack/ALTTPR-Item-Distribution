import json
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from login import postgres_username, postgres_password
import re

db_string = f'postgresql://{postgres_username}:{postgres_password}@localhost/alttpr'

db = create_engine(db_string, echo=True)
Session = sessionmaker(bind=db)

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

###################
# Start of Session
###################
session = Session()

##########
# Location Data
##########
table = Location.__table__

table.drop(db)
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






