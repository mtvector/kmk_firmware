import board
import gc
from kb import KMKKeyboard
from kmk.keys import KC, ModifierKey, make_key
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.quickpin.pro_micro.nice_nano_v2 import pinout as pins
#from kmk.hid import HIDModes
from kmk.modules.tapdance import TapDance

def get_key_from_coordinates(layer, hand, row, col):
    return keymap[layer][hand][row][col]

def flatten_keymap_layers(keymap):
    # Flatten each layer from a list of lists to a single list
    return [[key for row in layer for col in row for key in col] for layer in keymap]

keyboard = KMKKeyboard()

layers = Layers()
holdtap = HoldTap()
combos = Combos()
encoder_handler = EncoderHandler()
tapdance = TapDance()

holdtap.tap_time = 200
holdtap.prefer_hold = False
holdtap.tap_interrupted = True

keyboard.modules = [layers, combos, holdtap,encoder_handler,tapdance]
keyboard.extensions.append(MediaKeys())

encoder_handler.pins = (
    # reversed direction encoder with no button handling and divisor of 2
    (pins[4], pins[5], None, False, 2,), # encoder #2
    )

# Cleaner key name
_______ = KC.TRNS
XXXXXXX = KC.NO

ctrl_ind = 2
shft_ind = 3
    
lmods = [KC.LGUI, KC.LALT, KC.LCTRL, KC.LSFT]
rmods = [KC.RSFT,KC.RCTRL, KC.RALT, KC.RGUI]
hrl0 = [KC.A, KC.S, KC.D,KC.F]
hrr0 = [KC.J,KC.K,KC.L,KC.SCLN]
hrl1 = [KC.N0, KC.N4, KC.N5, KC.N6]
hml0 = [KC.HT(k,m) for k,m in zip(hrl0,lmods)]
hmr0 = [KC.HT(k,m) for k,m in zip(hrr0,rmods)]
hml1 = [KC.HT(k,m) for k,m in zip(hrl1,rmods)]

keymap = [
    [  # default_layer
        [[KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T], [KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSLASH]],
        [[KC.TAB] + hml0 + [KC.LT(2, KC.G)], [KC.LT(2, KC.H)] + hmr0 + [KC.QUOT]],
        [[KC.EXCLAIM, KC.Z, KC.X, KC.C, KC.LT(1, KC.V), KC.B], [KC.N, KC.LT(1, KC.M), KC.COMMA, KC.DOT, KC.SLSH, KC.TILDE]],
        [[KC.F1, KC.TG(2), KC.SPC, KC.TD(KC.TO(1), KC.TO(2), KC.TO(3))], [KC.ENT, KC.BSPC, KC.TG(1), KC.LGUI]]
    ],
    [  # lower_layer
        [[KC.ESC, KC.ASTR, KC.N7, KC.N8, KC.N9, KC.PLUS], [KC.F3, KC.F4, KC.UP, KC.F5, KC.F6, KC.F7]],
        [[KC.CIRC] + hml1 + [KC.DOT], [KC.EQL,KC.LEFT, KC.DOWN, KC.RIGHT, KC.F9,XXXXXXX]],
        [[KC.TO(0), KC.SLSH, KC.N1, KC.N2, KC.N3, KC.MINS], [KC.F2, KC.HOME, KC.PGDN, KC.END, KC.PGUP,XXXXXXX]],
        [[KC.F12, KC.F1, KC.TG(2), KC.SPC, KC.TD(KC.TO(0), KC.TO(2), KC.TO(3))], [KC.ENT, KC.BSPC, KC.TG(1), KC.TO(3)]]
    ],
    [  # raise_layer
        [[KC.ESC, KC.GRAVE, KC.PERC, KC.BSLASH, KC.PIPE, KC.SLSH], [KC.EXCLAIM, KC.AMPR, KC.PIPE, XXXXXXX, XXXXXXX, XXXXXXX]],
        [[KC.TAB, KC.CIRC, KC.LCBR, KC.LPRN, KC.LBRC, KC.HASH], [KC.EQL, KC.RBRC, KC.RPRN, KC.RCBR, KC.HASH, XXXXXXX]],
        [[KC.TO(0), XXXXXXX, XXXXXXX, XXXXXXX, KC.UNDS, KC.MINS], [KC.DOLLAR, KC.AT, KC.ASTR, XXXXXXX, XXXXXXX, XXXXXXX]],
        [[KC.F1, KC.TG(2), KC.SPC, KC.TD(KC.TO(0), KC.TO(1), KC.TO(3))], [KC.ENT, KC.BSPC, KC.TG(1), KC.TO(3)]]
    ],
    [  # adjust_layer
        [[KC.RELOAD, KC.RESET, KC.BOOTLOADER, XXXXXXX, XXXXXXX, XXXXXXX], [XXXXXXX, XXXXXXX, KC.UP, KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.AUDIO_VOL_UP]],
        [[XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX], [XXXXXXX, KC.LEFT, KC.DOWN, KC.RIGHT, XXXXXXX, KC.AUDIO_VOL_DOWN]],
        [[KC.TO(0), XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX], [XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.AUDIO_MUTE]],
        [[_______, KC.TO(0), KC.SPC, KC.TD(KC.TO(0), KC.TO(1), KC.TO(2))], [KC.ENT, KC.BSPC, KC.TO(0), _______]]
    ]
]

