import random
import smtplib
from tkinter import *
from tkinter import messagebox

def enter_email(window):
    window.destroy()
    email_window=Tk()
    email_window.geometry("400x150")
    email_window.title("Enter your email")
    entered_email_txt=Label(email_window,text="Enter your email to verify")
    entered_email=Entry(email_window,width=40,bg='white')
    send_code_btn=Button(text="Send code",background="white",command=lambda:send_code(entered_email.get(),email_window))
    entered_email_txt.place(x=130,y=25) 
    entered_email.place(x=80,y=55)
    send_code_btn.place(x=160,y=85)
    email_window.mainloop()

def send_code(reciever_email,window):
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
    msg = "Your OTP verification code is " + otp
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    email = "jhonassintayehu@gmail.com"
    password = "pphcgwqowpbcgilk"
    try:
        server.login(email,password)
    except:
        Error_txt='''Unable to login to the server. check the user_email or it's password given in the code.'''
        messagebox.showerror("Error",Error_txt)
        exit()
    try:
        server.sendmail(email, reciever_email, msg)
    except:
        Error_txt = '''Unable to send the verification code to the specified email address.
Make sure you are connected to the internet and the email address is correct.'''
        messagebox.showerror("Error", Error_txt)
        enter_email(window)
    server.quit()
    verify(otp, reciever_email, window)
def check(cotp,entered_otp,email,window):
    if cotp==entered_otp:verified(window)
    else:try_again(email,cotp,window)

def verify(cotp,email,window):
    window.destroy()
    otp_window=Tk()
    otp_window.geometry("550x200")
    otp_window.title("Enter the code")
    verify_btn=Button(otp_window,text="Verify",background="white",command=lambda: check(cotp,entered_otp.get(),email,otp_window) )
    resend_btn=Button(otp_window,text="Resend code",background="white",command=lambda:send_code(email,otp_window))
    entered_otp_txt=Label(otp_window,text='Enter the 6 digit verification code we sent to the email "'+email+'"' )
    entered_otp=Entry(otp_window,width=20,bg='white')
    change_email_btn=Button(otp_window,text="Change email",background="white",command=lambda:enter_email(otp_window),width=15)
    entered_otp_txt.place(x=60,y=25)
    entered_otp.place(x=200,y=55)
    verify_btn.place(x=240,y=85)
    resend_btn.place(x=220,y=115)
    change_email_btn.place(x=200,y=145)
    otp_window.mainloop()

def verified(window):
    window.destroy()
    verified_window=Tk()
    verified_window.geometry("300x100")
    verified_window.title("Verified")
    verified_txt=Label(verified_window,text="You have succecfully  verified your account.")
    ok_btn=Button(verified_window,text="Finish",background="white",command=verified_window.destroy)
    verified_txt.place(x=20,y=20)
    ok_btn.place(x=130,y=65)
    verified_window.mainloop()
def try_again(email,cotp,window):
  text = "Incorrect code! Please check your email and try again."
  messagebox.showerror("Try Again!",text)
  
email_window=Tk()
email_window.geometry("400x150")
email_window.title("Enter your email")
entered_email_txt=Label(email_window,text="Enter your email to verify")
entered_email=Entry(email_window,width=40,bg='white')
send_code_btn=Button(text="Send code",background="white",command=lambda:send_code(entered_email.get(),email_window))
entered_email_txt.place(x=130,y=25) 
entered_email.place(x=80,y=55)
send_code_btn.place(x=160,y=85)
email_window.mainloop()


