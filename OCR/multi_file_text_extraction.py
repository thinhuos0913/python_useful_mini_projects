# Import required packages
import sys
import os
from pathlib import Path
import cv2
import pytesseract

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# cur_dir = "D:/LEARNING/PROGRAMMING/PYTHON/python_useful_mini_projects/OCR"

# print(os.listdir(os.curdir))
# Get .jpg file name
# for img in os.listdir(os.curdir):
# 	if img.endswith(".JPG") or img.endswith(".jpg"):
# 		print(Path(img).stem)

for img in os.listdir(os.curdir):
	if img.endswith(".jpg"):
		img = cv2.imread(img)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
		rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
		dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
		contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
												cv2.CHAIN_APPROX_NONE)
		im2 = img.copy()
		# file = open("extracted.txt", "w+")
		# file.write("")
		# file.close()
		for cnt in contours:
			x, y, w, h = cv2.boundingRect(cnt)
			# Drawing a rectangle on copied image
			rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
			
			# Cropping the text block for giving input to OCR
			cropped = im2[y:y + h, x:x + w]
			
			# Open the file in append mode
			file = open("extracted.txt", "a")
			
			# Apply OCR on the cropped image
			text = pytesseract.image_to_string(cropped)
			
			# Appending the text into file
			file.write(text)
			file.write("------------------------------------\n")
