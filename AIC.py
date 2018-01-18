
# Array Image Conversions
import numpy
import pickle
from PIL import Image


# Array to Image

# Convert a numpy array to it's equivalent image file
# 8 bit binary

disp_width = 128
disp_height = 64
disp_pixles = disp_width*disp_height

def array_to_image(weights_array)

	binary_list = []
	for i in weights_array:
		i_in_binary = [int(x) for x in list('{0:0b}'.format(i))]
		if len(i_in_binary)<32:
			zero_int_padding = [0 for i in range((32-len(i_in_binary)))]
			i_in_binary = zero_int_padding.extend(i_in_binary)
		binary_list.extend(i_in_binary)

	if len(binary_list) < disp_pixles:
		zero_padding = [0 for i in range((disp_pixles-len(binary_list)))]
		binary_list.extend(zero_padding)

	if len(binary_list) > disp_pixles:
		binary_list = binary_list[:disp_pixles]

	binary_np_array = numpy.array(binary_list, numpy.int32)
	binary_np_array.shape(disp_height,disp_width)

	output_image = Image.fromarray(binary_np_array)
	output_image.resize((disp_width, disp_height), Image.ANTIALIAS).convert('1')

	return output_image


# Image to Array

# def image_to_array(image_file):
# 	weights_image = Image.open(image_file)
# 	ppm_image = image.resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
# 	binary_image_array = numpy.array(ppm_image)

# 	#convert from binary array to int array
# 	binary_int_array = []
# 	final_array = numpy.array()
# 	for i in numpy.nditer(binary_image_array):
# 		binary_int_array.append(i)
# 		if len(binary_int_array) == 8:
# 			#convert 