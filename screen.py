import curses
from curses import wrapper

def start(stdscr):
    stdscr.erase()
    stdscr.addstr("Welcome to the Speed Typing Test")
    stdscr.addstr("\nPress any key to begin.")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!\n"
    current_text = []

    while True:
        stdscr.erase()
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
        stdscr.refresh()
        
        input = stdscr.getkey()

        # handling backspace in different os
        if input in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(input)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start(stdscr)
    wpm_test(stdscr)

wrapper(main)
