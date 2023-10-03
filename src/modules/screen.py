# Color pair constants
RED_ON_BLACK = 1
GREEN_ON_BLACK = 2
BLUE_ON_BLACK = 3

def printOut(stdscr, curses, items):
    wifi_status_string = "Connected to Wi-Fi" if items['wifi_status'] else "Not connected to Wi-Fi"

    # Add text with custom color and attributes
    stdscr.addstr(0, 0, f"Current Time: \t{items['current_time']}")
    stdscr.addstr(1, 0, f"Last restart: \t{items['last_started_time']}")
    stdscr.addstr(2, 0, f"Current IP: {items['current_ip']}")
    stdscr.addstr(3, 0, wifi_status_string, curses.color_pair(GREEN_ON_BLACK if items['wifi_status'] else RED_ON_BLACK))
    stdscr.addstr(4, 0, "------------------------------")
    stdscr.addstr(5, 0, f"CPU Usage: \t{items['cpu_usage']}%")
    stdscr.addstr(6, 0, f"RAM Usage: \t{items['ram_usage']}%")
    stdscr.addstr(7, 0, f"CPU Temp: \t{items['cpu_temperature']}°C")
    stdscr.addstr(8, 0, "------------------------------")
    stdscr.addstr(9, 0, f"Count in 30 days: \t{items['count_in_30_days']}")
    stdscr.addstr(10, 0, f"Longest disconnect: \t{items['longest_disconnect']}")
    stdscr.addstr(11, 0, f"Average disconnect: \t{items['average_disconnect']}")
    stdscr.addstr(12, 0, "------------------------------")
    stdscr.addstr(13, 0, "Status Log:")
    for i, entry in enumerate(items['entires']):
        row = 14
        if entry['status'] == "Disconnected":
            stdscr.addstr(row + i, 0, f"{entry['status']} \t{entry['timestamp']}", curses.color_pair(RED_ON_BLACK))
        elif entry['status'] == "Connected":
            if entry['duration'] == 0:
                stdscr.addstr(row + i, 0, f"{entry['status']} \t{entry['timestamp']}", curses.color_pair(GREEN_ON_BLACK))
            else:
                stdscr.addstr(row + i, 0, f"{entry['status']} \t{entry['timestamp']} \t({entry['duration']})", curses.color_pair(GREEN_ON_BLACK))
        else:
            stdscr.addstr(row + i, 0, f"{entry['status']} \t{entry['timestamp']}", curses.color_pair(BLUE_ON_BLACK))

        if i >= 20:
            break
    # stdscr.addstr(4, 0, f"LDT: {items['last_disconnect_time']}")
    # stdscr.addstr(5, 0, f"LDD: {items['last_disconnect_duration']}")
    # stdscr.addstr(6, 0, f"Count: {items['disconnect_count']}")
    # stdscr.addstr(7, 0, "")
    stdscr.refresh()
