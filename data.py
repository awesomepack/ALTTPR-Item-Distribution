from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from login import postgres_username, postgres_password
import tables
import seedparser
import os

##########
# DB Info
##########

db_string = f'postgresql://{postgres_username}:{postgres_password}@localhost/alttpr'

db = create_engine(db_string, echo=True)
Session = sessionmaker(bind=db)

##########
# Table Definitions
##########

locations_table = tables.Locations.__table__
items_table = tables.Items.__table__
shops_table = tables.Shops.__table__
# special_table = tables.Special.__table__
seeds_table = tables.Seeds.__table__

##########
# Create Tables
##########

def makeTables(dropfirst = True):

    if dropfirst:
        locations_table.drop(db, checkfirst=True)
        items_table.drop(db, checkfirst=True)
        shops_table.drop(db, checkfirst=True)
        seeds_table.drop(db, checkfirst=True)
        # special_table.drop(db, checkfirst=True)

    locations_table.create(db)
    items_table.create(db)
    shops_table.create(db)
    seeds_table.create(db)

    ## Special used Dictionaries, but the fix using HSTORE isn't working 
    ## TODO: implement as an Enhancement for future development.
    # special_table.create(db)


##########
# Load Sample Data
##########


def load_sample(maketables = True, dropfirst = True):
    return load_data(seedparser.sample_filepath, maketables=maketables, dropfirst=dropfirst)

##########
# Load Data
##########

def load_data(filepath, maketables = True, dropfirst = True):
    session = Session()
    if maketables: makeTables(dropfirst)
    
    seed = seedparser.Seed(filepath)
    
    session.add(tables.Locations(seed_guid = seed.seed_guid, locations = seed.locations))
    session.add(tables.Items(seed_guid = seed.seed_guid, items = seed.items))
    for location, item in seed.locations.items():
        session.add(tables.Seeds(seed_guid = seed.seed_guid, item = item, location = location))
    # session.add(tables.Special(seed_guid = seed.seed_guid, special = seed.special))
    for shop in seed.shops:
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
        session.add(tables.Shops(seed_guid = seed.seed_guid, shops = shop_dict))

    session.commit()
    session.close()

def loadSeed(filepath : str, session : Session):
    seed = seedparser.Seed(filepath)
    
    session.add(tables.Locations(seed_guid = seed.seed_guid, locations = seed.locations))
    session.add(tables.Items(seed_guid = seed.seed_guid, items = seed.items))
    for location, item in seed.locations.items():
        session.add(tables.Seeds(seed_guid = seed.seed_guid, item = item, location = location))
    # session.add(tables.Special(seed_guid = seed.seed_guid, special = seed.special))
    for shop in seed.shops:
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
        session.add(tables.Shops(seed_guid = seed.seed_guid, shops = shop_dict))

    pass

def loadAllData(folderpath : str, limit = -1, batchsize = 1000, maketables = True, dropfirst = True):
    session = Session()
    if maketables:
        makeTables(dropfirst=dropfirst)
    if limit <=0:
        for i, file in enumerate(os.scandir(folderpath)):
            if i > 0 and batchsize > 0 and i%batchsize == 0:
                session.commit()
            else:
                print (f'unlimited ({i}): {file.path}')
                if file.path.endswith('.json'):
                    loadSeed(file.path, session)
    else:
        for i, file in enumerate(os.scandir(folderpath)):
            if i > 0 and batchsize > 0 and i%batchsize == 0:
                session.commit()
            if i>=limit:
                break
            else:
                print (f'{limit-i}: {file.path}' )
                if file.path.endswith('.json'):
                    loadSeed(file.path, session)
    session.commit()
    session.close()
    

