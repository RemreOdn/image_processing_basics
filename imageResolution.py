from PIL import Image

img = "unpeppered.PNG"

image = Image.open(img)
width, height = image.size
print(width, height)
