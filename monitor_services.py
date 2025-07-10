import os
import socket
import json
import requests
from datetime import datetime
import time

services = ['apache2', 'rabbitmq-server', 'postgresql']
host_name = socket.gethostname()
UPLOAD_URL = "http://localhost:5000/add"

def check_service_status(service):
    status = os.system(f"service {service} status > /dev/null 2>&1")
    return "UP" if status == 0 else "DOWN"

def mkdir_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def write_service_status(service, status):
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"./data/{service}-status-{timestamp}.json"
    data = {
        "service_name": service,
        "service_status": status,
        "host_name": host_name
    }
    with open(filename, "w") as f:
        json.dump(data, f)
    print(f"✅ Written status to {filename}")
    return filename

def upload_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            files = {'file': (os.path.basename(filepath), f)}
            response = requests.post(UPLOAD_URL, files=files)
            if response.status_code == 201:
                print(f"📤 Uploaded {filepath} successfully.")
            else:
                print(f"❌ Failed to upload {filepath}. Status: {response.status_code}")
    except Exception as e:
        print(f"❗ Error uploading {filepath}: {e}")

def main():
    mkdir_if_not_exists("./data")
    print(f"\n🔍 Monitoring services on host: {host_name}")
    print("🛠️ Services to monitor:", ", ".join(services))
    for service in services:
        status = check_service_status(service)
        filepath = write_service_status(service, status)
        print(f"🔧 {service} is {status}")
        print(f"📂 Status file created: {filepath}")
        upload_file(filepath)

if __name__ == "__main__":
    while True:
        try:
            main()
            print("😴 Sleeping for 5 seconds...\n\n\n")
            time.sleep(5)
        except KeyboardInterrupt:
            print("🛑 Monitoring stopped by user.")
            break
        except Exception as e:
            print(f"💥 An error occurred: {e}")
            break
