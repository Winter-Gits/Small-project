import os
os.system("cls")

import time
import sys

def animated_loading_bar(total_steps = 100, time_delay = 0.1):
    for step in range(total_steps + 1):
        #Calculating hash mark in loading bar
        hashes = "\u2593" * step
        #Calculating the remain space in loading bar
        spaces = ' ' * (total_steps - step)
        # Determine the color based on the percentage
        if step <= 30:
            color_code = 31  # Red
        elif step > 10 and step <= 60:
            color_code = 33  # Yellow
        elif step > 60 and step < 100:
            color_code = 93
        else:
            color_code = 32  # Green
        # ANSI escape code for color
        color_start = f"\033[{color_code}m"
        # ANSI escape code to reset color
        color_reset = "\033[0m"
        #Loading bar
        loading_bar = f"{color_start}{hashes}{spaces}| {step}/{total_steps}%"
        #Print loading bar
        print(f"\r{loading_bar}", end="")
        #Update immediately
        sys.stdout.flush()
        #Delay to create animation
        time.sleep(time_delay)
    print("\nDone!")

animated_loading_bar()