from PIL import Image, ImageChops

img = Image.open('dnk_38.jpg')

def tint_image(image, tint_color):
	return ImageChops.multiply(image, Image.new('RGB', image.size, tint_color))

img = tint_image(img, '#F1FEEC')

img.save("out.jpg")