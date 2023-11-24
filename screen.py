import curses
from curses import wrapper
import time
import random

def start(stdscr):
    stdscr.erase()
    stdscr.addstr("Welcome to the Speed Typing Test")
    stdscr.addstr("\nPress any key to begin.")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, time = 0, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(15, 0, f"WPM: {wpm}")
    stdscr.addstr(16, 0, f"Time: {round(time)}s")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def load_text():
    with open("quotes.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    stdscr.nodelay(True)
    start_time = time.time()

    while True:
        # max() to avoid 0 division error
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.erase()
        display_text(stdscr, target_text, current_text, time_elapsed, wpm)
        stdscr.refresh()
        
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            input = stdscr.getkey()
        except:
            continue

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

    while True:
        wpm_test(stdscr)
        stdscr.addstr(4, 0, "You've completed the text! Press any key to continue...")
        stdscr.getkey()

wrapper(main)
