
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

db_string = f'postgresql://{postgres_username}:{postgres_password}@localhost/alttpr'
engine = create_engine(db_string , echo = True)

app = Flask(__name__)

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

    # Creating connection to alttpr database

    # Begin Session
    session = Session(engine)

    # Select all entries from the database
    # text_statement = text("SELECT * FROM public.\"location-metadata\" ORDER BY location ASC ")
    stmt = select([tables.LocationMetadata.location, tables.LocationMetadata.x, tables.LocationMetadata.y, tables.LocationMetadata.map, tables.LocationMetadata.count])
    results = session.execute(stmt)
    

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




@app.route('/viz2/<location>')
def query_viz2(location):
    # Queries data to create a bar graph of item distribution in a selected area

    # maps query result object to js dataObj
    dataObject = {
        'location': '' , 
        'items': [] , 
        'occurrence': []
    }

    # Returns a dataObject on the endpoint


@app.route('/viz3')
def query_viz3():

    # Function to query main data for viz 3
    return 'This is endpoint for viz 3 data'





if __name__ == '__main__':

    app.run( debug = True)


