import os
import shutil
import subprocess

# Specify the GitHub repository URL
repo_url = "https://github.com/jlarminay/Python-Wifi-Monitor.git"

# Specify the local directory where you want to clone the repository
local_dir = "/home/pi/app"  # Replace with your desired directory

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

# Change to the cloned directory
os.chdir(local_dir)

# Specify the script you want to run within the repository
script_to_run = "main.py"

# Check if the script exists
if not os.path.isfile(script_to_run):
    print(f"Script '{script_to_run}' not found in the repository.")
    exit(1)

# Execute the script
try:
    subprocess.run(["python3", script_to_run], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error executing '{script_to_run}':", e)
    exit(1)