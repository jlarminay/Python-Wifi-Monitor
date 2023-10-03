import curses
import signal
import time
import sys
from modules import wifi, screen, file, cleaner, system

# Color pair constants
RED_ON_BLACK = 1
GREEN_ON_BLACK = 2
BLUE_ON_BLACK = 3

def setup_colors():
    curses.start_color()
    curses.init_pair(RED_ON_BLACK, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(GREEN_ON_BLACK, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(BLUE_ON_BLACK, curses.COLOR_BLUE, curses.COLOR_BLACK)

def exit_handler():
    file.write_status_to_file("stopped")
    sys.exit(0)

def main(stdscr):
    # Don't wait for Enter key press when calling getch()
    stdscr.nodelay(1)
    stdscr.clear()
    # stdscr.curs_set(0)  # Hide the cursor
    setup_colors()  # Initialize custom colors

    file.write_status_to_file("started")

    try:
        while True:
            stdscr.clear()

            wifi_status = wifi.is_wifi_connected()
            file.write_status_to_file('connected' if wifi_status else 'disconnected')

            file_analyzed = file.analyze_status_log()

            # Add text with custom color and attributes
            screen.printOut(stdscr, curses, {
                "current_time": cleaner.clean_datetime(time),
                "last_started_time": cleaner.clean_datetime(file_analyzed['last_started_time']),
                "current_ip": wifi.get_current_ip(),
                "wifi_status": wifi_status,
                #
                "cpu_usage": system.get_cpu_usage(),
                "ram_usage": system.get_ram_usage(),
                "cpu_temperature": system.get_cpu_temperature(),
                #
                "count_in_30_days": file_analyzed['count_in_30_days'],
                "longest_disconnect": cleaner.time_difference(file_analyzed['longest_disconnect']),
                "average_disconnect": cleaner.time_difference(file_analyzed['average_disconnect']),
                #
                "entires": file_analyzed['entires'],
            })

            # Check for Enter key press
            key = stdscr.getch()
            if key == 10:  # Enter key
                exit_handler()
                break

            time.sleep(0.5)  # Wait for 0.5 seconds before updating the information
    except KeyboardInterrupt:
        pass

signal.signal(signal.SIGTERM, exit_handler)

if __name__ == "__main__":
    curses.wrapper(main)
