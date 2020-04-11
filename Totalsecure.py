from tkinter import *
from tkinter import messagebox as mb
from Tsm import *
from random import *
import os
import stat
import time

mygui=Tk()
def update(temp1,temp2,temp3,temp4,profile):
   with open(r"C:/secure/secure.txt",'r') as file:
	   data=file.readlines()
   file.close()
   if data[3]!="otp="+temp3+"\n":
       mb.showinfo(title="profile",message="Wrong OTP")
   else:
       data[0]="username="+temp1+"\n"
       data[1]="password="+temp4+"\n"
       data[2]="email="+temp2+"\n"
       message=data[0]+data[1]
       send_mail(temp2,message)
       mb.showinfo(title="profile",message="Account created")
   with open(r"C:/secure/secure.txt",'w') as file:
	   file.writelines(data)
   file.close()
   profile.destroy()
   
   
	  
def check(temp1,temp2,temp3,config):
   with open(r"C:/secure/secure.txt",'r') as file:
	   data=file.readlines()
   file.close()
   if data[0]=="username="+temp1+"\n" and data[1]=="password="+temp3+"\n":
	   data[1]="password="+temp2+"\n"
	   mb.showinfo(title="config password",message="Updated successfully")
   else:
	   mb.showinfo(title="config password",message="Old Password mismatch")
   with open(r"C:/secure/secure.txt",'w') as file:
	   file.writelines(data)
   file.close()
   config.destroy()
def otp(mail_id):
   with open(r"C:/secure/secure.txt",'r') as file:
	   data=file.readlines()
   file.close()
   number=randint(1000,9999)
   data[3]="otp="+str(number)+"\n"
   with open(r"C:/secure/secure.txt",'w') as file:
	   file.writelines(data)
   file.close()
   message="Hey, Thanks for Choosing TotalSecure"+"\n"+"otp:"+str(number)
   send_mail(mail_id,message)

def profile():
   profile=Toplevel(mygui)
   profile.title("Profile")
   profile.geometry("400x300+470+200")
   label1=Label(profile,text="USERNAME")
   label1.grid(row=2,column=1,pady=3)
   text1=Entry(profile,textvariable=d,width=25)
   text1.grid(row=2,column=5,pady=3)
   label2=Label(profile,text="Email")
   label2.grid(row=3,column=1,pady=3)
   text2=Entry(profile,textvariable=e,width=25)
   text2.grid(row=3,column=5,pady=3)
   b2=Button(profile,text="Send otp",command=lambda:otp(e.get()))
   b2.grid(row=4,column=5)
   label2=Label(profile,text="OTP sent to your mail")
   label2.grid(row=5,column=1,pady=3)
   text2=Entry(profile,textvariable=f,width=25)
   text2.grid(row=5,column=5,pady=3)
   label3=Label(profile,text="Password")
   label3.grid(row=6,column=1,pady=3)
   text3=Entry(profile,textvariable=g,width=25)
   text3.grid(row=6,column=5,pady=3)
   b1 = Button(profile, text ="Update details",command=lambda:update(d.get(),e.get(),f.get(),g.get(),profile))
   b1.grid(row = 7, column = 1,pady=4,columnspan=2,padx=1) 
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()

def config():
	   config=Toplevel(mygui)
	   config.title("Configuration")
	   config.geometry("400x300+470+200")
	   label1=Label(config,text="USERNAME")
	   label1.grid(row=2,column=1,pady=3)
	   text1=Entry(config,textvariable=a,width=25)
	   text1.grid(row=2,column=5,pady=3)
	   label2=Label(config,text="NEW PASSWORD")
	   label2.grid(row=3,column=1,pady=3)
	   text2=Entry(config,textvariable=b,width=25)
	   text2.grid(row=3,column=5,pady=3)
	   label3=Label(config,text="OLD PASSWORD")
	   label3.grid(row=4,column=1,pady=3)
	   text3=Entry(config,textvariable=c,width=25)
	   text3.grid(row=4,column=5,pady=3)
	   img = PhotoImage(file = r"C:\secure\admin.png")
	   img1 = img.subsample(2, 2)
	   Label(config, image = img1).grid(row = 1, column = 12,columnspan = 4, rowspan = 4, padx = 5, pady = 5) 
	   b1 = Button(config, text = "CHANGE PASSCODE",command=lambda:check(a.get(),b.get(),c.get(),config)) 
	   b2 = Button(config, text = "REQUEST PASSCODE")
	   b1.grid(row = 6, column = 1,pady=4,columnspan=2,padx=1) 
	   b2.grid(row = 7, column = 1, pady=4,columnspan=2,padx=1)
	   mess_box=Text(config,height=2,width=45).grid(rowspan=4,columnspan=18,pady=45)
	   config.mainloop()
	   
def init():
    try:
        if not os.path.exists('my_folder'):
            os.makedirs('C:\\Stupid')
    except:
        print("")
def unlock(temp):
    with open(r"C:/secure/secure.txt",'r') as file:
            data=file.readlines()
    file.close()
    if data[1]=="password="+temp+"\n":
        os.system( "attrib -h -s C:\\stupid")
        mb.showinfo(title="TotalSecure", message="Folder unlocked")
    else:
        mail_id=data[2].split("=")[1]
        localtime = time.asctime( time.localtime(time.time()) )
        message="Someone tried to access TotalSecure Secretly "
        mb.showinfo(title="TotalSecure",message="Wrong password")
        send_mail(mail_id,message)
a=StringVar()
b=StringVar()
c=StringVar()
sc=StringVar()
def runcheck():
   if os.stat("C:\\stupid").st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN:
        label1=Label(mygui,text="Enter password").pack()
        text1=Entry(mygui,textvariable=sc,width=30).pack()
        b1=Button(mygui,text="UNLOCK",command=lambda:unlock(sc.get())).pack()
   else:
        os.system( "attrib +h +s C:\\stupid")
        mb.showinfo(title="TotalSecure", message="Folder Locked")
mygui.title("TotalSecure")
mygui.geometry("400x300+470+200")
mymenu=Menu(mygui)
mymenu.add_cascade(label="Profile",command=profile)
mymenu.add_cascade(label="Config",command=config)
mymenu.add_cascade(label="About")
mygui.config(menu=mymenu)
init()
b2=Button(mygui,text="RUN CHECK",command=runcheck()).pack()
mygui.mainloop()

    

