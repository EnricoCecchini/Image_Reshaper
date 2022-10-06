''' Description: Python script to resize images into square shape without cropping
    Disclaimer: Code from https://note.nkmk.me/en/python-pillow-add-margin-expand-canvas/
    was used to add padding to image
'''
from PIL import Image
import os

imageDir = input('Path: ')
#maxSize = (512, 512)

# Add padding to image
def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

try:
    os.mkdir(f'{imageDir}\output')
except:
    print('Output dir already exists')

# Resize images in directory
for filename in os.listdir(f'{imageDir}\source'):
    if '.png' in filename or '.jpg' in filename or '.jpeg' in filename:
        imagePath = f'{imageDir}\source\{filename}'
        print(imagePath)
        img = Image.open(imagePath)
        img = img.convert("RGBA")
        im_new = expand2square(img, (255, 255, 255, 0))
        im_new.save(f'{imageDir}\output\{filename}', 'PNG')
