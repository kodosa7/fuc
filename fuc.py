# resize your terminal to 100 chars wide or more

import time, curses
from data import big_text


text = ["fuck", "you", "corona"]
offsets = [[17, 34, 51, 68], [25, 42, 59], [0, 17, 34, 51, 68, 85]]

def print_one_letter(stdscr):
    curses.curs_set(0)
    for word in text:
        for letter in word:
            if letter in big_text.keys():
                for row in range(7, 15):
                    stdscr.addstr(row, 42, big_text[letter][row - 7])
                    stdscr.refresh()

            time.sleep(.125)
            stdscr.clear()

def print_words(stdscr, style):
    idx = 0
    for word, set in zip(text, offsets):
        for letter in word:
            for row in range(8):
                stdscr.addstr(row + 7, set[idx], big_text[letter][row])
                stdscr.refresh()

            if idx < (len(set) - 1):
                idx += 1
            else:
                idx = 0

            if style == 1:
                time.sleep(.125)
                stdscr.clear()

        if style == 2:
            time.sleep(.25)
            stdscr.clear()

while True:
    curses.wrapper(print_one_letter)
    curses.wrapper(print_words, 1)
    curses.wrapper(print_words, 2)
