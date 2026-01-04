import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Maybe I'd change for you someday", 0.15),
        ("But I can't help the way I feel", 0.14),
        ("Wish I was good", 0.14),
        ("wish that I could", 0.14),
        ("Give you my love now", 0.14),

        ("But I", 0.14),
        ("neeeeeeeeed", 0.12),
        ("to tell you something", 0.45),

        ("My heart just can't be faithful for long", 0.11),
        ("I swear I'll only make you cry", 0.1),
        

    ]

    delays = [1.5, 1.7, 1.5, 1.3, 0.5,
              0.7 , 0.3 , 0.7 , 
              0.3, 3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
