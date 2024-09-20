from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2






class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title('student')


        #======data entry variables========
        self.dep =StringVar()
        self.name =StringVar()
        self.id =StringVar()
        self.roll_no =StringVar()
        self.email =StringVar()
        self.phone_no =StringVar()
        self.gender =StringVar()
        self.photo =StringVar()
        self.address =StringVar()
        self.year =StringVar()
        self.semester =StringVar()
        self.course =StringVar()
        self.dob =StringVar()
        self.radio_button1 =StringVar()


        
        # First image 
        img = Image.open(r"C:\Users\sarra\Downloads\student01.jpeg")
        img = img.resize((650, 200), resample=Image.BICUBIC)
        self.photoimg = ImageTk.PhotoImage(img)
        
        first01 = Label(self.root, image=self.photoimg)
        first01.place(x=0, y=0, width=650, height=200)

        # Second image
        img1 = Image.open(r"C:\Users\sarra\Downloads\student02.jpeg")
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
        title = Label(self.root, text="Students Management System", font=("cursive", 25, "bold"), bg="white", fg="green")
        title.place(x=0, y=150, width=1300, height=40)

        #making frame
        frame=Frame(first03,bd=2)
        frame.place(x=5,y=-10,width=1250,height=600)

        #students details
        left=LabelFrame(frame,bd=2 ,bg="white",relief=RIDGE,text="Students Details",font=("cursive",12,"bold"),fg='red')
        left.place(x=10,y=10,width=700,height=500 )

        

        #course information
        course=LabelFrame(frame,bd=2 ,bg="white",relief=RIDGE,text="Course Information",font=("cursive",12,"bold"),fg='blue')
        course.place(x=10,y=35,width=700,height=150 )

        #department
        dep=Label(course,bg="white",text="Department",font=("cursive",12,"bold"),width=10)
        dep.grid(row=0,column=0,pady=10,sticky=W)

        #combobox
        combo=ttk.Combobox(course,textvariable=self.dep,font=("cursive",12,"bold"),state="readonly")
        combo["values"]=('Select Department','Computer','Civil','Humanity','Management','Medical','Sanskrit')
        combo.current(0)
        combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)


        #course01
        dep=Label(course,bg="white",text="Course",font=("cursive",12,"bold"),width=10)
        dep.grid(row=0,column=2,pady=10,sticky=W)

        #combobox
        combo=ttk.Combobox(course,textvariable=self.course,font=("cursive",12,"bold"),state="readonly",width=15)
        combo["values"]=('Select Course','CSE','ME','CYS','ARE','CCE','ECE')
        combo.current(0)
        combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #year
        dep=Label(course,bg="white",text="Year",font=("cursive",12,"bold"),width=10)
        dep.grid(row=2,column=0,pady=10,sticky=W)

        #combobox
        combo=ttk.Combobox(course,textvariable=self.year,font=("cursive",12,"bold"),state="readonly")
        combo["values"]=('Select Year','20-21','21-22','22-23','23-24')
        combo.current(0)
        combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)

        #semester
        dep=Label(course,bg="white",text="Semester",font=("cursive",12,"bold"),width=10)
        dep.grid(row=2,column=2,pady=10,sticky=W)

        #combobox
        combo=ttk.Combobox(course,textvariable=self.semester,font=("cursive",12,"bold"),state="readonly",width=15)
        combo["values"]=('Select Semester','sem-1','sem-2','sem-3','sem-4','sem-5','sem-6','sem-7','sem-8')
        combo.current(0)
        combo.grid(row=2,column=3,padx=5,pady=10,sticky=W)

        #class students information 
       
        class01=LabelFrame(frame,bd=2 ,bg="white",relief=RIDGE,text="Class Students Information",font=("cursive",12,"bold"),fg='green')
        class01.place(x=10,y=145,width=700,height=450)


        # ID entry
        dep = Label(class01, bg="white", text="Student ID:", font=("cursive", 12, "bold"))
        dep.grid(row=0, column=0, pady=10, padx=10, sticky=W)
        ID = ttk.Entry(class01,textvariable=self.id, width=20, font=("cursive", 12, "bold"))
        ID.grid(row=0, column=1, pady=5, padx=10, sticky=W)

        # NAME entry
        dep = Label(class01, bg="white", text="Name:", font=("cursive", 12, "bold"))
        dep.grid(row=0, column=2, pady=10, padx=10, sticky=W)
        name = ttk.Entry(class01,textvariable=self.name, width=20, font=("cursive", 12, "bold"))
        name.grid(row=0, column=3, pady=5, padx=10, sticky=W)

        # ROLL
        dep = Label(class01, bg="white", text="ROLL NO:", font=("cursive", 12, "bold"))
        dep.grid(row=1, column=0, pady=10, padx=10, sticky=W)
        roll = ttk.Entry(class01,textvariable=self.roll_no, width=20, font=("cursive", 12, "bold"))
        roll.grid(row=1, column=1, pady=5, padx=10, sticky=W)

        # DOB
        dep = Label(class01, bg="white", text="D.O.B:", font=("cursive", 12, "bold"))
        dep.grid(row=1, column=2, pady=10, padx=10, sticky=W)
        dob = ttk.Entry(class01,textvariable=self.dob, width=20, font=("cursive", 12, "bold"))
        dob.grid(row=1, column=3, pady=5, padx=10, sticky=W) 

        #phone
        dep = Label(class01, bg="white", text="Phone NO:", font=("cursive", 12, "bold"))
        dep.grid(row=2, column=0, pady=10, padx=10, sticky=W)
        phone = ttk.Entry(class01,textvariable=self.phone_no, width=20, font=("cursive", 12, "bold"))
        phone.grid(row=2, column=1, pady=5, padx=10, sticky=W)

        # EMAIL
        dep = Label(class01, bg="white", text="Email:", font=("cursive", 12, "bold"))
        dep.grid(row=2, column=2, pady=10, padx=10, sticky=W)
        email = ttk.Entry(class01,textvariable=self.email, width=20, font=("cursive", 12, "bold"))
        email.grid(row=2, column=3, pady=5, padx=10, sticky=W)

        # gender
        dep = Label(class01, bg="white", text="Gender:", font=("cursive", 12, "bold"))
        dep.grid(row=3, column=0, pady=10, padx=10, sticky=W)
        #gender = ttk.Entry(class01,textvariable=self.gender, width=20, font=("cursive", 12, "bold"))
        #gender.grid(row=3, column=1, pady=5, padx=10, sticky=W)
        combo=ttk.Combobox(class01,textvariable=self.gender,font=("cursive",12,"bold"),state="readonly")
        combo["values"]=('Male','Female','Other')
        combo.current(0)
        combo.grid(row=3,column=1,padx=5,pady=10,sticky=W)

        # address
        dep = Label(class01, bg="white", text="Address:", font=("cursive", 12, "bold"))
        dep.grid(row=3, column=2, pady=10, padx=10, sticky=W)
        address = ttk.Entry(class01,textvariable=self.address, width=20, font=("cursive", 12, "bold"))
        address.grid(row=3, column=3, pady=5, padx=10, sticky=W)  

        #radio buttons
        self.radio_button1=StringVar()     
        button1=ttk.Radiobutton(class01,variable=self.radio_button1,text='Take Photo Sample',value='Yes')    
        button1.grid(row=4,column=0)    
    
        button2=ttk.Radiobutton(class01,variable=self.radio_button1,text='No Photo Sample',value='No')    
        button2.grid(row=4,column=1)   

        #button frame
        btn=Frame(class01,bd=2,relief=RIDGE,bg='white')      
        btn.place(x=0,y=210,width=680,height=100)   

        #save button
        save=Button(btn,text='Save',command=self.add_data,width=15,font=('Cursive',13,'bold'),bg='green',fg='white')  
        save.grid(row=0,column=0)  

        #update button
        update=Button(btn,text='Update',command=self.update_data,width=15,font=('Cursive',13,'bold'),bg='lightblue',fg='white')  
        update.grid(row=0,column=1,padx=7,pady=0) 

        #reset button
        reset=Button(btn,text='Reset',command=self.reset_data,width=15,font=('Cursive',13,'bold'),bg='blue',fg='white')  
        reset.grid(row=0,column=2,padx=7,pady=0)
        
        #delete button
        delete=Button(btn,text='Delete',command=self.delete_data,width=15,font=('Cursive',13,'bold'),bg='red',fg='white')  
        delete.grid(row=0,column=3,padx=7,pady=0) 

        #take  photo button
        photo1=Button(btn,command=self.generate_data,text='Take Photo',width=15,font=('Cursive',13,'bold'),bg='orange',fg='white')  
        photo1.grid(row=1,column=0,padx=7,pady=5) 

        #update photo button
        photo2=Button(btn,text='Update Photo',width=15,font=('Cursive',13,'bold'),bg='pink',fg='white')  
        photo2.grid(row=1,column=1,padx=10,pady=5) 


        #rightside
        right=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("cursive",12,"bold"))
        right.place(x=700,y=10,width=550,height=500 )

        search=LabelFrame(right,bd=2 ,bg="white",relief=RIDGE,text="Search System",font=("cursive",12,"bold"),fg='blue')
        search.place(x=0,y=0,width=520,height=150)

        #search label

        searchlab = Label(search, bg="orange", text="Search By:", font=("cursive", 12, "bold"), fg='white')
        searchlab.grid(row=0, column=0, pady=10, padx=10, sticky=W)

        #combo box
        search1 = ttk.Combobox(search, font=("cursive", 13, "bold"), state="readonly", width=18)
        search1["values"] = ('Select ', 'Roll_no:', 'Semester', 'Phone1_no', 'Department')
        search1.current(0)
        search1.grid(row=1, column=0, padx=2, pady=10, sticky=W)


        search_entry = ttk.Entry(search, width=30, font=("cursive", 12, "bold"))
        search_entry.grid(row=1, column=1, pady=5, padx=10, sticky=W)

        # button
        searchbtn=Button(search,text='Search',width=15,font=('Cursive',13,'bold'),bg='blue',fg='white')  
        searchbtn.grid(row=2,column=0,padx=7,pady=0)
        
        #delete button
        showAll=Button(search,text='Show All',width=15,font=('Cursive',13,'bold'),bg='red',fg='white')  
        showAll.grid(row=2,column=1,padx=7,pady=0) 


        #table
        Table=LabelFrame(right,bd=2 ,bg="white",relief=RIDGE)
        Table.place(x=0,y=150,width=520,height=300)

        scrollx=ttk.Scrollbar(Table,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(Table,orient=VERTICAL)

        self.student_table2 = ttk.Treeview(
    Table,
    columns=('dep', 'photo', 'id', 'name', 'email', 'roll_no', 'gender', 'dob', 'address', 'phone_no', 'year', 'semester', 'course', 'radio_button1'),
    xscrollcommand=scrollx.set,
    yscrollcommand=scrolly.set
)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.student_table2.xview)
        scrolly.config(command=self.student_table2.yview)

        self.student_table2.heading('dep', text='Department')
        self.student_table2.heading('photo', text='Photo_Status')
        self.student_table2.heading('id', text='Student ID')
        self.student_table2.heading('name', text='Name')
        self.student_table2.heading('email', text='Email')
        self.student_table2.heading('roll_no', text='Roll No')
        self.student_table2.heading('gender', text='Gender')
        self.student_table2.heading('dob', text='D.O.B')
        self.student_table2.heading('address', text='Address')
        self.student_table2.heading('phone_no', text='Phone No')
        self.student_table2.heading('year', text='Year')
        self.student_table2.heading('semester', text='Semester')
        self.student_table2.heading('course', text='Course')
        self.student_table2.heading('radio_button1', text='Radio Button 1')



        self.student_table2['show']='headings'

        self.student_table2.column('dep', width=100)
        self.student_table2.column('name', width=100)
        self.student_table2.column('id', width=100)
        self.student_table2.column('roll_no', width=100)
        self.student_table2.column('email', width=100)
        self.student_table2.column('phone_no', width=100)
        self.student_table2.column('gender', width=100)
        self.student_table2.column('photo', width=100)
        self.student_table2.column('address', width=100)
        self.student_table2.column('year', width=100)
        self.student_table2.column('semester', width=100)
        self.student_table2.column('course', width=100)
       # self.student_table2.column('dob', width=100)
        self.student_table2.column('radio_button1', width=100)
        self.student_table2.pack(fill=BOTH,expand=1)
        self.student_table2.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()

    
