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

# locations_table = tables.Locations.__table__
# items_table = tables.Items.__table__
shops_table = tables.Shops.__table__
special_table = tables.Playthrough.__table__
seeds_table = tables.Seeds.__table__

##########
# Create Tables
##########

def makeTables(dropfirst = True):

    if dropfirst:
        # locations_table.drop(db, checkfirst=True)
        # items_table.drop(db, checkfirst=True)
        shops_table.drop(db, checkfirst=True)
        seeds_table.drop(db, checkfirst=True)
        special_table.drop(db, checkfirst=True)

    # locations_table.create(db, checkfirst=True)
    # items_table.create(db, checkfirst=True)
    shops_table.create(db, checkfirst=True)
    seeds_table.create(db, checkfirst=True)
    special_table.create(db, checkfirst=True)


##########
# Load Sample Data
##########


def loadSample(maketables = True, dropfirst = False):
    return loadAllData(seedparser.sample_folderpath, maketables=maketables, dropfirst=dropfirst)

def loadSeed(filepath : str, session : Session):
    seed = seedparser.Seed(filepath)
    
    # Items and Locations tables obsolesced by Seeds table
    # session.add(tables.Locations(seed_guid = seed.seed_guid, locations = seed.locations))
    # session.add(tables.Items(seed_guid = seed.seed_guid, items = seed.items))
    for location, item in seed.locations.items():
        session.add(tables.Seeds(seed_guid = seed.seed_guid, item = item, location = location))
    session.add(tables.Playthrough(seed_guid = seed.seed_guid, seed_number = seed.seed_number, playthrough = seed.playthrough))
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

def loadAllData(folderpath : str, limit = -1, batchsize = 1000, maketables = True, dropfirst = False):
    session = Session()
    if maketables:
        makeTables(dropfirst=dropfirst)
    if limit <=0:
        for i, file in enumerate(os.scandir(folderpath)):
            print (f'unlimited ({i}): {file.path}')
            if file.path.endswith('.json'):
                loadSeed(file.path, session)
                if i > 0 and batchsize > 0 and i%batchsize == 0:
                    session.commit()
    else:
        for i, file in enumerate(os.scandir(folderpath)):
            if i>=limit:
                break
            print (f'{limit-i}: {file.path}' )
            if file.path.endswith('.json'):
                loadSeed(file.path, session)
                if i > 0 and batchsize > 0 and i%batchsize == 0:
                    session.commit()
    session.commit()
    session.close()
