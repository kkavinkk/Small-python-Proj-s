from PIL import Image

def image_to_rgb_array(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to RGB mode if it's not
    image = image.convert('RGB')
    
    # Get the image dimensions
    width, height = image.size
    
    # Get the pixel data
    pixels = list(image.getdata())
    
    # Create a 2D array (list of lists) to represent the image
    rgb_array_2d = []
    for y in range(height):
        row = []
        for x in range(width):
            # Calculate the index in the flat list
            index = y * width + x
            row.append(pixels[index])
        rgb_array_2d.append(row)
    
    return rgb_array_2d

# Example usage
image_path = r'C:\Users\kavin\Downloads\code\Small-python-Proj-s\ASCIIart\bluecar.jpg'  # Replace with your image path
rgb_array_2d = image_to_rgb_array(image_path)

# Print the RGB array
for row in rgb_array_2d:
    print(row)
