# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# -*- coding: utf-8 -*-

import time
import locale
from datetime import datetime
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from computer import current_computer
from multiprocessing import Process, Pipe
from ext_temp import get_temp

SLEEP_TIME = 6

# Set locale to current country
# OS must have it installed, in raspberry pi os -> dpkg-reconfigure locales
locale.setlocale(locale.LC_ALL, "es_ES.UTF_8")

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 270

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonPrev = digitalio.DigitalInOut(board.D24)
buttonNext = digitalio.DigitalInOut(board.D23)
buttonPrev.switch_to_input()
buttonNext.switch_to_input()

def write_in_screen(date, IP, CPU, MemUsage, Disk, Temp):
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Write four lines of text.
    y = top
    draw.text((x, y), date, font=font, fill="#FFFFFF")
    y += font.getsize(date)[1]
    draw.text((x, y), IP, font=font, fill="#FF0000")
    y += font.getsize(IP)[1]
    draw.text((x, y), CPU, font=font, fill="#FFFF00")
    y += font.getsize(CPU)[1]
    draw.text((x, y), MemUsage, font=font, fill="#00FF00")
    y += font.getsize(MemUsage)[1]
    draw.text((x, y), Disk, font=font, fill="#0000FF")
    y += font.getsize(Disk)[1]
    draw.text((x, y), Temp, font=font, fill="#FF00FF")
#    y += font.getsize(extTemp)[1]
#    draw.text((x, y), extTemp, font=font, fill="#00FFFF")

    # Display image.
    disp.image(image, rotation)

def write_in_terminal(date, IP, CPU, MemUsage, Disk, Temp):
    print(date)
    print(IP)
    print(CPU)
    print(MemUsage)
    print(Disk)
    print(Temp)

def get_data_and_paint(computer):
    date = datetime.now().strftime("%c")
    IP = computer.hostname()
    CPU = computer.cpuload()
    MemUsage = computer.memory()
    Disk = computer.disk()
    Temp = computer.temperatura()
 #   extTemp = "Ext Temp: " + get_temp()

    write_in_screen(date, IP, CPU, MemUsage, Disk, Temp)
#   write_in_terminal(date, IP, CPU, MemUsage, Disk, Temp)

    time.sleep(SLEEP_TIME)

def get_computer():
    return current_computer(buttonPrev, buttonNext)

def main():
    while True:
        try:
            flag = open("/home/javi/tmp/FLAG", "r")
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            disp.image(image, rotation)
            time.sleep(30)
        except Exception:
            computer = get_computer()
            get_data_and_paint(computer)


if __name__ == '__main__':
    main()
