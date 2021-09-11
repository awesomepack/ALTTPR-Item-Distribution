from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from login import postgres_username, postgres_password
from tables import Special, Shops, Items, Locations
import sample_data


##########
# DB Info
##########

db_string = f'postgresql://{postgres_username}:{postgres_password}@localhost/alttpr'

db = create_engine(db_string, echo=True)
Session = sessionmaker(bind=db)

###################
# Start of Session
###################
session = Session()

##########
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

