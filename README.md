# 📈 Stock Data Pipeline on AWS

An end-to-end data engineering pipeline that ingests stock market data, performs transformation and validation, and uploads processed data to AWS S3.

---

## 🚀 Project Overview

This project demonstrates a complete data pipeline built using Python and AWS. It simulates a real-world ETL workflow where data is ingested from an external source, processed, validated, and stored in cloud storage.

---

## ⚙️ Tech Stack

- Python
- pandas
- yfinance (Yahoo Finance API)
- boto3 (AWS SDK)
- AWS S3
- Git & GitHub

---

## 🏗️ Architecture


Yahoo Finance API
↓
Data Ingestion (Python)
↓
Data Transformation (Cleaning + Feature Engineering)
↓
Data Validation (Schema + Quality Checks)
↓
AWS S3 (Cloud Storage)


---

## 📂 Project Structure


stock-sentiment-pipeline/
│
├── scripts/
│ ├── get_stock_data.py
│ ├── transform_data.py
│ ├── validate_data.py
│ ├── upload_to_s3.py
│ └── run_pipeline.py
│
├── output/ # Ignored (generated data)
├── requirements.txt
├── .gitignore
└── README.md


---

## 🔄 Pipeline Flow

### 1. Data Ingestion
- Fetches stock data using `yfinance`
- Stores raw data locally

### 2. Data Transformation
- Cleans column names
- Converts data types
- Adds derived features:
  - Price change
  - Percentage change
  - Moving average

### 3. Data Validation
- Ensures required columns exist
- Checks for duplicates
- Validates numeric values
- Enforces business rules

### 4. Cloud Upload
- Uploads processed dataset to AWS S3 using `boto3`

---

## ▶️ How to Run the Pipeline

1. Create virtual environment
python -m venv venv
.\venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Configure AWS credentials
aws configure

Enter:
AWS Access Key ID
AWS Secret Access Key
Region: us-east-1
Output format: json

4. Run the pipeline
python scripts/run_pipeline.py

☁️ Output
Processed data is uploaded to AWS S3:
s3://stock-data-pipeline-123/processed/aapl_processed.csv

📊 Key Features
End-to-end ETL pipeline
Modular pipeline design
Data cleaning and feature engineering
Data validation layer for reliability
AWS S3 cloud integration
Automated pipeline execution

🔐 Security
AWS credentials are NOT stored in the repository
Sensitive files are excluded using .gitignore

🚀 Future Enhancements
Add Apache Airflow for scheduling and orchestration
Integrate real-time streaming (Kafka or AWS Kinesis)
Build dashboards using Power BI or Tableau
Store data in AWS Redshift for analytics
Add CI/CD pipeline

👨‍💻 Author
Chaitanya Sri Arimanda
Data Engineer | Cloud & AWS
