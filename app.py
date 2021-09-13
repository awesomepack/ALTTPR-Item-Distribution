
# importing dependencies
import json
import sqlalchemy
from sqlalchemy import select, text
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import func, bindparam
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import MetaData
from login import postgres_password , postgres_username
from flask import Flask , redirect , url_for , request , render_template
from flask import jsonify
import tables
import os

app = Flask(__name__)

# Creating connection to alttpr database
db_string = f'postgresql://{postgres_username}:{postgres_password}@localhost/alttpr'
engine = create_engine(db_string , echo = True)
Session = sessionmaker(bind=engine)
regionsFile = 'resources/regions/regions.json'

with open(regionsFile) as file:
    regionInfo = json.load(file)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# Function to render potential home page with information on API routes
@app.route('/ALTTPR')
def home():
    return 'This route will serve up images'


@app.route('/viz1')
def query_viz1():
    return jsonify(regionInfo)


@app.route('/regions/<region_name>')
def query_viz2(region_name):

    # Begin Session
    session = Session()

    # location_list = regionToLocations_map[region_name]

    # Select all entries from the database
    #text_statement = text(f"SELECT \"{location_name}\" FROM public.\"{tables.Locations.__tablename__}\"")
    statement = select(func.count(tables.Seeds.item) , tables.Seeds.item).group_by(tables.Seeds.item).filter(tables.Seeds.location == region_name)
    results = session.execute(statement)

    #var test_data = ["Location_name", ['list of items'], ['list of values']];
    # initializing locationItems
    items = []
    count = []
    # Populating locationItems
    for row in results:
        count.append(row[0])# appending count -- ideally a pct
        items.append(row[1])# appending item name

    session.close()
    # Returning json data
    return jsonify([region_name, items, count])


@app.route('/viz3/<item_name>')
def query_viz3(item_name):

    # Begin Session
    session = Session()

    # Select all entries from the database
    #text_statement = text(f"SELECT \"{location_name}\" FROM public.\"{tables.Locations.__tablename__}\"")
    statement = select(func.count(tables.Seeds.location) , tables.Seeds.location).group_by(tables.Seeds.location).filter(tables.Seeds.item == item_name)
    results = session.execute(statement)

    #var test_data = ["Location_name", ['list of items'], ['list of values']];
    # initializing locationItems
    itemLocations = []

    # Populating locationItems
    for row in results:
        itemLocations.append(row[0])# appending count -- ideally a pct
        itemLocations.append(row[1])# appending item name

    session.close()
    # Returning json data
    return jsonify(itemLocations)
    
@app.route('/viz4')
def query_viz4():
    return jsonify(["String1","String2","String3"])

if __name__ == '__main__':
    app.run( debug = True)


