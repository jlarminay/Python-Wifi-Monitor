import datetime
import time
import os
from . import cleaner

last_status = None
log_directory = "/home/pi/logs/"  # Replace with your desired directory
log_filename = "internet_status.log"
log_location = os.path.join(log_directory, log_filename)

# Function to write status with timestamp to a file
def write_status_to_file(status):
    global last_status

    if(status == last_status):
        return
    
    last_status = status
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Check if the directory exists, and create it if not
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Write the status to the file
    with open(log_location, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {status}\n")

# Function to read the status log from the file
def read_status_log():
    status_log = []
    try:
        with open(log_location, "r", encoding="utf-8") as file:
            for line in file:
                status_log.append(line.strip())
        return status_log
    except FileNotFoundError:
        return []

# Function to parse the status log and calculate the required information
def analyze_status_log():
    status_log = read_status_log()
    status_log.reverse()

    count_in_30_days = 0
    longest_disconnect = None
    entires = []

    all_disconnect_durations = []
    last_disconnected_time = None

    for entry in status_log:
        timestamp_str, status = entry.strip().split(" - ", 1)
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

        if "disconnected" in status:
            entires.append({
                "status": "Disconnected",
                "timestamp": cleaner.clean_datetime(timestamp),
                "duration": 0
            })
            last_disconnected_time = timestamp
            count_in_30_days += 1
        elif "connected" in status:
            disconnected_duration = 0
            if last_disconnected_time:
                disconnected_duration = last_disconnected_time - timestamp
                last_disconnected_time = None
                all_disconnect_durations.append(disconnected_duration)
            
            entires.append({
                "status": "Connected",
                "timestamp": cleaner.clean_datetime(timestamp),
                "duration": cleaner.time_difference(disconnected_duration)
            })
        elif "started" in status:
            entires.append({
                "status": "Started",
                "timestamp": cleaner.clean_datetime(timestamp),
                "duration": 0
            })

        if (datetime.datetime.now() - timestamp).days > 30:
            break

    return {
        "count_in_30_days": count_in_30_days,
        "longest_disconnect": longest_disconnect,
        "average_disconnect": sum(disconnected_duration) / len(disconnected_duration) if len(disconnected_duration) > 0 else 0,
        "entires": entires
    }
