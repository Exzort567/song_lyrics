import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("you're all that I want this life", 0.15),
        ("I'll imagine we fell in love", 0.08),
        ("I'll nap under moonlight skies with you", 0.08),
        ("I think I'll picture us, you with the waves", 0.07),
        ("The oceans colors on your face", 0.08),
     
        
    ]

    delays = [3.2, 0.5, 0.5 , 0.5, 5 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
