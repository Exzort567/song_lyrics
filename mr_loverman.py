import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("I've shattered now, I'm spilling out", 0.13),
        ("Upon this linoleum ground", 0.15),
        ("I'm reeling in my brain again", 0.17),
        ("Before it can get back to you", 0.13),
        ("Oh what am I", 0.15),
        ("Supposed to do", 0.13),
        ("Without you?", 0.15),

        ("I'm Mr. Loverman", 0.16),
        ("And I miss my lover, man", 0.12),
        ("I'm Mr. Loverman", 0.13),
        ("Oh, and I miss my lover", 0.13),
    ]

    delays = [ 0.8, 1.3, 0.8, 1.2, 1.2, 1.2, 3.5,
               2.3, 2.5, 2.5, 1.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
