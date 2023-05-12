# Engage AI Data Platform

## Introduction

Engage AI Data Platform is an end-to-end data management solution providing a suite of services to manage the entire data lifecycle. It includes data ingestion, storage, processing, access, and governance. This repository will initialize the data platform, ingest World Bank data to datalake, and provide a guide to interact with the data.

## Requirements
- Python 3.7+
- A VM with Docker for Apache Superset
- [Cloudflare R2](https://developers.cloudflare.com/r2/) storage as datalake

## Installation
Clone this repository and install the required packages:

```bash
git clone https://github.com/n0k0m3/engage-ai-datalake
cd Engage-AI-Data-Platform
# Create a virtual environment
python3 -m venv .venv
# Activate the virtual environment
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

For initial data ingest to datalake, follow the instructions in [pipelines/README.md](pipelines/README.md).