import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Think I'll miss you forever", 0.07),
        ("Like the stars miss the sun in the morning sky", 0.08),
        ("Later's better than never", 0.08),
        ("Even if you're gone, I'm gonna drive", 0.09),
     
        
    ]

    delays = [ 1.3, 1.3 , 1.3, 5 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
