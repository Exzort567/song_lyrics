import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Number one party anthem, yeah, yeah", 0.2),
        ("The look of love, the rush of blood", 0.1),
        ("The She's with me's, the Gallic shrug", 0.1),
        ("The shutterbugs, the Camera Plus", 0.13),
        ("The black & white and the color dodge", 0.1),
        ("The good time girls, the cubicles", 0.1),
        ("The house of fun, the number one", 0.13),
        ("Party anthem, oh", 0.2),
    ]

    delays = [1.5, 0.35, 0.36, 0.35, 0.38, 0.43, 2, 2,]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
