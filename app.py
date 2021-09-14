
# importing dependencies
import json
import re
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
from flask_cors import CORS, cross_origin
import tables
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Creating connection to alttpr database
db_string = f'postgresql://{postgres_username}:{postgres_password}@localhost/alttpr'
engine = create_engine(db_string , echo = True)
Session = sessionmaker(bind=engine)
regionsFile = 'resources/regions/regions.json'
itemsFile = 'resoureces/items/items.json'

with open(regionsFile) as file:
    regionInfo = json.load(file)
with open(itemsFile) as file:
    itemInfo = json.load(file)


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/ALTTPR')
@app.route('/')
def home():
    response = render_template('index.html')
    return response

@app.route('/viz1')
def query_viz1():
    return jsonify(regionInfo)

@app.route('/resources/items')
def query_viz1():
    return jsonify(itemInfo)

@app.route('/playthrough/<seed_guid>')
def queryPlaythrough(seed_guid):
    session = Session()

    statement = select(tables.Playthrough.playthrough).filter(tables.Playthrough.seed_guid == seed_guid)
    results = session.execute(statement).first()
    data = []
    for row in results:   
        data = json.loads(row)
    session.close()
    return data


@app.route('/regions', methods=["GET","POST"])
@cross_origin()
def queryByLocations():

    data = request.json
    
    # Begin Session
    session = Session()

    # Select all entries from the database
    statement = select(func.count(tables.Seeds.item) , tables.Seeds.item).group_by(tables.Seeds.item).filter(tables.Seeds.location.in_(data))
    results = session.execute(statement)

    items = []
    count = []
    # Populating
    for row in results:
        count.append(row[0])# appending count -- ideally a pct
        items.append(row[1])# appending item name

    session.close()
    # Returning json data
    return jsonify([data, items, count])
    


@app.route('/items/<item_name>')
@cross_origin()
def query_viz3(item_name):

    # Begin Session
    session = Session()

    # Select all entries from the database
    statement = select(func.count(tables.Seeds.location) , tables.Seeds.location).group_by(tables.Seeds.location).filter(tables.Seeds.item == item_name)
    results = session.execute(statement)

    # initialize returns
    locationCount = []
    itemLocations = []

    # Populating locationItems
    for row in results:
        locationCount.append(row[0])# appending count -- ideally a pct
        itemLocations.append(row[1])# appending location name

    session.close()
    # Returning json data
    return jsonify([item_name , itemLocations , locationCount])
    
@app.route('/viz4')
def query_viz4():
    return jsonify(["String1","String2","String3"])

if __name__ == '__main__':
    app.run( debug = True)


