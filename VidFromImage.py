from asyncio.windows_events import NULL
from operator import mod
from matplotlib import image
from moviepy.editor import AudioFileClip, ImageClip
from tkinter import *
from tkinter import filedialog
import os

imagefile = ""
audiofile = "" 
outputfile = "D:\output.mp4" 

def browseImage():
    global imagefile
    imagefile = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Image files","*.jpeg*"),("all files","*.*")))
    label_file_explorer_1.configure(text="Image File: "+imagefile)

def browseAudio():
    global audiofile
    audiofile = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Audio Files","*.mp3*"),("all files","*.*")))
    label_file_explorer_2.configure(text="Audio File: "+audiofile)
    
def printfun() :
    print(imagefile)
    print(audiofile)

def makevid():
    audio_clip = AudioFileClip(audiofile)
    image_clip = ImageClip(imagefile)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 1
    video_clip.write_videofile(outputfile)
 
   
window = Tk()

window.title('Video Maker')
window.geometry("700x300")
window.minsize(700, 300)
window.maxsize(700, 300)
window.config(background = "black")
label_file_explorer_1 = Label(window,text = "No image file chosen ",width = 100, height = 4,fg = "white", bg="black")
label_file_explorer_2 = Label(window,text = "No audio file chosen",width = 100, height = 4,fg = "white", bg="black")

button_explore_1 = Button(window,text = "Open Image File",command = browseImage)
button_explore_2 = Button(window,text = "Open Audio File",command = browseAudio)
button_make = Button(window,text = "Make Video",command = makevid)
button_exit = Button(window,text = "Exit",command = exit)

label_file_explorer_1.grid(column = 0, row = 1)
label_file_explorer_2.grid(column = 0, row = 3)

button_explore_1.grid(column = 0, row = 2)
button_explore_2.grid(column = 0, row = 4)
button_make.grid(column = 0,row = 5)
button_exit.grid(column = 0,row = 6)
window.mainloop()




