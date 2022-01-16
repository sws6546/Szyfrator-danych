import tkinter
from tkinter import filedialog as fd
root = tkinter.Tk()

def diry():
    filename = fd.askopenfilename()
    print(filename)

szyfrowanie = tkinter.Button(root, text="Szyfrowanie", command=diry)
szyfrowanie.pack()

root.mainloop()