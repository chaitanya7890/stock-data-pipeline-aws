import boto3

file_path = "output/aapl_processed.csv"
bucket_name = "stock-data-pipeline-123"
s3_key = "processed/aapl_processed.csv"

s3 = boto3.client('s3')

try:
    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"Uploaded successfully to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print("Upload failed:", e)