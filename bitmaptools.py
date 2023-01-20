import displayio


def fill_region(dest_bitmap: displayio.Bitmap, x1: int, y1: int, x2: int, y2: int, value: int):
    x_counter = 1 if x1 <= x2 else -1
    y_counter = 1 if y1 <= y2 else -1
    #print(f"x counter: {x_counter}")
    #print(f"y counter: {y_counter}")

    #print(f"y range: {y1} - {y2}")
    #print(f"x range: {x1} - {x2}")
    for y_pixel in range(y1, y2, y_counter):
        for x_pixel in range(x1, x2, x_counter):

            if 0 <= x_pixel < dest_bitmap.width and \
                    0 <= y_pixel < dest_bitmap.height:

                #print(f"({x_pixel}, {y_pixel}) is in bounds")
                dest_bitmap[x_pixel, y_pixel] = value
            else:
                pass
                #print(f"({x_pixel}, {y_pixel}) is out of bounds")

    #print("after loops")