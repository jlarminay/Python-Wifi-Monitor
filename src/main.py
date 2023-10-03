import curses
import time
from modules import get_current_ip, is_wifi_connected

# Color pair constants
RED_ON_BLACK = 1
GREEN_ON_BLACK = 2

def setup_colors():
    curses.start_color()
    curses.init_pair(RED_ON_BLACK, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(GREEN_ON_BLACK, curses.COLOR_GREEN, curses.COLOR_BLACK)

def main(stdscr):
    # Don't wait for Enter key press when calling getch()
    stdscr.nodelay(1)
    stdscr.clear()
    setup_colors()  # Initialize custom colors

    try:
        while True:
            stdscr.clear()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            current_ip = get_current_ip.get_current_ip()
            wifi_status = is_wifi_connected.is_wifi_connected()
            wifi_status_string = "Connected to Wi-Fi" if wifi_status else "Not connected to Wi-Fi"

            # Add text with custom color and attributes
            stdscr.addstr(0, 0, f"Current Time: {current_time}")
            stdscr.addstr(1, 0, f"Current IP: {current_ip}")
            stdscr.addstr(2, 0, wifi_status_string, curses.color_pair(GREEN_ON_BLACK if wifi_status else RED_ON_BLACK))
            stdscr.addstr(4, 0, "------------------------------")
            stdscr.addstr(5, 0, "")
            stdscr.refresh()

            # Check for Enter key press
            key = stdscr.getch()
            if key == 10:  # Enter key
                break

            time.sleep(0.5)  # Wait for 0.5 seconds before updating the information
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    curses.wrapper(main)
