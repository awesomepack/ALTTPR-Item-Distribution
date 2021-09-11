# ALTTPR-Item-Distribution

Analysis of the distribution of items in the legend of Zelda a link to the past

## Using [Data.py](data.py)

### Prerequisites

- Create a Postgres Database named `alttpr`

- Create a file [login.py](login.py) with two entries:

  - postgres_username

  - postgres_password

### Execution

Once you run [data.py](data.py) there should be a new table in the `alttpr` database named `location-metadata` with 68 rows of data
