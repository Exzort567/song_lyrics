import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Of all the ones that cried their way", 0.09),
        ("I'm still waiting on you", 0.09),
        ("Maybe we seek for something that", 0.08),
        ("We couldn't ever have", 0.1),
        ("Maybe we choose the only love", 0.1),
        ("We know we won't accept", 0.1)
    ]

    delays = [0.5, 1, 1, 1, 0.5, 3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
