from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="powder blue")
        #======inserting the background JPG image=====#
        self.bg=ImageTk.PhotoImage(file="untitled.1.jpg")
        bg= Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        #left image on the window
        self.left = ImageTk.PhotoImage(file="untitled.png")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)
        #==========working under the register frame============#
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title = Label(frame1,text="REGISTER ENTRY",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #----------row1

        f_name = Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_fname.place(x=50,y=130,width=250)
        l_name = Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="White",fg="black").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_lname.place(x=370,y=130,width=250)
        contact = Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_contact.place(x=50,y=200,width=250)
        email = Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_email.place(x=370,y=200,width=250)
        question = Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_quest["values"]=("Select","Your Nick Name","Your Best Place","Your Favourite Game")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)


        answer = Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg= "light grey")
        self.txt_answer.place(x=370,y=270,width=250)
        password = Label(frame1,text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50,y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_password.place(x=50,y=340,width=250)
        cpassword=Label(frame1,text="Confirm password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_cpassword.place(x=370,y=340,width=250)
        # for the terms and conditions we have to insert the check box.........#
        self.var_chk=IntVar()
        self.chk=Checkbutton(frame1,text="I agree the terms and the conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12))
        self.chk.place(x=50,y=380)

        self.register_btn=Button(frame1,text="Register Now",bg="light grey",bd=10,fg="black",cursor="hand1",command=self.register_data)
        self.register_btn.place(x=50, y=420)



    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)

    def register_data(self):

        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()==""  :
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif  self.var_chk.get()==0:

            messagebox.showerror("Error","Please Agree our terms & condition",parent=self.root)
        else:


            try:

                con=pymysql.connect(host="localhost",user="root",password="sagar123",database="register")
                if con:
                    print("server info",con.get_server_info())
                cur=con.cursor()
                query="select * from register where email=%s"

                values=(self.txt_email.get())

                cur.execute(query,values)
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error", "User already Exist,Please try with another email", parent=self.root)
                else:
                    cur.execute("insert into register (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s%,%s",
                                    (self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()
                                    ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Successfully Registered", parent=self.root)
                self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


















root=Tk()
obj=Register(root)
root.mainloop()