# Inside the add_data method
    # Inside the add_data method
   # Inside the add_data method
    def add_data(self):
        if (
            self.dep.get() == 'Select Department' or
            self.name.get() == '' or
            self.id.get() == '' or
            self.year.get() == 'Select Year'
        ):
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='ranjit', database='user')
                print("Connected to MySQL Server:")
                print("Host:", conn.server_host)
                print("User:", conn.user)
                print("Database:", conn.database)

                my_cursor = conn.cursor()

                # Check the order of variables in the VALUES clause
                my_cursor.execute('INSERT INTO student_table2 (dep,photo, id, name, email, roll_no, gender, dob, address, phone_no, year, semester, course,radio_button1) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                    self.dep.get(),
                    self.photo.get(),
                    self.id.get(),
                    self.name.get(),
                    self.email.get(),
                    self.roll_no.get(),
                    self.gender.get(),
                    self.dob.get(),
                    self.address.get(),
                    self.phone_no.get(),
                    self.year.get(),
                    self.semester.get(),
                    self.course.get(),
                    self.radio_button1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Students Details have been added successfully', parent=self.root)

            except Exception as es:
                messagebox.showerror('Error', f'Due tooo {str(es)}', parent=self.root)


   #=================fetch data==========
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='ranjit', database='user')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student_table2")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table2.delete(*self.student_table2.get_children())
            for i in data:
                self.student_table2.insert("", END, values=i)
            conn.commit()
        conn.close()
        
        #=========focus cursor=======
    
    def get_cursor(self, event=""):
        cursor_focus = self.student_table2.focus()
        content = self.student_table2.item(cursor_focus)
        data = content['values']

        self.dep.set(data[0])
        self.photo.set(data[1])
        self.id.set(data[2])
        self.name.set(data[3])
        self.email.set(data[4])
        self.roll_no.set(data[5])
        self.gender.set(data[6])
        self.dob.set(data[7])
        self.address.set(data[8])
        self.phone_no.set(data[9])
        self.year.set(data[10])
        self.semester.set(data[11])
        self.course.set(data[12])
        self.radio_button1.set(data[13])

    #update button
    def update_data(self):
        if (
            self.dep.get() == 'Select Department' or
            self.name.get() == '' or
            self.id.get() == '' or
            self.year.get() == 'Select Year'
        ):
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        else:
            try:
                Update = messagebox.askyesno('Update', 'Do you want to Update the students details', parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='ranjit', database='user')
                    my_cursor = conn.cursor()
                    my_cursor.execute('UPDATE student_table2 SET dep=%s, name=%s, roll_no=%s, email=%s, dob=%s, gender=%s,photo=%s, address=%s, year=%s, semester=%s, course=%s, phone_no=%s, radio_button1=%s WHERE id=%s', (
                        self.dep.get(),
                        
                        self.name.get(),
                        self.roll_no.get(),
                        self.email.get(),
                        self.dob.get(),
                        self.gender.get(),
                        self.photo.get(), 
                        self.address.get(),
                       
                        self.year.get(),
                        self.semester.get(),
                        self.course.get(),
                        self.phone_no.get(),
                        self.radio_button1.get(),
                        self.id.get()
                    ))
                    messagebox.showinfo('Successfully', 'Students details Updated Successfully', parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}', parent=self.root)

    #delete button
    # Inside the delete_data method
    def delete_data(self):
        if self.id.get() == '':
            messagebox.showerror('Error', 'Student id required', parent=self.root)
        else:
            try:
                delete = messagebox.askyesno('Student Delete page', 'Do you want to Delete this Student', parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='ranjit', database='user')
                    print(conn)
                    my_cursor = conn.cursor()

                    # Corrected SQL statement
                    sql = 'DELETE FROM student_table2 WHERE id=%s'
                    val = (self.id.get(),)
                    my_cursor.execute(sql, val)

                    conn.commit()
                    messagebox.showinfo('Delete', 'Students details deleted successfully', parent=self.root)
                    self.fetch_data()
                    conn.close()
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}', parent=self.root)


