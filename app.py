import os
import sys
import time
from dotenv import load_dotenv 
# It loads the .env file (if it exists) into the environment
load_dotenv() 
def mask_secret(secret_value):
    """Masks a secret, showing only the first 4 chars."""
    if secret_value:
        return f"{secret_value[:4]}****"
    return "NOT SET!"

def run_app():
    print(f"Secure Pipeline Running in '{os.environ.get('APP_ENV')}' mode...")
    
    # 1. Load All 10 Secrets
    print("\nLoading Application Secrets...")
    db_pass = os.environ.get("DATABASE_PASSWORD")
    db_user = os.environ.get("DATABASE_USER")
    db_host = os.environ.get("DATABASE_HOST")
    db_name = os.environ.get("DATABASE_NAME")
    
    jwt_key = os.environ.get("JWT_SECRET_KEY")
    stripe_key = os.environ.get("STRIPE_API_KEY")
    
    s3_bucket = os.environ.get("S3_BUCKET_NAME")
    s3_key = os.environ.get("S3_ACCESS_KEY")
    s3_secret = os.environ.get("S3_SECRET_ACCESS_KEY")

    # 2. Validate a few critical secrets 
    if not db_pass or not jwt_key or not s3_key:
        print("\nERROR: A critical secret (DB, JWT, or S3) is missing.")
        sys.exit(1) 
        
    print("All secrets loaded successfully.")

    # 3. Simulate Real Work
    print("\n--- Simulating App Startup ---")
    
    # Simulate database connection
    print(f"Connecting to DB: mysql://{db_user}:{mask_secret(db_pass)}@{db_host}/{db_name}")
    time.sleep(1) 
    
    # Simulate user authentication service
    print(f"Initializing Auth Service with JWT Key: {mask_secret(jwt_key)}")
    time.sleep(1)
    
    # Simulate payment service
    print(f"Initializing Payments with Stripe Key: {mask_secret(stripe_key)}")
    time.sleep(1)
    
    # Simulate file storage service
    print(f"Connecting to S3 Bucket '{s3_bucket}' with Key: {mask_secret(s3_key)}")
    time.sleep(1)

    print("\nProject Demo Complete: All services initialized securely.")

if __name__ == "__main__":
    run_app()