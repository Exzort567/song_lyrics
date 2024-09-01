import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Whenever I see girls and boys", 0.10),
        ("Selling lanterns on the streets", 0.095),
        ("I remember the Child", 0.12),
        ("In the manger, as he sleeps", 0.11),

    ]

    delays = [ 0.13, 0.15, 0.5, 
              2 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
































