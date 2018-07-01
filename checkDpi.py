from PIL import Image
im = Image.open('test.tif')
print(im.info['dpi'])
