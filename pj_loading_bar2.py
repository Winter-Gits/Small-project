import os
os.system("cls")

import os
import time
import sys
import shutil

# Clear the terminal screen
os.system("cls" if os.name == "nt" else "clear")

def animated_loading_bar(total_steps=100, time_delay=0.1):
    def get_loading_info(step):
        if step <= 10:
            return "Loading resources..."
        elif step <= 20:
            return "Loading background..."
        elif step <= 40:
            return "Loading terrain..."
        elif step <= 50:
            return "Loading characters..."
        elif step <= 60:
            return "Loading weapons..."
        elif step <= 85:
            return "Loading structures..."
        elif step > 85 and step < 100:
            return "Loading particles..."
        elif step == 100:
            return "DONE!"

    # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns
    
    for step in range(total_steps + 1):
        # Calculating hash marks in the loading bar
        hashes = "\u2593" * step
        # Calculating the remaining space in the loading bar
        spaces = ' ' * (total_steps - step)
        # Determine the color based on the percentage
        if step <= 10:
            color_code = 31  # Red
        elif step <= 60:
            color_code = 93  # Gold
        elif step < 100:
            color_code = 33  # Yellow
        else:
            color_code = 32  # Green
        # Define the border
        upper_border = "\u2580" * (total_steps + 2)  # Adjust to match the width including the side borders
        lower_border = "\u2584" * (total_steps + 2)  # Adjust to match the width including the side borders
        # Bold the text
        bold_start = "\033[1m"
        bold_end = "\033[0m"
        # ANSI escape code for color
        color_start = f"\033[{color_code}m"
        # Constructing the loading bar string with color
        loading_bar = f"\u2588 {hashes}{spaces} \u2588"
        
        # Get loading info and center it
        loading_info = get_loading_info(step)
        # Add percentage into loading info 
        loading_info_with_percentage = f"{loading_info} {step}/{total_steps}%"
        # Center align each line within the terminal width
        upper_border_line = f"\u2588{upper_border}\u2588".center(terminal_width)
        loading_bar_line = loading_bar.center(terminal_width)
        lower_border_line = f"\u2588{lower_border}\u2588".center(terminal_width)
        loading_info_line = loading_info_with_percentage.center(terminal_width)
        
        # Print upper border, loading bar, lower border, and loading info centered
        print(f"\r{color_start}{upper_border_line}\n{color_start}{loading_bar_line}\n{color_start}{lower_border_line}\n{color_start}{loading_info_line}", end="")
        # Update immediately
        sys.stdout.flush()
        # Delay to create animation
        time.sleep(time_delay)
        # Move the cursor up four lines to overwrite the previous output
        if step < total_steps:
            print("\033[F\033[F\033[F\033[F", end="")

# Call the function to display the animated loading bar
animated_loading_bar()