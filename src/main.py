import curses
import time
import modules import get_current_ip, is_wifi_connected

def main(stdscr):
    # Don't wait for Enter key press when calling getch()
    stdscr.nodelay(1)
    stdscr.clear()

    try:
        while True:
            stdscr.clear()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            current_ip = get_current_ip.get_current_ip()
            wifi_status = "Connected to Wi-Fi" if is_wifi_connected.is_wifi_connected() else "Not connected to Wi-Fi"

            stdscr.addstr(0, 0, f"Current Time: {current_time}")
            stdscr.addstr(1, 0, f"Current IP: {current_ip}")
            stdscr.addstr(2, 0, wifi_status)
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
