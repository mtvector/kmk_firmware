from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.nice_nano_v2 import pinout as pins
from kmk.scanners import DiodeOrientation

col_pins = (
        pins[6],
        pins[7],
        pins[8],
        pins[9],
        pins[10],
        pins[11],
    )

row_pins = (
        pins[19],
        pins[18],
        pins[17],
        pins[16],
        pins[15],
        pins[14],
        pins[13],
        pins[1],
    )

print('row_pins',row_pins)
print('col_pins',col_pins)

class KMKKeyboard(_KMKKeyboard):
    col_pins = col_pins
    row_pins = row_pins
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = pins[0]
    encoder_pin_0 = pins[4]
    encoder_pin_1 = pins[5]

    # fmt: off
    # coord_mapping = [0, 1, 2, 3, 4, 5,         24, 25, 26, 27, 28, 29, 
    #                  8, 9, 10, 11, 12, 13,     32, 33, 34, 35, 36, 37, 
    #                  16, 17, 18, 19, 20, 21,   40, 41, 42, 43, 44, 45, 
    #                  50, 51, 52, 53,           56, 57, 58, 59]
    coord_mapping = [0, 1, 2, 3, 4, 5, 18, 19, 20, 21, 22, 23, 
 6, 7, 8, 9, 10, 11, 24, 25, 26, 27, 28, 29, 
 12, 13, 14, 15, 16, 17, 30, 31, 32, 33, 34, 35, 
 38, 39, 40, 41, 42, 43, 48, 49, 50, 51]

    # fmt: on
