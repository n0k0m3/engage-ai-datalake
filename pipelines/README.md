# Pipelines for Engage AI Data Platform
This repository contains the data ingestion and processing pipelines for the Engage AI Data Platform. These pipelines form a crucial component of our data management system, enabling efficient ingestion, processing, and storage of data from various sources.

## Current State
At the current stage, our pipeline system is equipped to process data from the World Bank, specifically the Global Development Indicator data. This pipeline fetches, unzips, merges, and stores the data into our Cloudflare R2 storage as Parquet files. Please note that at this time, we only handle Global Development Indicator data and not the entire World Bank data catalog.

## Future Development
We aim to extend our pipeline system to incorporate data from other valuable sources, broadening the scope and versatility of our data platform. These enhancements will be done keeping in mind the same principles of efficiency and reliability that our current system adheres to.

## Usage
The pipelines are designed to be run once during the initialization of the data lake. The processed data is stored in the Cloudflare R2 storage and can be accessed and analyzed using various tools such as DuckDB with HTTPFS, Polars/Pandas, and Apache Superset.

## Running the Pipeline
To initialize the pipeline (only for World Bank for now), navigate to the WB directory and run `main.py`:

```bash
cd pipelines/WB
python main.py
```