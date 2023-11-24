import curses
from curses import wrapper


def main(stdscr):
    stdscr.erase()
    stdscr.addstr("Hello World!")
    stdscr.refresh()
    stdscr.getkey()     # waits for user input

wrapper(main)
