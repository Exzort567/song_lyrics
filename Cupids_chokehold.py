import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("I love it when she calls my phone", 0.05),
        ("She even got her very own ringtone", 0.06),
        ("If that ain't love then I don't know what love is", 0.08),

        ("We even got a secret handshake", 0.05),
        ("And she loves the music that my band makes", 0.06),
        ("I know I'm young but if I had to choose her or the sun", 0.06),
        ("I'd be one nocturnal son of a gun", 0.08),
        
    ]

    delays = [0.13, 0.7, 3.6, 
              0.15, 0.3, 0.2    , 3 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
