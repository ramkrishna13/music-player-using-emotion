from tkinter import *
from tkinter import font
import os
from PIL import ImageTk, Image

win = Tk()
win.title("Emotify: Emotion Based Player")
win.configure(background="#a1dbcd")
img = ImageTk.PhotoImage(Image.open("music.png"))


def dataset(event):
    os.system('python real_time_video.py')
    b1.config(state=DISABLED)





def close_window():
    win.destroy()


f = Frame(win, width=500, height=500)
win.geometry('{}x{}'.format(400, 450))

fnt1 = font.Font(family='Times New Roman', size=15, weight='bold')
Label(f, text="Emotify: Emotion Based Music Player", font=fnt1).grid(row=1, column=2)
Label(f, image=img).grid(row=2, column=2)

fnt2 = font.Font(family='Helvectica', size=10, weight='bold')
b1 = Button(f, text="Start MusicPlayer", fg="#31dbcd", bg="#313a39", font=fnt2)
b1.grid(row=3, column=2, padx=10, pady=10, sticky='EWNS')
b1.bind("<Button 1>", dataset)



b4 = Button(f, text="Exit", fg="#31dbcd", bg="#383a39", command=close_window, font=fnt2)
b4.grid(row=10, column=2, padx=10, pady=10, sticky='EWNS')

f.pack()
win.mainloop()


