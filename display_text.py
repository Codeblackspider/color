from colorama import Fore, Style, init
from pyfiglet import figlet_format

# Initialize Colorama
init()

# Define the text to display
text = "fontbees"

# Create the styled text
styled_text = figlet_format(text, font="slant")

# Display the text in green color
print(Fore.GREEN + styled_text + Style.RESET_ALL)
