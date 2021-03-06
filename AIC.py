
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


def array_to_image(weights_array):

    binary_list = []
    for i in weights_array:
        for j in i:
            int_as_bin = [int(x) for x in list('{:0b}'.format(j))]
            if len(int_as_bin) < 32:
                temp = [0 for x in range(32 - len(int_as_bin))]
                temp.extend(int_as_bin)
                int_as_bin = temp
            binary_list.extend(int_as_bin)
        
    if len(binary_list) < disp_pixles:
        zero_padding = [0 for i in range((disp_pixles-len(binary_list)))]
        binary_list.extend(zero_padding)

    if len(binary_list) > disp_pixles:
        binary_list = binary_list[:disp_pixles]
    
    output_image = Image.new('1', (disp_width, disp_height))
    output_image.putdata(binary_list)

    return output_image


# Image to Array

def image_to_array(image_file, dim=(2, 128)):
  #weights_image = Image.open(image_file)
  ppm_image = image_file.resize((disp_width, disp_height), Image.ANTIALIAS).convert('1')
  image_array = numpy.array(ppm_image.getdata()).reshape(ppm_image.size[0], ppm_image.size[1])

  #convert from binary array to int array
  bit_str = ""
  final_array = numpy.array([], dtype=numpy.int32)
  for i in numpy.nditer(image_array):
      bit_str += str(i)
      if len(bit_str) == 32:
          final_array = numpy.append(final_array, [int(bit_str, 2)])
          bit_str = ""

  final_array.shape = dim
  return final_array
