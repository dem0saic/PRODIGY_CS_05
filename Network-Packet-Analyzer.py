from pyfiglet import figlet_format
from termcolor import colored
from termcolor import cprint

# Print the title of the program
title = "Network Packet Analyzer"
title_ascii = figlet_format(title, font="speed", width=100)

# Define colors
colors = ["white", "green", "blue"]

# Split the title into words
title_words = title_ascii.split('\n')

# Blend colors for each word
blended_title = []
for i, line in enumerate(title_words):
    if i < len(title_words) // 2:
        color = colors[0]
    elif i < len(title_words) * 3 // 4:
        color = colors[1]
    else:
        color = colors[2]
    blended_title.append(colored(line, color))

# Print the blended title
print("\n".join(blended_title))


# Display the creator of the program with their social handles
creator_info = """
Created by: Dem0saic
GitHub: https://github.com/dem0saic
LinkedIn: https://www.linkedin.com/in/owusuvincent/
"""
creator_colored = colored(creator_info, color="white")
print(creator_colored)

