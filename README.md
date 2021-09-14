# ALTTPR-Item-Distribution


Members: Jason, Merari, Dinh

Analysis of the distribution of items in the legend of Zelda a link to the past

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

#### [data.py](data.py)

To run:  Import or execute the [data.py](data.py) script in an interactive python terminal and then use the `loadSample()` function to test the database writing, or `loadAllData(folderpath)` to load files in bulk.  

-- Warning --

`loadAllData` will drop the tables first before inserting data from the folder.  To preserve old values be sure to set the parameter `dropfirst=False`
