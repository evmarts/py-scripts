from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

x, y = 10, 10

fname1 = raw_input("input image: ")
im = Image.open(fname1)
pointsize = 30
fillcolor = "white"
shadowcolor = "black"

text = "bordered text."

font = ImageFont.truetype("utils/Futura.ttc",60)
draw = ImageDraw.Draw(im)

draw.text((x-2, y-2), text, font=font, fill=shadowcolor)
draw.text((x+2, y-2), text, font=font, fill=shadowcolor)
draw.text((x-2, y+2), text, font=font, fill=shadowcolor)
draw.text((x+2, y+2), text, font=font, fill=shadowcolor)

# now draw the text over it
draw.text((x, y), text, font=font, fill=fillcolor)

im.show()
