from PIL import Image

image_path = r'ASCIIart\bluecar.jpg'
with Image.open(image_path) as img:

    width, height = img.size
    print(f"Width: {width}")
    print(f"Height: {height}")