import time
import displayio
from adafruit_progressbar import ProgressBar
from displayio.pygame_display import Display

# Make the display context
splash = displayio.Group(max_size=10)
display = Display(None, None, width=1770, height=920)
display.show(splash)

# set progress bar width and height relative to board's display
width = display.width - 40
height = 30

x = display.width // 2 - width // 2
y = display.height // 3

# Create a new progress_bar object at (x, y)
progress_bar = ProgressBar(x, y, width, height, 1.0)

# Append progress_bar to the splash group
splash.append(progress_bar)

current_progress = 0.0


while display.running:
    # range end is exclusive so we need to use 1 bigger than max number that we want
    for current_progress in range(0, 101, 1):
        #print("Progress: {}%".format(current_progress))
        progress_bar.progress = current_progress / 100  # convert to decimal
        time.sleep(0.01)
    time.sleep(0.3)
    progress_bar.progress = 0.0
    time.sleep(0.3)