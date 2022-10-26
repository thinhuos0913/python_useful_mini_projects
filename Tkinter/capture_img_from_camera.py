from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from time import sleep
from threading import Thread

window = Tk()
window.title("Show camera")

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# ret,frame = video.read()

# cv2.imshow("W", frame)

canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH)//2
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)//2

canvas = Canvas(window,width=canvas_w,height=canvas_h)
canvas.pack()

img_count = 0
photo = None
grscl = 0

def cvt_grscl():
	global grscl
	grscl=1-grscl

def save_img():
	global img_count
	ret, frame = video.read()
	img_name = "opencv_frame_{}.png".format(img_count)
	cv2.imwrite(img_name, frame)
	print("{} written!".format(img_name))
	img_count += 1

button = Button(window,text = "Greyscale", command=cvt_grscl)
button.pack()

save = Button(window,text="Save image", command=save_img)
save.pack()

def update_frame():
	global canvas, photo, grscl, img_count
	# Read from camera
	ret, frame = video.read()
	# Resize frame
	frame = cv2.resize(frame,dsize=None,fx=0.5,fy=0.5)
	# Convert color from BGR to RGB
	if grscl==0:
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	else:
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Convert numpy array to color image
	photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
	# Show window
	canvas.create_image(0,0,image = photo,anchor = tkinter.NW)
	window.after(15,update_frame)

update_frame()

window.mainloop()