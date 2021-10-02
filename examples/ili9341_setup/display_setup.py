import time
import board
import displayio
import adafruit_ili9341

def setup_display():
    # Release any resources currently in use for the displays
    displayio.release_displays()

    spi = board.SPI()
    tft_cs = board.CE0
    tft_dc = board.D25

    display_bus = displayio.FourWire(
        spi, command=tft_dc, chip_select=tft_cs, reset=board.D24
    )
    display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)
    return display
