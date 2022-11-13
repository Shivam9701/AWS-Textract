import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

my_w = tk.Tk()
my_w.geometry("450x400")
my_w.title("AWS Textract")
mf1 = ('san serif', 18, 'bold')
l1 = tk.Label(my_w, text="Upload an Image\n", width=30, font=mf1)
l1.pack()
b1 = tk.Button(my_w, text='Upload File and Analyse', width=30, command=lambda: upload_file())
b1.pack()


def upload_file():
    global img
    f_types = [('Jpg Files', "*.jpg")]
    filename = filedialog.askopenfile(filetype=f_types)
    img = Image.open(filename)
    # resizing for fitting
    img_resize = img.resize((400, 200))
    img = ImageTk.PhotoImage(img_resize)
    b2 = tk.Button(my_w, image=img)
    b2.pack()


my_w.mainloop()

