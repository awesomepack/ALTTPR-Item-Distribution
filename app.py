# The Flask application will go here
# Starting out with a tutorial

# importing dependencies
from flask import Flask , redirect , url_for , request , render_template

app = Flask(__name__)

@app.route('/ALTTPR')
def home():

    return 'This is the home page'

    # Function to render potential home page with information on API routes

@app.route('/viz1')
def query_viz1():

    # Function to query main data in preparation of viz1
    return 'This is endpoint for viz1 data'

@app.route('/viz2')
def query_viz2():

    # Function to query main data for viz 2
    return 'This is endpoint for viz 2 data'

@app.route('/viz3')
def query_viz3():

    # Function to query main data for viz 3
    return 'This is endpoint for viz 3 data'





if __name__ == '__main__':

    app.run( debug = True)

# To Do:
# tutorial: https://www.tutorialspoint.com/flask/flask_templates.htm
# inspect one of USGS's data endpoints , that is what we will try to mimic for each route
# Create a dummy dataset with our desired structure
# Create a dummy database for our dummy dataset
# Layout routes for our three visualizations

# Each route should:
    # Query the main data needed for the visualization
    # format the data in an object for use in js.