combos_coordinates = [ #Combos across all layers
    (((1, 0, 4), (3, 0, 2)), KC.UNDERSCORE),  
    (((1, 1, 1), (3, 0, 2)), KC.UNDERSCORE),  
    (((1, 0, 3), (3, 0, 2)), KC.TAB),  
    (((1, 1, 2), (3, 0, 2)), KC.TAB),  
    (((1, 0, 4), (3, 1, 1)), KC.DEL),  
    (((1, 1, 1), (3, 1, 1)), KC.DEL),  
    (((0, 0, 1), (0, 0, 2)), KC.ESC),  
    (((1, 0, 1), (1, 0, 2)), KC.TAB),  
    # (((2, 0, 1), (2, 0, 2)),KC.LCTRL(KC.Z)), 
    # (((2, 0, 2), (2, 0, 3)),KC.LCTRL(KC.X)),
    # (((2, 0, 3), (2, 0, 4)),KC.LCTRL(KC.C)),
    # (((2, 0, 4), (2, 0, 5)),KC.LCTRL(KC.V)),
    # (((2, 0, 3), (2, 0, 4), (2, 0, 5)),KC.LCTRL(KC.LSFT(KC.V))),
    ]

def generate_combos(keymap, combos_coordinates, layers=[0]):
    for layer_idx in layers:
        for combo in combos_coordinates:
            key_coords, output = combo
            yield Chord(
                tuple(get_key_from_coordinates(layer_idx, hand, row, col) for hand, row, col in key_coords),
                output
            )

combo_list = list(generate_combos(keymap, combos_coordinates,[0,1,2]))

combo_list += [
    Chord((hmr0[-2],hmr0[-1]),KC.QUOT),
    Chord((KC.O, KC.P), KC.BSLASH),
    Chord((KC.SLSH, KC.DOT), KC.TILDE),
    Chord((hml1[0], hml1[1]), KC.CIRC),
    Chord((KC.Z,KC.X),KC.LCTRL(KC.Z)),
    Chord((KC.X,KC.C),KC.LCTRL(KC.X)),
    Chord((KC.C,KC.V),KC.LCTRL(KC.C)),
    Chord((KC.V,KC.B),KC.LCTRL(KC.V)),
    Chord((KC.C,KC.V,KC.B),KC.LCTRL(KC.LSFT(KC.V)))
]

combos.combos = combo_list

combo_layers = {
  (1, 2): 3,
   }
keyboard.modules.append(Layers(combo_layers))

# fmt: off
keyboard.keymap = flatten_keymap_layers(keymap)

encoder_handler.map = [ ((KC.UP, KC.DOWN),), # Layer 1
                        (( KC.LCTRL(KC.EQUAL),  KC.LCTRL(KC.MINUS)),), # Layer 2
                        ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP),), # Layer 3
                        ((KC.UP, KC.DOWN),), # Layer 4
                      ]

# fmt:on
if __name__ == '__main__':
    keyboard.go()#keyboard.go(hid_type=HIDModes.USB)#, secondary_hid_type=HIDModes.BLE, ble_name='choctopus')