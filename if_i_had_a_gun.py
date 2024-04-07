import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("let me fly you to the moon", 0.1),
        ("my eyes have always", 0.1),
        ("followed you around the room", 0.1),
        ("cause you're the only", 0.1),
        ("God that I will ever need", 0.1),
        ("i'm holding on and", 0.08),
        ("waiting for the moment to find me", 0.1),
      

    ]

    delays = [1, 0.7, 0.5, 0.7, 0.9, 0.3, 2]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
