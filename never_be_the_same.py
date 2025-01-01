import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("just", 0.05),
        ("one hit", 0.05),
        ("of you", 0.05),
        ("I knew", 0.05),
        ("I'll never", 0.08),
        ("be the", 0.07),
        ("same", 0.05),

        ("its you,", 0.08),
        ("babe", 0.08),
        ("and i'm,", 0.08),
        ("a sucker", 0.08),
        ("for the way", 0.08),
        ("that you move", 0.08),
        ("babe", 0.05),

        ("and i", 0.05),
        ("could try", 0.05),
        ("to run", 0.05),
        ("but it", 0.08),
        ("would be", 0.08),
        ("useless", 0.2),
        ("you're", 0.05),

        ("to blame", 0.05),
        ("just", 0.05),
        ("one hit", 0.05),
        ("of you", 0.05),
        ("I knew", 0.05),
        ("I'll never", 0.05),
        ("ever ever", 0.05),
        ("be the same", 0.05),
      

    ]

    delays = [0.07, 0.07, 0.07, 0.07, 0.07, 0.06, 0.8,
              0.1, 0.3, 0.07, 0.07, 0.07, 0.06, 0.1,
              0.4, 0.05, 0.07, 0.05, 0.08, 0.06, 0.3,
              0.07, 0.6, 0.05, 0.07, 0.05, 0.08, 0.06,
              0.3,]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
