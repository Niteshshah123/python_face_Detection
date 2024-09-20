from tkinter import *
from tkinter import Tk
from PIL import Image,ImageTk
from students import student
import os

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title('Face Detection')

        # First image 
        img = Image.open(r"C:\Users\sarra\Downloads\face01.webp")
        img = img.resize((650, 200), resample=Image.BICUBIC)
        self.photoimg = ImageTk.PhotoImage(img)
        
        first01 = Label(self.root, image=self.photoimg)
        first01.place(x=0, y=0, width=650, height=200)

        # Second image
        img1 = Image.open(r"C:\Users\sarra\Downloads\face01.webp")
        img1 = img1.resize((650, 200), resample=Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        first02 = Label(self.root, image=self.photoimg1)
        first02.place(x=650, y=0, width=650, height=200)

        # Background image
        img3 = Image.open(r"C:\Users\sarra\Downloads\bg01.gif")
        img3 = img3.resize((1300, 700), resample=Image.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        first03 = Label(self.root, image=self.photoimg3)
        first03.place(x=0, y=200, width=1300, height=700)

        # Giving title name
        title = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("cursive", 25, "bold"), bg="white", fg="red")
        title.place(x=0, y=150, width=1300, height=40)

       # Button1
        img4 = Image.open(r"C:\Users\sarra\Downloads\collage01.jpeg")
        img4 = img4.resize((200, 200), resample=Image.BICUBIC)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        button1 = Button(self.root, image=self.photoimg4,command=self.student_details, cursor="hand2")
        button1.place(x=150, y=200, width=150, height=150)

        button1 = Button(self.root,text="Student Details",command=self.student_details, cursor="hand2",font=("cursive", 12, "bold"), bg="white", fg="red")
        button1.place(x=150, y=350, width=150, height=30)

        #button2
        img5 = Image.open(r"C:\Users\sarra\Downloads\face detection01.jpeg")
        img5 = img5.resize((200, 200), resample=Image.BICUBIC)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        button2 = Button(self.root, image=self.photoimg5, cursor="hand2")
        button2.place(x=400, y=200, width=150, height=150)

        button2 = Button(self.root,text="Face Detector", cursor="hand2",font=("cursive", 12, "bold"), bg="white", fg="red")
        button2.place(x=400, y=350, width=150, height=30)

        #button3
        img6 = Image.open(r"C:\Users\sarra\Downloads\attendance01.jpeg")
        img6 = img6.resize((200, 200), resample=Image.BICUBIC)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        button3 = Button(self.root, image=self.photoimg6, cursor="hand2")
        button3.place(x=650, y=200, width=150, height=150)

        button3 = Button(self.root,text="Attendance", cursor="hand2",font=("cursive", 12, "bold"), bg="white", fg="red")
        button3.place(x=650, y=350, width=150, height=30)
        
        #button4 
        img7 = Image.open(r"C:\Users\sarra\Downloads\help01.jpeg")
        img7 = img7.resize((200, 200), resample=Image.BICUBIC)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        button3 = Button(self.root, image=self.photoimg7, cursor="hand2")
        button3.place(x=900, y=200, width=150, height=150)

        button3 = Button(self.root,text="Help Desk", cursor="hand2",font=("cursive", 12, "bold"), bg="white", fg="red")
        button3.place(x=900, y=350, width=150, height=30)
        
        #button5
        img8 = Image.open(r"C:\Users\sarra\Downloads\tain data.jpeg")
        img8 = img8.resize((200, 200), resample=Image.BICUBIC)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        button4 = Button(self.root, image=self.photoimg8, cursor="hand2")
        button4.place(x=150, y=450, width=150, height=150)

        button4 = Button(self.root,text="Train Data", cursor="hand2",font=("cursive", 12, "bold"), bg="white", fg="red")
        button4.place(x=150, y=600, width=150, height=30)
        

        #button6
        img9 = Image.open(r"C:\Users\sarra\Downloads\photos.jpeg")
        img9 = img9.resize((200, 200), resample=Image.BICUBIC)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        button4 = Button(self.root, image=self.photoimg9, cursor="hand2",command=self.open_img)
        button4.place(x=400, y=450, width=150, height=150)

        button4 = Button(self.root,text="Photos", cursor="hand2",command=self.open_img,font=("cursive", 12, "bold"), bg="white", fg="red")
        button4.place(x=400, y=600, width=150, height=30)
        

         #button7
        img10 = Image.open(r"C:\Users\sarra\Downloads\developer.jpeg")
        img10 = img10.resize((200, 200), resample=Image.BICUBIC)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        button4 = Button(self.root, image=self.photoimg10, cursor="hand2")
        button4.place(x=650, y=450, width=150, height=150)

        button4 = Button(self.root,text="Developer", cursor="hand2",font=("cursive", 12, "bold"), bg="white", fg="red")
        button4.place(x=650, y=600, width=150, height=30)


         #button8
        img11 = Image.open(r"C:\Users\sarra\Downloads\exit.jpeg")
        img11 = img11.resize((200, 200), resample=Image.BICUBIC)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        button4 = Button(self.root, image=self.photoimg11, cursor="hand2")
        button4.place(x=900, y=450, width=150, height=150)

        button4 = Button(self.root,text="Exit", cursor="hand2",font=("cursive", 12, "bold"), bg="white", fg="red")
        button4.place(x=900, y=600, width=150, height=30)


    def open_img(self):
        os.startfile("D:\Projects\data")






        #============function===============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
