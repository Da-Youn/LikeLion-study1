from PIL import Image, ImageFilter

img = Image.open("C:/Users/User/Desktop/코딩/멋사/Week6/pillow/image.png")

img_resize = img.resize((256, 256))
img_resize.save('C:/Users/User/Desktop/코딩/멋사/Week6/pillow/resize_image.png')

img_rotate = img.rotate(45)
img_rotate.save('C:/Users/User/Desktop/코딩/멋사/Week6/pillow/rotate_image.png')

img_blur = img.filter(ImageFilter.BLUR)
img_blur.save('C:/Users/User/Desktop/코딩/멋사/Week6/pillow/blur_image.png')

new_img = new_image = Image.new(
    'RGB', (2*img.size[0], 2*img.size[1]), (102, 103, 171))
new_image.paste(img, (0, 0))
new_image.paste(img_resize, (img.size[0], 0))
new_image.paste(img_rotate, (0, img.size[0]))
new_image.paste(img_blur, (img.size[0], img.size[0]))
new_image.show()
