from resizeimage import resizeimage


from tkinter.filedialog import *

img = askopenfilename()


from PIL import Image


a = int(input('Enter height : '))
b = int(input('Enter width : '))

with open(img, 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [a, b])
        im2 = cover.crop((10, 200, 154, 60))
        cover.save('resize.jpeg', image.format)


q = input('Do you want to take a pdf copy of this file (y/n) : ')

n = 0
if q in ['y', 'Y', 'yes', 'Yes']:
    img = Image.open(img)
    im1 = img.convert('RGB')
    im1.save(r'resize.pdf')
else:
    print('Terminated ')
