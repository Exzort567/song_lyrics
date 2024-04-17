import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Cause you know how to give me that", 0.05),
        ("you know how to pull me back", 0.05),
        ("when I go runnin', runnin'", 0.05),
        ("tryna get away from loving ya", 0.05),
        ("you know how to love me hard", 0.05),
        ("I won't lie, I'm falling hard", 0.05),
        ("yep, I'm falling for ya", 0.05),
        
        ("but there's nothing wrong with that", 0.04),
        ("you da one that I dream", 0.06),
        ("about all day", 0.06),
        ("you da one that I think", 0.06),
        ("about always", 0.06),
        ("you are the one,", 0.06),
        ("so I make sure I'll behave", 0.06),
        ("my love is your love,", 0.06),
        ("your love is my love", 0.06),
        ("you da one that I dream", 0.06),
        ("about all day", 0.06),
        
      

    ]

    delays = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 1, 0.3, 1, 0.3, 0.3 , 0.6, 0.8, 0.6, 2]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
