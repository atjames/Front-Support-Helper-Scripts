import requests
import json
import time
from datetime import datetime, timezone

# ============================================================================
# CONFIGURATION - Modify these values as needed
# ============================================================================

# API Configuration
API_URL = "https://api2.frontapp.com/"
API_TOKEN = "API_TOKEN_HERE"
HTTP_METHOD = "POST"  # Supported: GET, POST, PUT, PATCH, DELETE

# Request Payload (only used for POST, PUT, PATCH methods)
PAYLOAD = {
}

# Success Status Codes (add or remove as needed)
# Common success codes: 200 (OK), 201 (Created), 202 (Accepted), 204 (No Content)
SUCCESS_CODES = {200, 201, 202, 204}

# Run Configuration
NUM_RUNS = 1                    # How many times the request will repeat
MAX_RETRIES = 3                 # How many retry attempts per run
DELAY_BETWEEN_RETRIES = 2       # Seconds to wait between retry attempts
DELAY_BETWEEN_RUNS = 2          # Seconds to wait between different runs

# File Configuration
LOG_FILENAME = "api_responses.txt"

# Timezone Configuration
USE_UTC_TIMEZONE = False  # Set to True for UTC timestamps, False for local timezone

# ============================================================================
# DO NOT MODIFY BELOW THIS LINE (unless you know what you're doing hehe)
# ============================================================================

# Prepare headers
headers = {
    'Authorization': f'Bearer {API_TOKEN}', 
}

def get_timestamp():
    """Get timestamp with timezone information based on configuration"""
    if USE_UTC_TIMEZONE:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
    else:
        return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

def log_response_to_file(response, run_num, attempt_num, timestamp):
    """Log the API response to file with timestamp, run number, and attempt number"""
    with open(LOG_FILENAME, "a", encoding="utf-8") as file:
        file.write("=" * 80 + "\n")
        file.write(f"RUN #{run_num} - ATTEMPT #{attempt_num} - {timestamp}\n")
        file.write(f"HTTP Method: {HTTP_METHOD}\n")
        file.write(f"Status Code: {response.status_code}\n")
        
        # Only log payload for methods that use it
        if HTTP_METHOD.upper() in ['POST', 'PUT', 'PATCH']:
            file.write("Request Payload:\n")
            file.write(json.dumps(PAYLOAD, indent=2) + "\n")
        else:
            file.write("Request Payload: None (GET/DELETE request)\n")
            
        file.write("-" * 40 + "\n")
        file.write("Response:\n")
        
        if response.content:
            try:
                data = response.json()
                file.write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
            except json.decoder.JSONDecodeError:
                file.write(f"Raw response content: {response.text}\n")
        else:
            file.write("No content returned\n")
        
        file.write("=" * 80 + "\n\n")

