import etl as e
import argparse
import time
import sys


DB_SCHEMA = "sa"
TABLE = "rides"
DOWNLOAD_DIR = "data/original"
PROCESSED_DIR = "data/processed"
STATIC_DIR = "data/static"


def extraction(config: dict) -> None:
    """ Runs extraction

        Args:
            config (str): configuration dictionary
    """
    e.info("EXTRACTION: START DATA EXTRACTION")
    url = config["url"]
    fname = config["fname"]
    fname = f"{DOWNLOAD_DIR}/{fname}"
    e.info("EXTRACTION: DOWNLOADING DATA")
    e.download_data(url, fname)
    e.info("EXTRACTION: COMPLETED")


def transformation(config: dict) -> None:
    """Runs transformation

    Args:
        config (dict): [description]
    """
    e.info("TRANSFORMATION: START TRANSFORMATION")
    e.info("TRANSFORMATION: READING DATA")
    fname = config["fname"]
    df = e.read_parquet(f"{DOWNLOAD_DIR}/{fname}")
    e.info("TRANSFORMATION: DATA READING COMPLETED")
    e.info("TRANSFORMATION: DATA SUBSETTING BY DATE") 

    # Select only the rows in the analysis period
    # What happens if there is no data in this period?
    # What should we do in that case?
    start_date = config["period"]["start_date"]
    end_date = config["period"]["end_date"]
    df = df.loc[(start_date <= df["tpep_pickup_datetime"]) & (df["tpep_dropoff_datetime"] <= end_date)]

    e.info("TRANSFORMATION: SUBSETTING DONE")
    e.info("TRANSFORMATION: ADDING SPATIAL INFORMATION")

    # Add latitude and longitude columns from shapefile (the geometry is polygons)
    gdf = e.read_shp(f"{STATIC_DIR}/taxi_zones.shp")
    # Layer is in EPSG:2263, we prefer in 4326
    gdf = gdf.to_crs('EPSG:4326')
    # create columns with latitude and longitude using the representative_point
    # which is similar to centroid, but garanteed to be inside the polygon
    gdf['latitude'] = gdf.representative_point().y
    gdf['longitude'] = gdf.representative_point().x
    locations = gdf[['LocationID', 'latitude', 'longitude']]
    # Rename columns to match the the join column and output columns
    pu_locations = locations.rename(columns={
        "LocationID":"PULocationID",
        "latitude":"pickup_latitude",
        "longitude":"pickup_longitude"})
    do_locations = locations.rename(columns={
        "LocationID":"DOLocationID",
        "latitude":"dropoff_latitude",
        "longitude":"dropoff_longitude"})
    # Join the pickup and drop off x and y and columns
    df = df.merge(pu_locations, on='PULocationID')
    df = df.merge(do_locations, on='DOLocationID')

    # Rename columns to match the database model
    df = df.rename(columns={
        "tpep_pickup_datetime":"pickup_datetime",
        "tpep_dropoff_datetime":"dropoff_datetime",
        "RatecodeID":"rate_code"})
    
    # Fix wrong payment_type = 0 to 5 (unknown)
    df.loc[df.payment_type == 0, 'payment_type'] = 5

    cols = config["columns"]

    # This is a simple transformation, but simple transformations
    # can be quite tricky. Consider what happens if there is
    # a column in cols not present in df?
    # How can we save that?
    df = df[cols]
    
    e.info("TRANSFORMATION: SAVING TRANSFORMED DATA")
    e.write_csv(df, fname=f"{PROCESSED_DIR}/{fname}", sep=",")
    e.info("TRANSFORMATION: SAVED")
    e.info("TRANSFORMATION: COMPLETED")


def load(config: dict, chunksize: int=1000) -> None:
    """Runs load

    Args:
        config (dict): configuration dictionary
        chunksize (int): the number of rows to be inserted at one time
    """
    try:
        fname = config["fname"]
        db = e.DBController(**config["database"])
        e.info("LOAD: READING DATA")
        df = e.read_csv(f"{PROCESSED_DIR}/{fname}")
        e.info("LOAD: DATA READ")
        e.info("LOAD: INSERTING DATA INTO DATABASE")
        db.insert_data(df, DB_SCHEMA, TABLE, chunksize=chunksize)
        e.done("LOAD: DONE")
    except Exception as err:
        e.die(f"LOAD: {err}")


def parse_args() -> str:
    """ Reads command line arguments

        Returns:
            the name of the configuration file
    """
    parser = argparse.ArgumentParser(description="GPS: ETL working example")
    parser.add_argument("--config_file", required=False, help="The configuration file", default="./config/00.yml")
    args = parser.parse_args()
    return args.config_file

def time_this_function(func, **kwargs) -> str:
    """ Times function `func`

        Args:
            func (function): the function we want to time

        Returns:
            a string with the execution time
    """
    import time
    t0 = time.time()
    func(**kwargs)
    t1 = time.time()
    return f"'{func.__name__}' EXECUTED IN {t1-t0:.3f} SECONDS"

def main(config_file: str) -> None:
    """Main function for ETL

    Args:
        config_file (str): configuration file
    """
    config = e.read_config(config_file)
    # extraction(config)
    msg = time_this_function(extraction, config=config)
    e.info(msg)
    # transformation(config)
    msg = time_this_function(transformation, config=config)
    e.info(msg)
    # load(config, chunksize=10000)
    msg = time_this_function(load, config=config, chunksize=1000)
    e.info(msg)


if __name__ == "__main__":
    config_file = parse_args()
    main(config_file)
