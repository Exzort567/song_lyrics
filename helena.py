import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("because you never learn", 0.08),
        ("a goddamn thing", 0.13),
        ("you're just a sad song", 0.08),
        ("with nothing to say", 0.1),
    ]

    delays = [0.1, 2, 1.3, 0.3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
