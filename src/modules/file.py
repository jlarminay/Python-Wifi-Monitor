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

    count_in_30_days = 0
    longest_disconnect = None
    entires = []

    all_disconnect_durations = []
    last_disconnected_time = None
    last_started_time = None

    for entry in status_log:
        timestamp_str, status = entry.strip().split(" - ", 1)
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

        # check if within 30 days
        if (datetime.datetime.now() - timestamp).days > 30:
            continue

        # skip if caused my midnight restart
        if timestamp.hour == 0 and timestamp.minute < 1:
            continue

        if "disconnected" in status:
            entires.append({
                "status": "Disconnected",
                "timestamp": cleaner.clean_datetime(timestamp),
                "duration": 0
            })
            last_disconnected_time = timestamp.timestamp()
            count_in_30_days += 1
        elif "connected" in status:
            disconnected_duration = None
            if last_disconnected_time:
                disconnected_duration = timestamp.timestamp() - last_disconnected_time
                if longest_disconnect == None or disconnected_duration > longest_disconnect:
                    longest_disconnect = disconnected_duration
                all_disconnect_durations.append(disconnected_duration)
                last_disconnected_time = None
            
                entires.append({
                    "status": "Connected",
                    "timestamp": cleaner.clean_datetime(timestamp),
                    "duration": 0 if disconnected_duration == None else cleaner.time_difference(disconnected_duration)
                })
        elif "started" in status:
            # entires.append({
            #     "status": "Started",
            #     "timestamp": cleaner.clean_datetime(timestamp),
            #     "duration": 0
            # })
            last_started_time = timestamp

    average_disconnect = sum(all_disconnect_durations) / len(all_disconnect_durations) if len(all_disconnect_durations) > 0 else 0
    entires.reverse()

    return {
        "count_in_30_days": count_in_30_days,
        "longest_disconnect": longest_disconnect if longest_disconnect != None else 0,
        "average_disconnect": average_disconnect if average_disconnect != None else 0,
        "last_started_time": last_started_time,
        "entires": entires
    }
