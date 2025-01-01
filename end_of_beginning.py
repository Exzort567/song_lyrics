import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Remember twenty-four?", 0.13),
        ("And when I'm back in Chicago, I feel it", 0.13),
        ("Another version of me, I was in it", 0.16),
    ]

    delays = [7, 1.4, 1.3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
