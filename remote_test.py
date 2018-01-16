
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from picamera import PiCamera

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

camera.start_preview()

##############################################################

# The fun bits
# Test: take picture, convert, display
# Testing this 5 times

for i in range(5):
	camera.capture('/home/pi/Desktop/test_images/test_image.jpg' % i)
	
	image = Image.open('/home/pi/Desktop/test_images/test_image.jpg').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
	disp.image(image)
	disp.display()


##############################################################

camera.stop_preview()

disp.clear()
disp.display()
