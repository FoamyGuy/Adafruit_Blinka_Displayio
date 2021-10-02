import time
import board
import displayio
from display_setup import setup_display

display = setup_display()

# Create a Group to hold the TileGrid
group = displayio.Group()
# Add the TileGrid to the Group

display.show(group)

time.sleep(1)
