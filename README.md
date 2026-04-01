#  NYC Taxi Data Batch Processing Pipeline

A scalable batch-processing data pipeline built using **PySpark, Docker, and Apache Airflow** to analyze NYC Yellow Taxi trip data.

---

##  Overview
This project demonstrates a data engineering pipeline designed to process large-scale, time-series data efficiently. It follows a **microservices-based architecture** and supports batch processing for analytics use cases.

---

##  Architecture
![Architecture Diagram](architecture_diagram.png)

**Flow:**
Data Source → Ingestion → PySpark Processing → Parquet Storage → Airflow Scheduling

---

##  Technologies Used
- **PySpark** – Distributed data processing  
- **Docker** – Containerization & microservices  
- **Apache Airflow** – Workflow scheduling  
- **Parquet** – Optimized storage format  

---

##  Microservices
- **Ingestion Service**: Loads raw CSV data  
- **Processing Service**: Cleans and aggregates data using PySpark  
- **Storage Layer**: Stores processed data in Parquet format  
- **Scheduler**: Automates batch jobs using Airflow  

---

##  Reliability & Scalability
- Docker ensures service isolation and reproducibility  
- PySpark enables distributed processing of large datasets  
- Airflow provides reliable job scheduling  

---

##  How to Run
```bash
docker-compose up
python ingestion/ingest_data.py
python processing/pyspark_job.py
