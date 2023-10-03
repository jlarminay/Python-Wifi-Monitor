import os
import shutil
import subprocess
import requests

# Specify the GitHub repository URL
repo_url = "https://github.com/jlarminay/Python-Wifi-Monitor.git"
# Specify the local directory where you want to clone the repository
local_dir = "/home/pi/app"
# Specify the script you want to run within the repository
script_to_run = "start.py"

# Function to check internet connectivity
def is_connected_to_internet():
    try:
        # Attempt to send a request to a known website (e.g., google.com)
        requests.get("https://github.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Function to set permissions recursively
def set_permissions(path):
    os.chmod(path, 0o755)
    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for dirname in dirnames:
                os.chmod(os.path.join(dirpath, dirname), 0o755)
            for filename in filenames:
                os.chmod(os.path.join(dirpath, filename), 0o755)

# Check if connected to the internet
if is_connected_to_internet():
    print("Connected to the internet")

    # Check if the target directory already exists
    if os.path.exists(local_dir):
        try:
            # Remove the existing directory and its contents
            shutil.rmtree(local_dir)
            print(f"Removed existing directory: {local_dir}")
        except Exception as e:
            print(f"Error removing existing directory: {e}")
            exit(1)

    # Clone the repository
    try:
        subprocess.run(["git", "clone", repo_url, local_dir], check=True)
        print("Repository cloned successfully.")
    except subprocess.CalledProcessError as e:
        print("Error cloning repository:", e)
        exit(1)

else:
    print("Not connected to the internet. Cannot download the repository.")

# Change to the cloned directory
os.chdir(local_dir)

# Check if the script exists
if not os.path.isfile(script_to_run):
    print(f"Script '{script_to_run}' not found in the repository.")
    exit(1)

# Set permissions recursively for the cloned directory
set_permissions(local_dir)

# Execute the script
try:
    subprocess.run(["python3", script_to_run], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error executing '{script_to_run}':", e)
    exit(1)
