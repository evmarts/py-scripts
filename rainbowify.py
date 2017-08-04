from PIL import Image, ImageChops

img = Image.open('in/img1.jpg')

def tint_image(image, tint_color):
	return ImageChops.multiply(image, Image.new('RGB', image.size, tint_color))

# tint_image(img, (0, 128, 128)).show()

for r in range(127, 255,32):
	for g in range(127,255,32):
		for b in range(127,255,32):
			tint_image(img, (r,g,b)).save("out/" + str(r)+"_"+str(g)+"_"+str(b) + ".jpg")
			# tint_image(img, (r,g,b)).show()


