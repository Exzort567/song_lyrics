import sys
from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

console = Console()

def print_lyrics():
    lines = [
        ("Is it a crime to be unsure?", 0.2),
        ("In time, we'll find if it's sustainable", 0.18),
        ("You're pure, you're kind, mature, divine", 0.18),
        ("You might be too good for me, unattainable", 0.15),
    ]

    delays = [0.23, 2, 0.2, 2]
    
    console.clear()
    title = Text("♪ Who Knows ♪", style="bold #851D20", justify="center")
    console.print(Panel(title, box=box.DOUBLE, border_style="#851D20", padding=(1, 1), width=40))
    console.print()
    
    colors = ["#851D20", "#A52428", "#C52B30", "#E53238"]
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            console.print(char, style=f"bold {colors[i]}", end='')
            sys.stdout.flush()
            sleep(char_delay)
        
        sleep(delays[i])
        console.print()

if __name__ == "__main__":
    try:
        print_lyrics()
    except KeyboardInterrupt:
        sys.exit(0)