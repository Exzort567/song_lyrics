import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Sometimes when I'm lonely", 0.08),
        ("I sit and think about him", 0.06),
        ("And it hurts to remember ", 0.06),
        ("all the good times", 0.06),

        ("When I thought I could ", 0.06),
        ("never live without him", 0.06),

        ("And I wonder does it have to be the same", 0.08),
        ("Every time", 0.08),
        ("when I see him,", 0.08),
        ("will it bring back all the pain?", 0.07),
        ("Ah-ha-ha,", 0.08),
        ("how can I forget that name?", 0.08),

    ]

    delays = [0.2, 0.1, 0.1, 0.1,
              0.1, 0.1, 
              1.4, 0.8, 0.4, 0.9, 0.5, 4]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
