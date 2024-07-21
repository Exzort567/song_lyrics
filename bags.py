import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Can you see me?", 0.07),
        ("I'm waiting for the right time", 0.07),
        ("I can't read you,", 0.07),
        ("but if you want,", 0.07),
        ("the pleasure's all mine", 0.06),
        ("Can you see me", 0.07),

        ("using everything to hold back?", 0.07),
        ("I guess this could be worse", 0.07),
        ("Walkin' out the door with your bags", 0.07),


    ]

    delays = [0.23, 0.2, 0.2, 0.17, 0.2, 0.2, 
              0.33, 0.2, 3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
