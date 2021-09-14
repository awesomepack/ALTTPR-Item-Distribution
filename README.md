# ALTTPR-Item-Distribution


Members: Jason, Merari, Dinh

Analysis of the distribution of items in [The Legend of Zelda: a Link to the Past VeeTorp Randomizer](https://github.com/sporchia/alttp_vt_randomizer)

## Loading Sample Data

### Prerequisites

- Create a Postgres Database named `alttpr`

- Create a file [login.py](login.py) with two entries:

  - postgres_username

  - postgres_password

### Execution

#### Expected Behavior

#### [locations.py](locations.py)

Once you run [locations.py](locations.py) there should be a new table in the `alttpr` database named `location-metadata` with 68 rows of data containing columns for `seed_guid`, `map`, `x` and `y` at a minumum
No longer used by app.py.   Instead app.py serves the region/location information from [regions.json](resources/regions/regions.json): a hand stitched restructure of the former `location-metadata` database

#### [data.py](data.py)

To run:  Import or execute the [data.py](data.py) script in an interactive python terminal and then use the `loadSample()` function to test the database writing, or `loadAllData(folderpath)` to load files in bulk.  

#### [Flask App](app.py)

Can be run either via `python app.py` or via `flask run`.

##### Flask Routes

- `/viz1` returns json describing the pins to be drawn on the map and the item locations that those pins represent

- `/playthrough/<seed_guid>` returns a json representation of a sample playthrough guaranteed to be able to beat the given seed

- `/regions` given POST request: returns the counts of items found at any of the locations in the list given in the request

- `/items/<item_name>` returns a count of how often that item appears at each location

- `/viz4` dummy route to eventually serve `seed_guid` values for use in a dropdown to pair with the  `/playthrough/<seed_guid>` route

