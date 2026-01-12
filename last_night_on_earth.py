import sys
from time import sleep
import time 











def print_lyrics():
    lines = [
        ("You are the moonlight of my life", 0.1),
        ("Every night", 0.15),
        ("Givin' all my love to you", 0.13),
        ("My beatin' heart belongs to you", 0.12),
        ("I walked for miles 'til I found you", 0.12),

        ("I'm here to honour you", 0.12),
        ("If I lose everything in the fire", 0.12),
        ("I'm sendin' all my love to you", 0.12),
        

    ]

    delays = [1.2, 1.8, 4.7, 4.2, 3.8,
              1, 1 , 1.2 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
