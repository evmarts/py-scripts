from PIL import Image, ImageChops

img = Image.open('img.jpg')

def tint_image(image, tint_color):
	return ImageChops.multiply(image, Image.new('RGB', image.size, tint_color))

tint_image(img, '#F1FEEC').show()