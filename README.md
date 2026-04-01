# NYC Taxi Data Batch Processing Pipeline

🚀 Scalable Batch Data Pipeline using PySpark | Docker | Airflow

## Overview
This project implements a batch-processing data pipeline using PySpark to analyze NYC Yellow Taxi data.

## Technologies Used
- PySpark
- Docker
- Apache Airflow
- Parquet Storage

## Architecture
Data Source → Ingestion → PySpark Processing → Parquet Storage → Visualization

## How to Run
1. Start Docker:
   docker-compose up
2. Run ingestion script:
   python ingestion/ingest_data.py
3. Run PySpark job:
   python processing/pyspark_job.py

## Output
Processed data stored in Parquet format.

## Author
Yashaswini
