import PIL

from PIL import Image


image = PIL.Image.open("C:/Users/manis/Downloads/atuh-beach-sunrise-nusa-penida-bali-indonesia.jpg")

width, height = image.size

print(width, "X", height)
