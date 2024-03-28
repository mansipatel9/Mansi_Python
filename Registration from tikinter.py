from tkinter import *

root=Tk()
root.geometry("350x370")
root.title("Registration from")
root.resizable(width=False,height=False)

l_Registrationfrom=Label(root,text="REGISTRTION  FROM",font=("Arial",15))
l_Registrationfrom.place(x=80,y=20)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=140,y=50)

e_id=Entry(root)
e_id.place(x=110,y=70)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=143,y=90)

e_id=Entry(root)
e_id.place(x=110,y=110)

l_address=Label(root,text="ADDRESS")
l_address.place(x=149,y=130)

e_address=Entry(root)
e_address.place(x=110,y=150)

l_zipcode=Label(root,text="ZIP CODE")
l_zipcode.place(x=150,y=170)

e_zipcode=Entry(root)
e_zipcode.place(x=110,y=188)

sumbit=Button(root,text="SUMBIT",bg="white",fg="black",font=("calibri",12))
sumbit.place(x=140,y=210)
