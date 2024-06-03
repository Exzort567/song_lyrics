import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("I'm gonna pack my things", 0.1, False),
        ("and leave you behind", 0.1, False),
        ("This feeling's old and I know", 0.1, False),
        ("that I've made up my mind", 0.08, False),
        ("I hope you feel what I felt", 0.11, False),
        ("when you shattered my soul", 0.08, False),
        ("'Cause you were cruel and I'm a fool", 0.08, False),
        ("So, please let me go", 0.08, True),

        ("But I love you so", 0.13, False),
        ("please let me go", 0.13, True),
        ("I love you so ", 0.13, False),
        ("please let me go", 0.13, True),
        ("I love you so ", 0.13, False),
        ("please let me go", 0.13, True),
        ("I love you so ", 0.13, False)
    ]

    delays = [0.8, 0.5, 0.5, 0.5, 0.7, 0.5, 0.5, 2.7, 
              1, 0.8, 1, 0.8, 1.1, 0.8, 5]

    for i, (line, char_delay, is_colored) in enumerate(lines):
        if is_colored:
            print("\033[91m", end='')  

        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)

        if is_colored:
            print("\033[0m", end='')  

        time.sleep(delays[i])
        print('')

print_lyrics()
