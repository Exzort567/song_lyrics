import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("I'm not the kind of fool", 0.09),
        ("Who's gonna sit and sing to you,", 0.087),
        ("About stars, girl.", 0.18),

        ("But last night I looked up into", 0.09),
        ("The dark half of the \033[34mblue\033[0m,", 0.07),
        ("And they'd gone backwards.", 0.1),

        ("Something in your magnetism", 0.09),
        ("Must have pissed them off,", 0.09),
        ("Forcing them to get an early night.", 0.1),
    ]

    delays = [0.2, 1.8, 0.7, 
              0.2, 1.5, 1.7, 
              0.15, 1.4, 3 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
