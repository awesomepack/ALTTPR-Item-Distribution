# ALTTPR-Item-Distribution

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

Once you run [data.py](data.py) there should be two new tables - `items` and `locations` - with one row of sample data each as well as a third table, `shops` with multiple rows all belonging to the same seed.
