
import time
import pickle

import numpy

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

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

# # Create blank image for drawing.
# # Make sure to create image with mode '1' for 1-bit color.
# width = disp.width
# height = disp.height
# image = Image.new('1', (width, height))

# # Get drawing object to draw on image.
# draw = ImageDraw.Draw(image)

# # Draw a black filled box to clear the image.
# draw.rectangle((0,0,width,height), outline=0, fill=0)

##############################################################

# Configuring and initializing camera

camera = PiCamera()

#camera.start_preview()

##############################################################

# Test: take picture, convert, make pic array, display pic
# Testing this 5 times

'''
for i in range(5):
	camera.capture('/home/pi/Desktop/test_images/test_image.jpg')
	
	image = Image.open('/home/pi/Desktop/test_images/test_image.jpg')
	ppm_image = image.resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
	
	disp.image(ppm_image)
	disp.display()

	time.sleep(3)

camera.stop_preview()

disp.clear()
disp.display()
'''

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

with open("test_matrix_b.txt", "wb") as biases:
	pickle.dump(b_matrix, biases)

with open("test_inputs.txt", "wb") as inputs:
	pickle.dump(input_list, inputs)

#load arrays
weights_array = []
with open("test_matrix_w.txt", "rb") as wm:
	weights_array = pickle.load(wm)

bias_array = []
with open("test_matrix_b.txt", "rb") as bm:
	bias_array = pickle.load(bm)

intput_vector = []
with open("test_inputs.txt", "rb") as il:
	intput_vector = pickle.load(il)

#display arrays
weights_image = AIC.array_to_image(weights_array)
biases_image = AIC.array_to_image(bias_array)
input_vector_image = AIC.array_to_image([intput_vector])

disp.image(weights_image)
disp.display()
time.sleep(3)

disp.image(biases_image)
disp.display()
time.sleep(3)

disp.image(input_vector_image)
disp.display()
time.sleep(3)

##############################################################

disp.clear()
disp.display()
