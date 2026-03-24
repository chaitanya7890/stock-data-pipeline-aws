import subprocess

def run_step(step_name, command):
    print(f"\n--- Running: {step_name} ---")
    result = subprocess.run(command, shell=True)
    
    if result.returncode != 0:
        raise Exception(f"{step_name} failed!")
    print(f"{step_name} completed successfully.")

try:
    run_step("Ingestion", "python scripts/get_stock_data.py")
    run_step("Transformation", "python scripts/transform_data.py")
    run_step("Validation", "python scripts/validate_data.py")
    run_step("Upload to S3", "python scripts/upload_to_s3.py")

    print("\n🚀 PIPELINE EXECUTED SUCCESSFULLY 🚀")

except Exception as e:
    print("\n❌ PIPELINE FAILED ❌")
    print(str(e))