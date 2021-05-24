import cv2
import tkinter as tk
from tkinter import *
import tkinter.ttk
from tkinter.ttk import Frame
from PIL import Image, ImageTk

white 		= "#ffffff"
lightBlue2 	= "#adc5ed"
font 		= "Constantia"
fontButtons     = (font, 12)
maxWidth  	= 800
maxHeight 	= 480

#haarcascade face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');
eye_glasses = cv2.CascadeClassifier('eyeglasses.xml')
#Graphics window
mainWindow = tk.Tk()
mainWindow.title('Liveness Registration')
mainWindow.configure(bg=lightBlue2)
#mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
mainWindow.geometry('850x600')
mainWindow.resizable(0,0)
mainWindow.protocol("WM_DELETE_WINDOW",True)
#mainWindow.overrideredirect(1)

# Create label
mainFrame = Frame(mainWindow)
mainFrame.place(x=20, y=20)                

#Capture video frames
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)

cap = cv2.VideoCapture(0)

def show_frame():

	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame,
                                          scaleFactor=1.3, minNeighbors=5);
	for x,y,w,h in faces:
				frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3)

	eyes = eye_glasses.detectMultiScale(frame,
                                          scaleFactor=1.3, minNeighbors=5);
	for x,y,w,h in eyes:
				frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),3)
	cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

	img   = Image.fromarray(cv2image).resize((760, 400))
	imgtk = ImageTk.PhotoImage(image = img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)
	
l = Label(mainWindow, text = "Remove SunGlasses/Spectacles (if any)",width = 40, height= 1)
l.config(font =("Constantia", 14))
l.pack()
l.place(x=200,y=430)

closeButton = Button(mainWindow, text = "QUIT", font = fontButtons, bg = white, width = 20, height= 1)
closeButton.configure(command= lambda: (cap.release(),mainWindow.destroy()))  

closeButton.place(x=300,y=530)
show_frame()  #Display
mainWindow.mainloop()  #Starts GUI
