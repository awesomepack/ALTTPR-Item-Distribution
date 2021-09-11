
# importing dependencies
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import create_engine
from login import postgres_password , postgres_username
from flask import Flask , redirect , url_for , request , render_template

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
    return str(Base.classes.keys())


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

# To Do:
# tutorial: https://www.tutorialspoint.com/flask/flask_templates.htm
# inspect one of USGS's data endpoints , that is what we will try to mimic for each route

# Create A dummy data query result for viz2
# Create a function that returns it in Json or GeoJson format
# Try accessing the data from your endpoint via plot.js

