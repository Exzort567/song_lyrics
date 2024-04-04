import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("I was over love,", 0.04),
        ("though I had enough,", 0.05),
        ("then I found you,", 0.06),
        ("oh I was, no doubt, stressed out", 0.1),
        ("without you", 0.08),
        ("All we got is us,", 0.1),
        ("when nobody does, ", 0.07),
        ("I got you", 0.07),
        ("For your sanity and my mentality", 0.1),
        ("Could you tell where my head", 0.08),
        ("was at when you found me", 0.05)

    ]

    delays = [0.3, 0.3, 0.3, 0.3, 0.4, 0.3, 0.1, 0.6, 0.07, 0.3, 0.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
