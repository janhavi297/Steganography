from PIL import Image
im = Image.open("image1.jpg")
im.show()

print(im.format, im.size[1], im.mode)
