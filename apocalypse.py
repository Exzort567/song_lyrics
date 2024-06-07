import sys
from time import sleep
import time

def apply_gradient(text):
    # Define the gradient colors for an "apocalypse" vibe
    colors = [
        "\033[38;5;88m",  # Dark red
        "\033[38;5;130m", # Orange-red
        "\033[38;5;94m",  # Deep orange
        "\033[38;5;136m", # Orange
        "\033[38;5;166m", # Dark orange
        "\033[38;5;202m", # Red-orange
        "\033[38;5;208m", # Orange-red
        "\033[38;5;124m", # Red
        "\033[38;5;88m"   # Dark red
    ]
    
    gradient_text = ''
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        gradient_text += color + char
    gradient_text += "\033[0m"  # Reset color
    return gradient_text

def print_lyrics():
    lines = [
        ("Got the music in you, baby", 0.08),
        ("Tell me why", 0.08),
        ("Got the music in you, baby", 0.08),
        ("Tell me why", 0.08),

        ("You've been locked in here forever", 0.05),
        ("And you just can't say goodbye", 0.09),
        
        ("Your lips, my lips", 0.09),
        ("Apocalypse", 0.009),
        ("Your lips, my lips", 0.09),
        ("Apocalypse", 0.009)
    ]

    delays = [0.1, 2, 0.3, 2, 
              0.2, 6.6, 
              1.2, 6.4, 1.2, 5]

    for i, (line, char_delay) in enumerate(lines):
        if "Apocalypse" in line:
            line = line.replace("Apocalypse", apply_gradient("Apocalypse"))
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
