
import time
import pickle

import numpy

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from picamera import PiCamera
import picamera.array

import AIC


# Configuring and initiallizing display

# Raspberry Pi pin configuration:
RST = 24

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()


##############################################################

# Configuring and initializing camera

camera = PiCamera()

with picamera.array.PiRGBArray(camera) as output:
    camera.capture(output, 'rgb')
    print('Captured %dx%d image' % (
            output.array.shape[1], output.array.shape[0]))