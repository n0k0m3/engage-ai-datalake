---
title: Home Page
layout: home
nav_order: 1
---

# Engage AI Data Platform

The Engage AI Data Platform is a sophisticated, cloud-based data management platform serving as a single source of truth for all data leveraged by Engage AI Data Analysts. Designed with robustness and adaptability in mind, the platform encompasses an entire data lifecycle, including data ingestion, storage, processing, access, and governance. The main features of this platform include:

## 1. Data Ingestion
The platform provides a systematic, high-performance data [ingestion pipeline](/pipelines/) for processing data. This pipeline, implemented in Python, ensures efficient fetching, unzipping, and merging of data files. This automation results in a seamless process, minimizing human intervention, and eliminating potential errors.


## 2. Data Storage
With the philosophy of 'free, fast, and reliable', the platform utilizes Cloudflare R2, a cost-effective alternative to Amazon S3. This service offered by Cloudflare guarantees efficient data storage, ensuring data accessibility and availability at all times. The use of Parquet, a columnar storage file format, ensures optimal read/write speed and storage efficiency.


## 3. Data Processing and Access
Engage AI Data Platform offers two versatile alternatives for interacting with the data. For users who prefer SQL, `DuckDB` with `HTTPFS` is provided to enable direct reading from the Cloudflare R2 storage. This approach ensures a convenient and SQL-friendly interface for data analysis. Alternatively, for Python enthusiasts, the platform supports `Polars`/`Pandas` libraries along with `boto3` for caching data from the storage, allowing analysts to utilize a familiar, Pythonic approach to data manipulation.


## 4. Data Dashboard ([Guide](SUPERSET.md))
For a holistic view of the data, the platform incorporates Apache Superset, a modern, enterprise-ready business intelligence web application. With the DuckDB plugin, Superset provides interactive and customizable dashboards, allowing analysts to perform real-time data exploration. This service can be hosted either in a Cloud VM or locally, ensuring flexibility and convenience for the researchers.
