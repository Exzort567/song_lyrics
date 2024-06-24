import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("You're not broken, just bent,", 0.07),
        ("and we can learn to love again", 0.07),
        ("Oh, tear ducts and rust", 0.1),
        ("I'll fix it for us", 0.1),

        ("We're collecting dust,", 0.1),
        ("but our love's enough", 0.1),


    ]

    delays = [0.5, 0.5, 1, 1.1,
              0.5, 3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
