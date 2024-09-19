from PIL import Image


def image_to_rgb(image_path):
    #Retreive the Image
    image = Image.open(image_path)

    #We can convert to "RGB" mode
    image = image.convert('RGB')

    #find dimensions of the image
    width, height = image.size

    # retreive all pixel data
    pixels = list(image.getdata())

    # IMPORTANT** a 2d array is a LIST OF LISTS(List x List)
    rgb_array = [] #starts with and empty list
    for y in range(height):
        row = [] #Empty list for top to bottom
        for x in range(width):
            #Calculate the dimensions of our array
            index = y * width + x
            row.append(pixels[index])
        rgb_array.append(row)
    
    return rgb_array

image_path = r'C:\Users\kavin\Downloads\code\Small-python-Proj-s\ASCIIart\bluecar.jpg'
rgb_array(image_path)

for row in rgb_array:
    print(row)
