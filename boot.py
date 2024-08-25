from kmk.bootcfg import bootcfg
import board
from kmk.quickpin.pro_micro.nice_nano_v2 import pinout as pins

bootcfg(
    # required:
    sense = pins[-1],
    # optional:
    source = pins[-2],
    boot_device: int = 0,
    cdc_console: bool = True,
    cdc_data: bool = False,
    consumer_control: bool = True,
    keyboard: bool = True,
    midi: bool = True,
    mouse: bool = True,
    nkro: bool = False,
    pan: bool = False,
    storage: bool = True,
    usb_id: Optional[tuple[str, str]] = None,
    **kwargs,
) -> bool