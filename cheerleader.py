import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("She gives me love", 0.07),
        ("and affection", 0.07),
        ("Baby, did I mention?", 0.1),
        ("You're the only girl for me", 0.08),
        ("No, I don't need the next one", 0.07),
        ("Mama loves you too", 0.05),
        ("She thinks I made the right selection", 0.07),
        ("Now all that's left to do", 0.07),
        ("Is just for me to pop the question", 0.07)
    ]

    delays = [0.06, 0.3, 0.3, 0.2, 0.6, 0.1, 0.1, 0.1, 5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
