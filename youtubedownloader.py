from tkinter import *
from tkinter import filedialog


# UI (Tampilan e)
screen = Tk()
title = screen.title("Yutubb Downloaderr")
canvas = Canvas(screen, width=1920, height=1080, background='black')
canvas.pack()

# Image/Logo
#logo_img = PhotoImage(file='yt.png')
label_font = Label(screen, text='YUTUB DOWNLOADER', font= 48)
#canvas.create_image(250, 80, image=logo_img)

# Link Field
link = Entry(screen, width=50)
label = Label(screen, text='Paste Download Link Kesini Oiii: ', font= 15)

# Widget ---> Window
canvas.create_window(700, 240, window=link)
canvas.create_window(700, 200, window=label)
canvas.create_window(700, 150, window=label_font)


screen.mainloop()