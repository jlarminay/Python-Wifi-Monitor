import curses
import time

def main(stdscr):
    # Don't wait for Enter key press when calling getch()
    stdscr.nodelay(1)
    stdscr.clear()

    try:
        while True:
            stdscr.clear()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            stdscr.addstr(0, 0, f"Current Time: {current_time}")
            stdscr.refresh()
            
            # Check for Enter key press
            key = stdscr.getch()
            if key == 10:  # Enter key
                break

            time.sleep(0.5)  # Wait for 1 second before updating the time
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    curses.wrapper(main)
