
import time
import pickle

import numpy

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from picamera import PiCamera

import AIC

##############################################################

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

# Configuring and initializing camera

camera = PiCamera()

camera.brightness = 25

#initialize LED conrol

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

##############################################################

# Now for the fun bit
# make array into pic, display

# Write list files 
w_list_1 = [i for i in range(128)]
w_list_2 = [i+1 for i in range(128)]
w_matrix = [w_list_1, w_list_2]

b_list_1 = [i%3 for i in range(128)]
b_list_2 = [i%5 for i in range(128)]
b_matrix = [b_list_1, b_list_2]

input_list = [1 for i in range(128)]

with open("test_matrix_w.txt", "wb") as weights:
	pickle.dump(w_matrix, weights)  

#load arrays
weights_array = []
with open("test_matrix_w.txt", "rb") as wm:
	weights_array = pickle.load(wm)


#display arrays
weights_image = AIC.array_to_image(weights_array)

weights_image.save("weights_pic.bmp")

disp.image(weights_image)
disp.display()
time.sleep(1)

disp.clear()
disp.display


#convert images to arrays
new_w_array = AIC.image_to_array(weights_image)
b = numpy.array(weights_array)
print numpy.array_equal(new_w_array, b)

#turn LED on, then off
GPIO.output(18, GPIO.HIGH)
time.sleep(2)
GPIO.output(18, GPIO.LOW)


##############################################################

disp.clear()
disp.display()

#camera.stoppreview()

GPIO.cleanup()

