import tkinter as tk
from tkinter import filedialog, END
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import boto3

my_w = tk.Tk()
my_w.geometry("450x400")
my_w.title("AWS Textract")
mf1 = ('san serif', 18, 'bold')
l1 = tk.Label(my_w, text="Upload an Image\n", width=30, font=mf1)
l1.pack()
b1 = tk.Button(my_w, text='Upload File and Analyse', width=30, command=lambda: upload_file())
b1.pack()


def upload_file():
    aws_mag_con = boto3.session.Session(profile_name='demo_user')
    client = aws_mag_con.client(service_name='textract', region_name='ap-south-1')
    global img
    f_types = [('Jpg Files', "*.jpg")]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename, "r")
    # resizing for fitting
    img_resize = img.resize((400, 200))
    img = ImageTk.PhotoImage(img_resize)
    imgbytes = get_image_byte(filename)
    b2 = tk.Button(my_w, image=img)
    b2.pack()
    response = client.detect_document_text(
        Document={'Bytes': imgbytes})
    out = [""]
    for item in response['Blocks']:
        if item['BlockType'] == 'WORD':
            print(item['Text'])
            out.append(item['Text'])

    my_w1 = tk.Tk()
    my_w1.geometry("450x400")
    my_w1.title("Words")
    mf2 = ('Georgia', 18, 'bold')
    l2 = tk.Label(my_w1, text="Identified Words\n", width=30, font=mf2)
    l2.pack()
    text = tk.Text(my_w1)
    for sr in out:
        text.insert(END, sr + '\n')
    text.pack()
    my_w1.mainloop()




def get_image_byte(filename):
    with open(filename, "rb") as imgfile:
        return imgfile.read()


my_w.mainloop()