#reset
    def reset_data(self):
        self.dep.set('Select Department')
        self.photo.set('')
        self.id.set('')
        self.name.set('')
        self.email.set('')
        self.roll_no.set('')
        self.gender.set('')
        self.dob.set('')
        self.address.set('')
        self.phone_no.set('')
        self.year.set('Select Year')
        self.semester.set('Select Semester')
        self.course.set('Select Course')
        self.radio_button1.set('')

    #generate database
    def generate_data(self):
        if (
            self.dep.get() == 'Select Department' or
            self.name.get() == '' or
            self.id.get() == '' or
            self.year.get() == 'Select Year'
        ):
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='ranjit', database='user')
                my_cursor = conn.cursor()
                my_cursor.execute('SELECT * FROM student_table2')
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1

                my_cursor.execute('UPDATE student_table2 SET dep=%s, photo=%s, name=%s, email=%s, roll_no=%s, gender=%s, dob=%s, address=%s, phone_no=%s, year=%s, semester=%s, course=%s, radio_button1=%s WHERE id=%s', (
                    self.dep.get(),
                    self.photo.get(),
                    self.name.get(),
                    self.email.get(),
                    self.roll_no.get(),
                    self.gender.get(),
                    self.dob.get(),
                    self.address.get(),
                    self.phone_no.get(),
                    self.year.get(),
                    self.semester.get(),
                    self.course.get(),
                    self.radio_button1.get(),
                    id + 1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #========= face frontal from cv2=========
                face_classifier = cv2.CascadeClassifier(r"D:\Projects\haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path_name = r"D:\Projects\data" + str(id+1) + '.' + str(img_id) + '.jpg'
                        cv2.imwrite(file_path_name, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow('cropped face', face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 25:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Results', 'Generating data')

            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}', parent=self.root)
if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()