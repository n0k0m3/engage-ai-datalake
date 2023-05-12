---
title: Apache Superset guide
layout: default
nav_order: 2
---


# Guide to import the data into Superset

## Create a new database connection

1. Setup a generic DuckDB connection
   - Go to `Settings > Database Connections > + Database`
   - Supported database: `DuckDB`
   - Change database name to preferred name
   - Set `SQLAlchemy URI` to `duckdb:///:memory:`
   - In `Advanced > SQL Lab`, turn on `Allow DML`
   - For now, select `FINISH` to save the connection
2. Install `HTTPFS`
   - Go to `SQL > SQL Lab`
   - Select the DuckDB database with the name you just created
   - In SQL editor, run `INSTALL httpfs;`. It will return `The query returned no data` if successful.
3. Add S3 source for DuckDB
   - Go back to `Settings > Database Connections`
   - On the row of the DuckDB database, click `Edit`
   - Go to `Advanced > Other`, in `Engine Parameters` box fill in these contents:
    ```json
    {
        "connect_args": {
            "preload_extensions": [
                "httpfs"
            ],
            "config": {
                "s3_endpoint": "s3_endpoint_without_https",
                "s3_access_key_id": "s3_access_key_id",
                "s3_secret_access_key": "s3_secret_access_key",
                "s3_url_style": "path",
                "s3_use_ssl": "False"
            }
        }
    }
    ```
    - Click `FINISH` to save the connection

## Import the dataset

1. In the `SQL Lab` page, select the DuckDB database with the name you just created
2. To list all the tables, run `SELECT * FROM glob("s3://<bucket-name>/*");`
3. To load dataframes, run `SELECT * FROM 's3://<bucket-name>/<path-to-parquet>';`
4. Note: treats `S3` path as table name for queries, joins, etc.