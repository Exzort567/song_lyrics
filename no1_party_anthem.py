import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Number one party anthem, yeah, yeah", 0.15),
        ("The look of love, the rush of blood", 0.07),
        ("The She's with me's, the Gallic shrug", 0.1),
        ("The shutterbugs, the Camera Plus", 0.08),
        ("The black & white and the color dodge", 0.07),
        ("The good time girls, the cubicles", 0.05),
        ("The house of fun, the number one", 0.07),
        ("Party anthem, oh", 0.07),
    ]

    delays = [1, 0.3, 0.3, 0.2, 0.6, 0.1, 0.1, 2,]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
