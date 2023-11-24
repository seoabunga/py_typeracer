import curses
from curses import wrapper

def start(stdscr):
    stdscr.erase()
    stdscr.addstr("Welcome to the Speed Typing Test")
    stdscr.addstr("\nPress any key to begin.")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!"
    current_text = []

    while True:
        stdscr.erase()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()
        
        input = stdscr.getkey()

        # handling backspace in different os
        if input in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(input)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start(stdscr)
    wpm_test(stdscr)

wrapper(main)
