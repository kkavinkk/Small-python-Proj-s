from PIL import Image
import numpy as np

image_path = r'C:\Users\kavin\Downloads\code\Small-python-Proj-s\ASCIIart\bluecar.jpg'
with Image.open(image_path) as img:

    width, height = img.size
    print(f"Width: {width}")
    print(f"Height: {height}")

pixels = img.getdata(height, width)
print(pixels)

#for x in len(pixel_matrix):
#    for y in len(pixel_matrix[x]):
#        pixel = pixel_matrix[x][y]