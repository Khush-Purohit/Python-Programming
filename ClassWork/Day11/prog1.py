# import PIL
from PIL import Image

with Image.open("C:\\Users\\dbda.STUDENTSDC\\Desktop\\WhatsApp Image 2025-10-09 at 4.23.41 PM.jpeg") as img:
# with Image.open("ClassWork\Day11\lenna.png") as img:
    img.load()

img.show()


# Image.merge("RGB", )