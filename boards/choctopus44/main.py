import board

from kb import KMKKeyboard
from kmk.keys import KC, ModifierKey, make_key
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.combos import Combos, Combo, Chord, Sequence
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.quickpin.pro_micro.nice_nano_v2 import pinout as pins
from kmk.hid import HIDModes
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()

layers = Layers()
holdtap = HoldTap()
mouse_key = MouseKeys()
combos = Combos()
encoder_handler = EncoderHandler()
tapdance = TapDance()

holdtap.tap_time = 250
holdtap.prefer_hold = False

keyboard.modules = [layers, combos, holdtap, mouse_key,encoder_handler,tapdance]
keyboard.extensions.append(MediaKeys())

encoder_handler.pins = (
    # reversed direction encoder with no button handling and divisor of 2
    (pins[4], pins[5], None, False, 2,), # encoder #2
    )

# Cleaner key names
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

combos.combos = [
    Chord((hml0[shft_ind], KC.SPC), KC.UNDERSCORE),
    Chord((hmr0[-(shft_ind+1)], KC.SPC), KC.UNDERSCORE),
    Chord((hml0[ctrl_ind], KC.SPC), KC.TAB),
    Chord((hmr0[-(ctrl_ind+1)], KC.SPC), KC.TAB),
    Chord((hml0[shft_ind], KC.BSPC), KC.DEL),
    Chord((hmr0[-(shft_ind+1)], KC.BSPC), KC.DEL),
    Chord((KC.Z,KC.X),KC.LCTRL(KC.Z)),
    Chord((KC.X,KC.C),KC.LCTRL(KC.X)),
    Chord((KC.C,KC.V),KC.LCTRL(KC.C)),
    Chord((KC.V,KC.B),KC.LCTRL(KC.V)),
    Chord((KC.C,KC.V,KC.B),KC.LCTRL(KC.LSFT(KC.V))),
]


combo_layers = {
  (1, 2): 3,
   }
keyboard.modules.append(Layers(combo_layers))

# fmt: off
keyboard.keymap = [
    [  # default_layer
        KC.ESC, KC.Q, KC.W, KC.E, KC.LT(1, KC.R), KC.T, KC.Y, KC.LT(1, KC.U), KC.I, KC.O, KC.P, KC.BSLASH,
        KC.TAB] + hml0 + [KC.LT(2, KC.G), KC.LT(2, KC.H)] + hmr0 +[ KC.QUOT,
        #KC.TILDE,KC.EXCLAIM, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLSH,
        KC.EXCLAIM, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLSH,KC.TILDE,
        KC.F1, KC.TG(2), KC.SPC, KC.TD(KC.TO(1),KC.TO(2),KC.TO(3)), KC.ENT, KC.BSPC, KC.TG(1), KC.LGUI
    ],
    [  # lower_layer
        KC.ESC, KC.ASTR, KC.N7, KC.N8, KC.N9, KC.PLUS, KC.F3, KC.F4, KC.UP, KC.F5, KC.F6, KC.F7,
        KC.CIRC] + hml1+ [KC.DOT, KC.EQL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.F9, KC.F10,
        KC.TO(0), KC.SLSH, KC.N1, KC.N2, KC.N3, KC.MINS, KC.F2, KC.HOME, KC.PGDN, KC.END, KC.PGUP, KC.F12,
        KC.F1, KC.TG(2), KC.SPC, KC.TD(KC.TO(0),KC.TO(2),KC.TO(3)), KC.ENT, KC.BSPC, KC.TG(1), KC.TO(3)
    ],
    [  # raise_layer
        KC.ESC, KC.GRAVE,XXXXXXX, KC.BSLASH, KC.SLSH, KC.LSFT(KC.N9), KC.EXCLAIM, KC.AMPR, KC.PIPE, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.TAB, KC.HASH, KC.LCBR, KC.LPRN, KC.LBRC, KC.HASH, KC.CIRC, KC.RBRC, KC.RPRN, KC.RCBR, KC.MINS, KC.EQL,
        KC.TO(0), XXXXXXX, XXXXXXX, KC.PERC, KC.DOLLAR, KC.UNDS, XXXXXXX, KC.AT, KC.ASTR, XXXXXXX, KC.TILDE, XXXXXXX,
        KC.F1, KC.TG(2), KC.SPC,KC.TD(KC.TO(0),KC.TO(1),KC.TO(3)), KC.ENT, KC.BSPC, KC.TG(1), KC.TO(3)
    ],
    [  # adjust_layer
        KC.RELOAD, KC.RESET, KC.BOOTLOADER, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.UP, KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.AUDIO_VOL_UP,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN, KC.RIGHT, XXXXXXX, KC.AUDIO_VOL_DOWN,
        #KC.BLE_REFRESH, KC.BLE_DISCONNECT, KC.HID, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN, KC.RIGHT, XXXXXXX, KC.AUDIO_VOL_DOWN,
        KC.TO(0), XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.AUDIO_MUTE,
        _______, KC.TO(0), KC.SPC, KC.TD(KC.TO(0),KC.TO(1),KC.TO(2)), KC.ENT, KC.BSPC, KC.TO(0), _______
    ],
]

encoder_handler.map = [ ((KC.UP, KC.DOWN),), # Layer 1
                        (( KC.LCTRL(KC.EQUAL),  KC.LCTRL(KC.MINUS)),), # Layer 2
                        ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP),), # Layer 3
                        ((KC.UP, KC.DOWN),), # Layer 4
                      ]

# fmt:on

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)#, secondary_hid_type=HIDModes.BLE, ble_name='choctopus')
