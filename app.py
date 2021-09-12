
# importing dependencies
import sqlalchemy
from sqlalchemy import select, text
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData
from login import postgres_password , postgres_username
from flask import Flask , redirect , url_for , request , render_template
from flask import jsonify
import tables


app = Flask(__name__)

# Creating connection to alttpr database
db_string = f'postgresql://{postgres_username}:{postgres_password}@localhost/alttpr'
engine = create_engine(db_string , echo = True)


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/ALTTPR')
def home():
    return 'This is the home page'

    # Function to render potential home page with information on API routes


@app.route('/viz1')
def query_viz1():

    # Begin Session
    session = Session(engine)

    # Select all entries from the database
    # text_statement = text("SELECT * FROM public.\"location-metadata\" ORDER BY location ASC ")
    statement = select([tables.LocationMetadata.location, tables.LocationMetadata.x, tables.LocationMetadata.y, tables.LocationMetadata.map, tables.LocationMetadata.count])
    results = session.execute(statement)
    

    # initializing the map locations dictionary that will be served
    mapLocations = []

    # populating mapLocations with results from query
    for row in results:
        location = row[0]
        map = row[3]
        if map == "lightworld":
            x = row[1]
            y = 2007 - row[2]
            coords = [y, x]
        else:
            x = row[1] + 2007
            y = 2007 - row[2]
            coords = [y, x]
            
        count = row[4]
        mapLocations.append([location, coords, count])
    return jsonify(mapLocations)


@app.route('/viz2/<location_name>')
def query_viz2(location_name):

    # Begin Session
    session = Session(engine)

    # Select all entries from the database
    #text_statement = text(f"SELECT \"{location_name}\" FROM public.\"{tables.Locations.__tablename__}\"")
    stmt = select(func.count(tables.Seeds.item) , tables.Seeds.item).group_by(tables.Seeds.item).filter(tables.Seeds.location == location_name)
    results = session.execute(stmt)

    #var test_data = ["Location_name", ['list of items'], ['list of values']];
    # initializing locationItems
    locationItems = []

    # Populating locationItems
    for row in results:
        locationItems.append(row[0])# appending count -- ideally a pct
        locationItems.append(row[1])# appending item name

    
    # Returning json data
    return jsonify(locationItems)





@app.route('/viz3')
def query_viz3():
    
    if __name__ == '__main__':

        app.run( debug = True)


