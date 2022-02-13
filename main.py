# Adafruit Rotary Volume Control Switch
#
# Julien Widmer
# https://github.com/julienwidmer/adafruit-rotary-volume-control-switch
import board
import neopixel
import digitalio
import rotaryio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)

# Rotary Encoder Switch
encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB)
last_position = encoder.position

switch = digitalio.DigitalInOut(board.SWITCH)
switch.switch_to_input(pull=digitalio.Pull.DOWN)

previous_switch_value = False
mute_status = False

# NeoPixel LED
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixels.brightness = 0.1  # set brightness to 10%
pixels.fill((0, 255, 0))  # set to green

while True:
    # Mute/unmute
    if switch.value and not previous_switch_value:
        if mute_status:
            print("Mute: OFF")
        else:
            print("Mute: ON")

        mute_status = not mute_status
        cc.send(ConsumerControlCode.MUTE)

        # Prevent unwanted mute toggling when user does not release the button
        while switch.value:
            previous_switch_value = True
        previous_switch_value = False

    # Adjust volume level
    current_position = encoder.position
    position_change = int(current_position - last_position)
    last_position = current_position

    if position_change < 0:
        print("- Decreased Volume -")
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    elif position_change > 0:
        print("+ Increased Volume +")
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
