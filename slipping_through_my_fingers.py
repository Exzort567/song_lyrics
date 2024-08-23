import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("What happened to those wonderful adventures", 0.1),
        ("The places I had planned for us to go?", 0.1),
        ("Well, some of that we did,", 0.1),
        ("but most we didn't", 0.1),

        ("And why?", 0.1),
        ("I just don't know", 0.11),
        ("Slipping through my fingers all the time", 0.07),


    ]

    delays = [1.8, 2.2, 0.4, 0.4,
              0.3, 1, 3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
