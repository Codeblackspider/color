from pyfiglet import figlet_format
from colored import fore, style
import math

def rgb_to_ansi256(r, g, b):
    return 16 + 36 * (r // 51) + 6 * (g // 51) + (b // 51)

def get_gradient_color(start_color, end_color, steps, step):
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    r = int(r1 + (r2 - r1) * step / steps)
    g = int(g1 + (g2 - g1) * step / steps)
    b = int(b1 + (b2 - b1) * step / steps)
    return (r, g, b)

def gradient_text(text, start_color, end_color, steps):
    gradient_text = ""
    for i in range(len(text)):
        color = get_gradient_color(start_color, end_color, len(text), i)
        ansi_color = rgb_to_ansi256(color[0], color[1], color[2])
        gradient_text += f"{fore(ansi_color)}{text[i]}{style('reset')}"
    return gradient_text

# Define the text to display and gradient colors
text = "fontbees"
start_color = (0, 255, 0)  # Green
end_color = (0, 0, 255)    # Blue

# Create the styled text with gradient
figlet_text = figlet_format(text, font="slant")
gradient_text_output = gradient_text(figlet_text, start_color, end_color, len(text))

# Display the gradient text
print(gradient_text_output)
