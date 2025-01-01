import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("I had all and then most of you", 0.08),
        ("Some and now none of you", 0.08),
        ("Take me back to the night we met", 0.11),
    ]

    delays = [0.1, 2.8, 4]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
