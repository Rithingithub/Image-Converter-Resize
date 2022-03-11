from PIL import Image

imgsrc = input("Provide the file name of the image: ")
im = Image.open(imgsrc)

im = Image.open(imgsrc)
# converting to png
rgb_im = im.convert("RGB")
# exporting the image
rgb_im.save("Colloseum.png")
im.show()


# Size of the original image in pixels
width, height = im.size

# Setting the points for cropped image
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5

# output gives cropped image
im1 = im.crop((left, top, right, bottom))
new_size = (300, 300)
im1 = im1.resize(new_size)

# show the output
im1.show()
