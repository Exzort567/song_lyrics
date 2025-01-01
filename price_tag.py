import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Seems like everybody's", 0.1),
        ("got a price", 0.1),

        ("I wonder how they", 0.1),
        ("sleep at night", 0.1),

        ("when the sale comes first ", 0.1),
        ("and the truth comes second", 0.08),
        ("just stop for a minute and smile :)", 0.1),

        ("why is everybody so serious?", 0.1),
        ("action so damn mysterious", 0.1),

        ("got shades on your eyes", 0.1),
        ("and your heels so high that", 0.1),
        ("you can't even have a good time", 0.1),

        ("everybody look to their left", 0.1),
        ("everybody look to their right", 0.1),

        ("can you feel that? yeah", 0.1),
        ("we're paying with love tonight", 0.1),

        ("it's not about", 0.1),
        ("the money, money, money", 0.1),

        ("we don't need", 0.1),
        ("your money, money, money", 0.1),

        ("we just wanna make", 0.1),
        ("the world dance", 0.1),

        ("forget about the price tag", 0.1),
        
        ("ain't about the, uh,", 0.1),
        ("cha-ching cha-ching", 0.1),

        ("ain't about the, yeah,", 0.1),
        ("ba-bling ba-bling", 0.1),

        ("wanna make the world dance", 0.1),
        ("forget about the price tag", 0.1),
      
      

    ]

    delays = [1, 0.7, 0.5, 0.7, 0.9, 0.3, 2]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
