from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
out = './output'

for filename in os.listdir(path):
	img = Image.open(f"{path}/{filename}")
	# print(img.size)
	# cropped_img = img.crop((300, 150, 700, 1000))
	# print(cropped_img.size)
	edit = img.filter(ImageFilter.SHARPEN)
	# edit = img.filter(ImageFilter.BLUR).convert('L').rotate(20)
	# edit = img.filter(ImageFilter.CONTOUR)
	# edit = img.filter(ImageFilter.EDGE_ENHANCE)
	# edit = img.filter(ImageFilter.EMBOSS)
	# edit = img.filter(ImageFilter.FIND_EDGES)
	edit = img.filter(ImageFilter.SMOOTH)

	factor = 1.5
	enhancer = ImageEnhance.Contrast(edit)
	edit = enhancer.enhance(factor)

	new_name = os.path.splitext(filename)[0]
	edit.save(f'{out}/{new_name}_processed.jpg')

	edit.show()
