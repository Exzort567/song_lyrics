import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("But when he loves me", 0.09),
        ("I feel like I'm floating", 0.1),
        ("When he calls me pretty", 0.1),
        ("I feel like somebody", 0.12),

        ("Even when we fade", 0.12),
        ("eventually to nothing", 0.13),

        ("You will always be my", 0.11),
        ("favorite form of loving", 0.1),
        

    ]

    delays = [0.2, 0.5, 0.4, 0.5,
              0.5 , 0.5, 
              0.3, 3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
