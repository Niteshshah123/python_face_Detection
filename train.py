from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title('train')

           # giving title
        title = Label(self.root, text="Train Data Set", font=("cursive", 25, "bold"), bg="grey", fg="aqua")
        title.place(x=0, y=0, width=1300, height=40)

        #photo
         # First image 
        img = Image.open(r"C:\Users\sarra\OneDrive\Pictures\train01.jpg")
        img = img.resize((650, 220), resample=Image.BICUBIC)
        self.photoimg = ImageTk.PhotoImage(img)
        
        first01 = Label(self.root, image=self.photoimg)
        first01.place(x=0, y=40, width=650, height=220)

        img1 = Image.open(r"C:\Users\sarra\OneDrive\Pictures\train02.jpg")
        img1 = img1.resize((650, 220), resample=Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        first02 = Label(self.root, image=self.photoimg1)
        first02.place(x=650, y=40, width=650, height=220)

#button

        button4 = Button(self.root,text="Train Data",command=self.train_class, cursor="hand2",font=("cursive", 12, "bold"), bg="green", fg="white")
        button4.place(x=0, y=240, width=1300, height=50)
        
        img2 = Image.open(r"C:\Users\sarra\OneDrive\Pictures\train03.jpg")
        img2 = img2.resize((1300, 420), resample=Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        first03 = Label(self.root, image=self.photoimg2)
        first03.place(x=0, y=280, width=1300, height=420)


    def train_class(self):
        data_dir = "D:\Projects\data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # grey scale image
            imgNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imgNp)
            ids.append(id)
            cv2.imshow('Training', imgNp)
            cv2.waitKey(1)
        ids = np.array(ids)

        # ============================Training========
       
        clf = cv2.face.LBPHFaceRecognizer_create()
        

        clf.train(faces, ids)
        clf.write('Classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('Results', 'Data Training Completed')







if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()