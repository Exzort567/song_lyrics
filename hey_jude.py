import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("And anytime you,", 0.06),
        ("feel the pain,", 0.08),
        ("Hey, Jude, refrain,", 0.1),

        ("Don't carry the world", 0.12),
        ("upon your shoulders", 0.09),
        ("For well you know", 0.08),

        ("that it's a fool ", 0.08),
        ("Who plays it cool", 0.1),
        ("By making his world", 0.08),

        ("a little colder", 0.2),
        ("Na, na na, na na,", 0.1),
        ("na na, na na", 0.15)

    ]

    delays = [0.12, 0.23, 0.6, 
              0.5, 3, 0.3, 
              0.5, 0.7, 0.8, 
              1, 0.1, 2]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
