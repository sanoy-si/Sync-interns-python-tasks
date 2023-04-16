from tkinter import *
import datetime
import time
from threading import *
import pygame


def set_alarm():
    clock.destroy()
    alarm_time=f"{hour.get()}:{minute.get()}:{second.get()}"
    while alarm_time != datetime.datetime.now().strftime("%H:%M:%S"):
        time.sleep(1)
        print("Current time: "+ datetime.datetime.now().strftime("%H:%M:%S"),"Alarm set at: " + alarm_time)
    print("Wake Up!")
def play_sound():
    pygame.init()
    m=pygame.mixer.Sound("a.mp3")
    m.play()
def endf():
    pygame.mixer.pause()
    stop_sound()
    clock2.destroy()
    exit()
def stop_sound():
    m=pygame.mixer.Sound("a.mp3")
    m.stop()


clock=Tk()
clock.title("Alarm Clock")
clock.geometry("550x250")
p=PhotoImage(file="a3.gif.gif")
img=Label(clock,image=p,height=200)
alarm_clock_txt=Label(clock,text="Alarm Clock",font=("None",20),background="white")
set_time_txt=Label(clock,text="When to wake you up?",font=("None",15) ,background="white")
set_alarm_btn=Button(text="Set alarm",command=set_alarm,width=25)
clock.configure(background="white")
alarm_clock_txt.place(x=50,y=200)
set_time_txt.place(x=290,y=60)
img.place(x=0,y=0) 
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23'
        )
hour = StringVar(clock)
hour.set("Hr")
hrs = OptionMenu(clock, hour, *hours)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')

minute = StringVar(clock)
minute.set("Min")
mins = OptionMenu(clock, minute, *minutes)
second = StringVar(clock)
second.set("Sec")
secs = OptionMenu(clock, second, *minutes)
hrs.place(x=260,y=120)
mins.place(x=350,y=120)
secs.place(x=440,y=120)
set_alarm_btn.place(x=295,y=180)
clock.mainloop()
def ring():
    while not var.get():
        play_sound()
clock2=Tk()
clock2.title("Alarm clock")
clock2.geometry("550x250")
clock2.configure(background="white")
p=PhotoImage(file="a3.gif.gif")
img=Label(clock2,image=p,height=200)
alarm_clock_txt=Label(clock2,text="Alarm Clock",font=("None",20),background="white")
wake_up_txt=Label(clock2,text="Time\n to\n wake up!",font=("None",25) ,background="white")
var=IntVar()
var.set(0)
Radio_btn=Radiobutton(clock2,text="I am awake.",variable=var, value=1,command=endf,background="white",font=("None",15))
t1=Thread(target=ring)
t1.start()
alarm_clock_txt.place(x=50,y=200)
wake_up_txt.place(x=300,y=40)
img.place(x=0,y=0) 
Radio_btn.place(x=300,y=200)
clock2.mainloop()




