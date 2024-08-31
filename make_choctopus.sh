#Download same circuitpython and matching mpy builds
#https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/nice_nano/en_US/
#https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/mpy-cross/linux-amd64/
#https://github.com/adafruit/Adafruit_nRF52_Bootloader/releases
#Install circuitpython, set system mpy to the correct version
#make sure clean-dist is on if you're changing anything because of silly caching
conda activate kmk

make compile copy-compiled copy-board clean-dist MPY_SOURCES='kmk/ lib/' BOARD='boards/choctopus44' MOUNTPOINT='/media/mt/CIRCUITPY'