def make_api_request_with_retry(run_num, max_retries=3, delay_seconds=3):
    """Make API request with retry logic"""
    
    for attempt in range(1, max_retries + 1):
        timestamp = get_timestamp()
        print(f"\n--- Run #{run_num} - Attempt #{attempt} ({HTTP_METHOD}) at {timestamp} ---")
        
        try:
            # Make request using configured method
            method = HTTP_METHOD.upper()
            if method in ['POST', 'PUT', 'PATCH']:
                # Methods that typically include a payload
                response = requests.request(method, API_URL, json=PAYLOAD, headers=headers)
            else:
                # Methods that typically don't include a payload (GET, DELETE)
                response = requests.request(method, API_URL, headers=headers)
            
            # Log every response to file
            log_response_to_file(response, run_num, attempt, timestamp)
            
            # Check if request was successful
            if response.status_code in SUCCESS_CODES:
                if response.content:
                    print(f"✅ Request successful with status {response.status_code}. Content returned.")
                    try:
                        data = response.json()
                        print("Response data:", data)
                        print(f"✅ Response logged to {LOG_FILENAME}")
                        return response  # Success, exit the retry loop
                    except json.decoder.JSONDecodeError as e:
                        print(f"⚠️  JSON decoding error: {e}")
                        print(f"Raw response content: {response.text}")
                        print(f"✅ Response logged to {LOG_FILENAME}")
                        return response  # Still consider it successful
                else:
                    print(f"✅ Request successful with status {response.status_code}. No content returned.")
                    print(f"✅ Response logged to {LOG_FILENAME}")
                    return response  # Success, exit the retry loop
            else:
                print(f"❌ Request failed with status {response.status_code}")
                try:
                    data = response.json()
                    print("Error response:", data)
                except json.decoder.JSONDecodeError as e:
                    print(f"JSON decoding error: {e}")
                    print(f"Raw response content: {response.text}")
                
                print(f"✅ Response logged to {LOG_FILENAME}")
                
                # If this isn't the last attempt, wait before retrying
                if attempt < max_retries:
                    print(f"⏳ Waiting {delay_seconds} seconds before retry...")
                    time.sleep(delay_seconds)
                else:
                    print(f"❌ All {max_retries} attempts failed.")
                    return response  # Return the last failed response
                    
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error on Run #{run_num} - Attempt #{attempt}: {e}")
            
            # Log network errors to file as well
            with open(LOG_FILENAME, "a", encoding="utf-8") as file:
                file.write("=" * 80 + "\n")
                file.write(f"RUN #{run_num} - ATTEMPT #{attempt} - {timestamp}\n")
                file.write(f"HTTP Method: {HTTP_METHOD}\n")
                file.write(f"Network Error: {str(e)}\n")
                
                # Only log payload for methods that use it
                if HTTP_METHOD.upper() in ['POST', 'PUT', 'PATCH']:
                    file.write("Request Payload:\n")
                    file.write(json.dumps(PAYLOAD, indent=2) + "\n")
                else:
                    file.write("Request Payload: None (GET/DELETE request)\n")
                    
                file.write("=" * 80 + "\n\n")
            
            if attempt < max_retries:
                print(f"⏳ Waiting {delay_seconds} seconds before retry...")
                time.sleep(delay_seconds)
            else:
                print(f"❌ All {max_retries} attempts failed due to network errors.")
                return None

# Initialize the log file with a header
with open(LOG_FILENAME, "w", encoding="utf-8") as file:
    file.write(f"API Testing Log - Started at {get_timestamp()}\n")
    file.write(f"HTTP Method: {HTTP_METHOD}\n")
    file.write(f"Endpoint: {API_URL}\n")
    file.write(f"Configuration: {NUM_RUNS} runs, {MAX_RETRIES} retries per run, {DELAY_BETWEEN_RETRIES}s retry delay, {DELAY_BETWEEN_RUNS}s run delay\n\n")

# Execute multiple runs of the API request with retry logic
print(f"🚀 Starting {NUM_RUNS} runs of {HTTP_METHOD} requests with retry logic...")
run_results = []

for run in range(1, NUM_RUNS + 1):
    print(f"\n{'='*60}")
    print(f"🔄 STARTING RUN #{run} of {NUM_RUNS}")
    print(f"{'='*60}")
    
    # Add a run separator to the log file
    with open(LOG_FILENAME, "a", encoding="utf-8") as file:
        file.write(f"\n{'*'*100}\n")
        file.write(f"STARTING RUN #{run} of {NUM_RUNS} - {get_timestamp()}\n")
        file.write(f"{'*'*100}\n\n")
    
    response = make_api_request_with_retry(run, max_retries=MAX_RETRIES, delay_seconds=DELAY_BETWEEN_RETRIES)
    
    if response:
        run_results.append(f"Run #{run}: HTTP {response.status_code}")
        print(f"✅ Run #{run} completed with status {response.status_code}")
    else:
        run_results.append(f"Run #{run}: Network error")
        print(f"❌ Run #{run} failed with network error")
    
    # Wait between runs (except for the last run)
    if run < NUM_RUNS:
        print(f"⏳ Waiting {DELAY_BETWEEN_RUNS} seconds before next run...")
        time.sleep(DELAY_BETWEEN_RUNS)

print(f"\n{'='*60}")
print("🏁 ALL RUNS COMPLETED")
print(f"{'='*60}")
print("📊 Summary:")
for result in run_results:
    print(f"  {result}")
print(f"\n📁 All responses logged to {LOG_FILENAME}")
