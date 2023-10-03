import curses
import time
from modules import wifi, screen

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
    # stdscr.curs_set(0)  # Hide the cursor
    setup_colors()  # Initialize custom colors

    try:
        while True:
            stdscr.clear()

            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            current_ip = wifi.get_current_ip()
            wifi_status = wifi.is_wifi_connected()

            # Add text with custom color and attributes
            screen.printOut(stdscr, curses, {
                "current_time": current_time,
                "current_ip": current_ip,
                "wifi_status": wifi_status
            })

            # Check for Enter key press
            key = stdscr.getch()
            if key == 10:  # Enter key
                break

            time.sleep(0.5)  # Wait for 0.5 seconds before updating the information
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    curses.wrapper(main)
