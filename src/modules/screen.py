# Color pair constants
RED_ON_BLACK = 1
GREEN_ON_BLACK = 2

def printOut(stdscr, curses, items):
    wifi_status_string = "Connected to Wi-Fi" if items.wifi_status else "Not connected to Wi-Fi"

    # Add text with custom color and attributes
    stdscr.addstr(0, 0, f"Current Time: {items.current_time}")
    stdscr.addstr(1, 0, f"Current IP: {items.current_ip}")
    stdscr.addstr(2, 0, wifi_status_string, curses.color_pair(GREEN_ON_BLACK if items.wifi_status else RED_ON_BLACK))
    stdscr.addstr(3, 0, "------------------------------")
    stdscr.addstr(4, 0, "")
    stdscr.refresh()