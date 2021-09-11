
# importing dependencies
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData
from login import postgres_password , postgres_username
from flask import Flask , redirect , url_for , request , render_template
from flask import jsonify

app = Flask(__name__)


@app.route('/ALTTPR')

def home():

    return 'This is the home page'

    # Function to render potential home page with information on API routes

@app.route('/viz1')
def query_viz1():

    # Creating connection to alttpr database
    db_string = f'postgresql://{postgres_username}:{postgres_password}@localhost/alttpr'
    engine = create_engine(db_string , echo = True)

    # Reflecting database
    Base = automap_base()
    Base.prepare(engine , reflect = True)

    # passing reference to the location-metadata table
    Locations = Base.classes.locationMetadata

    # Begin Session
    session = Session(engine)

    # Select all entries from the database
    results = session.query(Locations.location , Locations.map , Locations.X , Locations.y).all()

    # initializing the map locations dictionary that will be served
    mapLocations = []

    # populating mapLocations with results from query
    for row in results:
        mapLocations.append([row[0] , [row[2], row[3]]]);
        # mapLocations['Map'].append(row[1]);
        # mapLocations['x'].append(2007 - row[2]);

        # if row[1] == 'darkworld':

        #     mapLocations['y'].append(2007 + row[3])
        # else:
        #     mapLocations['y'].append(row[3])

    return jsonify(mapLocations)




@app.route('/viz2/<Location>')
def query_viz2(Location):
    # Queries data to create a bar graph of item distribution in a selected area

    # maps query result object to js dataObj
    dataObject = {
        'location': '' , 
        'items': [] , 
        'occurrence': []
    };

    # Returns a dataObject on the endpoint


@app.route('/viz3')
def query_viz3():

    # Function to query main data for viz 3
    return 'This is endpoint for viz 3 data'





if __name__ == '__main__':

    app.run( debug = True)


