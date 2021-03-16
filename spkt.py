from tkinter  import *
import pandas as pd
from PIL import Image,ImageTk
from gtts import gTTS
import os
import  tkinter.messagebox
import mysql.connector

def main():
    R1=Tk()
    R1.geometry('800x600+100+100')
    R1.title('Speech Recognition Application')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R1,image=photo_image)
    label.place(x=0,y=0)
   
   
    
    l1=Label(R1,text="SPEECH RECOGNITION SYSTEM",font=('Candara',20,'bold'),bg='Light Blue',justify='center')
    l1.place(x=200,y=100)
    Registerbtn = Button(R1,text = "REGISTER",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=signup)
    loginbtn = Button(R1,text = "LOGIN",width=17,height=2,font=('Candara',15,'bold'),bg='Light Blue',justify='center',command=login)
    Registerbtn.place(x =300 ,y=200)
    loginbtn.place( x =300,y=300)
    R1.mainloop()
    
def signup():
    def Signups():
        Name=name.get()
        Email_id=emailid.get()
        Phone_no=phno.get()
        Password=pswd.get()

    
        aa= mysql.connector.connect(host='localhost',port= 3300,user="root",passwd="123",db="Speech_Recognition")
        mm = aa.cursor()
        mm.execute("""INSERT INTO SpeechAPI VALUES (%s,%s,%s,%s)""",(Name,Email_id,Phone_no,Password))

        aa.commit()

        if name.get() == '' or pswd.get() == '':
             tkinter.messagebox.showinfo("Sorry","Please fill the required information correctly")
        else:
            tkinter.messagebox.showinfo("Welcome %s" %Name, "Lets Login")
            login()
            
    global R2
    R2=Toplevel()
    R2.geometry('800x600+100+100')
    R2.title('REGISTER NOW')

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R2,image=photo_image)
    label.place(x=0,y=0)
   



    lblInfo=Label(R2,text="Name",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=140)

    lblInfo=Label(R2,text="Email_id",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=190)
    
    lblInfo=Label(R2,text="Phone_no",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=240)

    lblInfo=Label(R2,text="Password",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=200,y=290)
    
    name=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    name.place(x=300,y= 140 )
    
    emailid=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    emailid.place(x=300,y=190 )
    
    phno=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    phno.place(x=300,y= 240 )
    
    pswd=Entry(R2,show='*',width=20,font=("bold",15),highlightthickness=2)
    pswd.place(x=300,y= 290 )

    submitbtn= Button(R2,text = "Submit",width=10,height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=Signups)

    submitbtn.place(x =350,y=340)
      
    R2.mainloop()

def login():
    def logininto():
        aa = mysql.connector.connect(host='localhost', port=3300, user="root", passwd="123", db="Speech_Recognition")
        mm = aa.cursor()
        Name = e1.get()
        Password = e2.get()
        if e1.get() == "" or e2.get() == "":
            tkinter.messagebox.showinfo("Sorry", "Please complete the required field correctly")
        else:
            mm.execute('SELECT * FROM SpeechAPI WHERE Name = %s AND Password = %s',(Name,Password))
            for i in Name:
                print( 0 )
            if mm.fetchall():
                tkinter.messagebox.showinfo("Welcome %s" % Name, "Logged in successfully")
                fun1()
            else:
                tkinter.messagebox .showinfo("Sorry", "Wrong password")
  
    global R3
    R3 = Toplevel()
    R3.geometry('800x600+100+100')
    R3.title("LOGIN NOW")

    image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R3,image=photo_image)
    label.place(x=0,y=0)
   


    lblInfo=Label(R3,text="Name",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=230,y=200)
   
    lblInfo=Label(R3,text="Password",fg="black",font=('Candara',15,'bold'))
    lblInfo.place(x=230,y=250)
    
    e1= Entry(R3,width=15,font=("bold",17),highlightthickness=2,bg="WHITE")
    e1.place(x=330, y=190)

    e2= Entry(R3,width=15,font=("bold",17),show="*",highlightthickness=2,bg="WHITE")
    e2.place(x=330, y=240)

    loginbtn = Button(R3, text="LOGIN", width=10, height=2,fg="black",font=('Candara',15,'bold'),justify='center',bg="light blue",command=logininto)
    loginbtn.place(x=380, y=400)
    
    R3.mainloop()
    
def fun1():
    
    global R4
    R4=Tk()
    R4.geometry('800x600')
    R4.title('Speech Recognition Application')

    '''image=Image.open('image5.jpeg')
    image=image.resize((800,600))
    photo_image=ImageTk.PhotoImage(image)
    label=Label(R4,image=photo_image)
    label.place(x=0,y=0)'''
   
    one=Label(R4,text="",bg="orange")             
    two=Label(R4,text="",bg="white")
    three=Label(R4,text="",bg="green")

    one.pack(fill=X)
    two.pack(fill=X)
    three.pack(fill=X)

    
    one1=Label(R4,text="",bg="orange")             
    two2=Label(R4,text="",bg="white")
    three3=Label(R4,text="",bg="green")

    one1.pack(fill=X,side=BOTTOM)
    two2.pack(fill=X,side=BOTTOM)
    three3.pack(fill=X,side=BOTTOM)

   
    TSbtn = Button(R4,text = "TEXT_TO_SPEECH",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun2)
    STbtn = Button(R4,text = "SPEECH_TO_TEXT",width=17,height=2,font=('Candara',15,'bold'),justify='center',bg='Light Blue',command=fun3)
    TSbtn.place(x =300 ,y=200)
    STbtn.place(x =300,y=300)
    R4.mainloop()

def fun2():
    import gtts,os
    from gtts import gTTS
    tts=gTTS('Hi Nishanth How Are You',lang='en',slow=True)
    tts.save('hello1.mp3')
    os.system('hello1.mp3')
    os.remove('hello1.mp3')
    
def fun3():
    import speech_recognition as sr
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio=r.listen(source)
    try:
        print("You said:"+r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results;{0}".format(e))
 
    
main()   






    
            

    
    
