import board

from kb import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.combos import Combos, Combo, Chord, Sequence
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.quickpin.pro_micro.nice_nano_v2 import pinout as pins

keyboard = KMKKeyboard()

layers = Layers()
holdtap = HoldTap()
mouse_key = MouseKeys()
combos = Combos()
encoder_handler = EncoderHandler()

holdtap.tap_time = 350

keyboard.modules = [layers, combos, holdtap, mouse_key,encoder_handler]
keyboard.extensions.append(MediaKeys())

encoder_handler.pins = (
    # reversed direction encoder with no button handling and divisor of 2
    (pins[4], pins[5], None, False, 2,), # encoder #2
    )

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

mods_before_modmorph = set()
def modmorph(names = {'DUMMY_KEY',}, default_kc = KC.NO, morphed_kc = KC.NO, triggers = {KC.LSHIFT, KC.RSHIFT}):
    def _pressed(key, state, KC, *args, **kwargs):
        global mods_before_modmorph
        mods_before_modmorph = triggers.intersection(state.keys_pressed)
        # if a trigger is held, morph key
        if mods_before_modmorph:
            state._send_hid()
            for mod_kc in mods_before_modmorph:
                # discard triggering mods so morphed key is unaffected by them
                state.keys_pressed.discard(mod_kc)
            state.keys_pressed.add(morphed_kc)
            state.hid_pending = True
            return state
        # else return default keycode
        state.keys_pressed.add(default_kc)
        state.hid_pending = True
        return state
    def _released(key, state, KC, *args, **kwargs):
        if {morphed_kc,}.intersection(state.keys_pressed):
            state.keys_pressed.discard(morphed_kc)
            for mod_kc in mods_before_modmorph:
                # re-add previously discarded shift so normal typing isn't impacted
                state.keys_pressed.add(mod_kc)
        else:
            state.keys_pressed.discard(default_kc)
        state.hid_pending = True
        return state
    modmorph_key = make_key(names=names, on_press=_pressed,
                            on_release=_released)
    return modmorph_key

combos.combos = [
    Chord((KC.LSFT, KC.SPC), KC.UNDERSCORE),
    Chord((KC.RSFT, KC.SPC), KC.UNDERSCORE),
    Chord((KC.LCTRL, KC.SPC), KC.TAB),
    Chord((KC.RCTRL, KC.SPC), KC.TAB),
    Chord((KC.LSFT, KC.BSPC), KC.DEL),
    Chord((KC.RSFT, KC.BSPC), KC.DEL),
]

modmorph({'SPC_UNDERSCORE'}, KC.SPC, KC.UNDERSCORE, triggers = {KC.LSHIFT, KC.RSHIFT})

combo_layers = {
  (1, 2): 3,
   }
keyboard.modules.append(Layers(combo_layers))

# fmt: off
keyboard.keymap = [
    [  # default_layer
        KC.ESC, KC.Q, KC.W, KC.E, KC.LT(1, KC.R), KC.T, KC.Y, KC.LT(1, KC.U), KC.I, KC.O, KC.P, KC.BSLASH,
        KC.TAB, KC.HT(KC.A, KC.LGUI), KC.HT(KC.S, KC.LALT), KC.HT(KC.D, KC.LCTRL), KC.HT(KC.F, KC.LSFT), KC.LT(2, KC.G), KC.LT(2, KC.H), KC.HT(KC.J, KC.RSFT), KC.HT(KC.K, KC.RCTRL), KC.HT(KC.L, KC.RALT), KC.HT(KC.SCLN, KC.RGUI), KC.QUOT,
        KC.EXCLAIM, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.QUESTION, KC.SLSH,
        KC.F1, KC.TG(1), KC.SPC_UNDERSCORE, KC.LSFT, KC.ENT, KC.BSPC, KC.TG(2), KC.LGUI
    ],
    [  # lower_layer
        KC.ESC, KC.SLSH, KC.N7, KC.N8, KC.N9, KC.PLUS, KC.F3, KC.F4, KC.UP, KC.F5, KC.F6, KC.F7,
        KC.CIRC, KC.ASTR, KC.N4, KC.N5, KC.N6, KC.DOT, KC.EQL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.F9, KC.F10,
        KC.TO(0), KC.N0, KC.N1, KC.N2, KC.N3, KC.MINS, KC.COMMA, KC.HOME, KC.PGDN, KC.END, KC.PGUP, KC.F12,
        KC.F1, KC.TG(1), KC.SPC, KC.LSFT, KC.ENT, KC.BSPC, KC.TG(2), KC.F2
    ],
    [  # raise_layer
        KC.ESC, _______, _______, KC.BSLASH, KC.SLSH, KC.LSFT(KC.N9), KC.EXCLAIM, KC.AMPR, KC.PIPE, KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.AUDIO_VOL_UP,
        KC.TAB, KC.CIRC, KC.LCBR, KC.LPRN, KC.LBRC, KC.HASH, KC.TILDE, KC.RBRC, KC.RPRN, KC.RCBR, KC.MINS, KC.AUDIO_VOL_DOWN,
        KC.TO(0), _______, _______, KC.PERC, KC.DOLLAR, KC.UNDS, KC.GRAVE, KC.AT, KC.EQL, _______, KC.TO(3), KC.AUDIO_MUTE,
        KC.F1, KC.TG(1), KC.SPC, KC.LSFT, KC.ENT, KC.BSPC, KC.TG(2), KC.F2
    ],
    [  # adjust_layer
        KC.RELOAD, KC.RESET, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.UP, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.BLE_REFRESH, KC.BLE_DISCONNECT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN, KC.RIGHT, XXXXXXX, XXXXXXX,
        KC.TO(0), XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        _______, KC.TO(0), KC.SPC, KC.LSFT, KC.ENT, KC.BSPC, KC.TO(0), _______
    ],
]

encoder_handler.map = [ ((KC.UP, KC.DOWN),), # Layer 1
                        (( KC.LCTRL(KC.EQUAL),  KC.LCTRL(KC.MINUS)),), # Layer 2
                        ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP),), # Layer 3
                        ((KC.UP, KC.DOWN),), # Layer 4
                      ]

# fmt:on

if __name__ == '__main__':
    keyboard.go()
