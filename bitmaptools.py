import time
from typing import Tuple

from displayio import Bitmap

import displayio


def fill_region(dest_bitmap: displayio.Bitmap, x1: int, y1: int, x2: int, y2: int, value: int):
    x_counter = 1 if x1 <= x2 else -1
    y_counter = 1 if y1 <= y2 else -1

    for y_pixel in range(y1, y2, y_counter):
        for x_pixel in range(x1, x2, x_counter):

            if 0 <= x_pixel < dest_bitmap.width and \
                    0 <= y_pixel < dest_bitmap.height:

                dest_bitmap[x_pixel, y_pixel] = value
            else:
                pass


def draw_line(
        bitmap: Bitmap,
        x_0: int,
        y_0: int,
        x_1: int,
        y_1: int,
        color: int,
) -> None:
    _line_on(bitmap, (x_0, y_0), (x_1, y_1), color)


def _safe_draw(
        bitmap: displayio.Bitmap,
        point: Tuple[int, int],
        color: int,
) -> None:
    (x, y) = point
    if 0 <= x < bitmap.width and 0 <= y < bitmap.height:
        bitmap[x, y] = color


def _line_on(
        bitmap: displayio.Bitmap,
        p_0: Tuple[int, int],
        p_1: Tuple[int, int],
        color: int,
) -> None:
    (x_0, y_0) = p_0
    (x_1, y_1) = p_1

    def pt_on(x, y):
        _safe_draw(bitmap, (x, y), color)

    if x_0 == x_1:
        if y_0 > y_1:
            y_0, y_1 = y_1, y_0
        for _h in range(y_0, y_1 + 1):
            pt_on(x_0, _h)
    elif y_0 == y_1:
        if x_0 > x_1:
            x_0, x_1 = x_1, x_0
        for _w in range(x_0, x_1 + 1):
            pt_on(_w, y_0)
    else:
        steep = abs(y_1 - y_0) > abs(x_1 - x_0)
        if steep:
            x_0, y_0 = y_0, x_0
            x_1, y_1 = y_1, x_1

        if x_0 > x_1:
            x_0, x_1 = x_1, x_0
            y_0, y_1 = y_1, y_0

        d_x = x_1 - x_0
        d_y = abs(y_1 - y_0)

        err = d_x / 2

        if y_0 < y_1:
            ystep = 1
        else:
            ystep = -1

        for x in range(x_0, x_1 + 1):
            if steep:
                pt_on(y_0, x)
            else:
                pt_on(x, y_0)
            err -= d_y
            if err < 0:
                y_0 += ystep
                err += d_x


def boundary_fill(dest_bitmap: Bitmap,
                  x: int, y: int,
                  fill_color_value: int,
                  replaced_color_value: int):
    print(f"found {dest_bitmap[x, y]} at ({x}, {y})")

    def _append_unique(_list, value):
        if value not in _list:
            _list.append(value)


    # if (dest_bitmap[x, y] == replaced_color_value):
    #     dest_bitmap[x, y] = fill_color_value
    #     #time.sleep(0.001)
    #
    #     boundary_fill(dest_bitmap, x+1, y, fill_color_value, replaced_color_value)
    #     boundary_fill(dest_bitmap, x-1, y, fill_color_value, replaced_color_value)
    #     boundary_fill(dest_bitmap, x, y+1, fill_color_value, replaced_color_value)
    #     boundary_fill(dest_bitmap, x, y-1, fill_color_value, replaced_color_value)

    _fill_points = []

    if (dest_bitmap[x, y] == replaced_color_value):
        dest_bitmap[x, y] = fill_color_value

        _fill_points.append((x + 1, y))
        _fill_points.append((x - 1, y))
        _fill_points.append((x, y + 1))
        _fill_points.append((x, y - 1))

    while len(_fill_points) > 0:
        #time.sleep(0.001)
        _cur_point = _fill_points.pop(0)

        if (dest_bitmap[_cur_point[0], _cur_point[1]] == replaced_color_value):
            dest_bitmap[_cur_point[0], _cur_point[1]] = fill_color_value

            _append_unique(_fill_points, (_cur_point[0] + 1, _cur_point[1]))
            _append_unique(_fill_points, (_cur_point[0] - 1, _cur_point[1]))
            _append_unique(_fill_points, (_cur_point[0], _cur_point[1] + 1))
            _append_unique(_fill_points, (_cur_point[0] - 1, _cur_point[1] - 1))
