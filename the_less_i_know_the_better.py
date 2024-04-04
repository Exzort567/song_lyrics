import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("she said", 0.08),
        ("\u2018It's not now or never", 0.08),
        ("wait ten years, we'll be together\u2019", 0.08),
        ("I said,", 0.1),
        ("\u2018Better late than never", 0.1),
        ("just don't make me wait forever\u2019", 0.1),
        ("Don't make me wait", 0.09),
        ("forever", 0.07),
       
    ]

    delays = [0.2, 1.3, 0.8, 0.3, 0.6, 5, 0.2, 4]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
