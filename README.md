# Adafruit Rotary Volume Control Switch
Use a rotary encoder switch to control the volume of the audio playing on your devices.

## Devices currently supported
This list is not exhaustive and include only devices that were tested.
It is likely to work if your device can provide enough power and support generic USB controllers.
* iPhone (iOS 15.2.1)
* MacBook Pro (macOS Monterey 12.1)

# What you will need
## Hardware
* 1x [Adafruit Rotary Trinkey](https://www.adafruit.com/product/4964)
* 1x [Rotary Encoder + Extras](https://www.adafruit.com/product/377)
* 1x Soldering Iron
* 1x Solder Wire

### Optional (based on your device)
* 1x USB-A to USB-C Adapter
* 1x USB-A to Lightning Adapter
* 1x USB-A to Micro-USB Adapter

# How to get started (macOS)
## Step 1 - Solder Components
Solder the rotary encoder on the board. There are five solder points.

## Step 2 - Download CircuitPython
[Download the latest stable release](https://circuitpython.org/board/adafruit_rotary_trinkey_m0/) of CircuitPython that will work with the Rotary Trinkey.

## Step 3 - Install CircuitPython
Plug your board into your computer and double-click on the reset button. Once the reset button has been double-clicked, the RGB status LED located under the board should be solid green.

A new disk named `TRINKEYBOOT` should have appeared in your Finder. Drag and drop at its root the UF2 file previously downloaded during step 2. The disk will automatically disappear before appearing under the name `CIRCUITPYTHON`.

### Troubleshooting - The RGB status LED is solid red
If the RGB status LED is red, try using a different port or a different adapter. If you used a cable, be sure to use a data-sync cable.

## Step 4 - Download `main.py`
Download the `main.py` [file from the repository](main.py) and add it at the root of your `CIRCUITPYTHON` drive.

## Step 5 - Control the volume level on your device
Plug it to [any supported device](#devices-currently-supported) and turn the rotary switch to the right or to the left to increase/decrease the volume.