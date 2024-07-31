import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("When you lose something you cannot replace", 0.11),
        ("Tears stream", 0.11),
        ("down your face", 0.11),
        ("I promise you I will learn from my mistakes", 0.12),
    ]

    delays = [2.4, 1.7, 1.7, 1.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
