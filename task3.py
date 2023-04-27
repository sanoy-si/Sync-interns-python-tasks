from tkinter import *
from tkinter import messagebox 
import pyshorteners

def shorten():   
   try:
      shortened=pyshorteners.Shortener().tinyurl.short(long_url.get())
   except:
      messagebox.showerror("Error","An Error occured while generating the link!\nPlease make sure you are connected to the internet and you entered a correct URL and Try again!")
      return

   chang_look()

   if short_link.get():
      short_link.delete(0,END)
   short_link.insert(END,shortened)


def chang_look():
   window.geometry("700x350")
   short_link_txt["fg"]="black"
   short_link["background"]="white"
   short_link["bd"]=1
   copy["background"]="white"
   copy["bd"]=2
   copy["text"]="Copy"


def copy():
  window.clipboard_clear()
  window.clipboard_append(short_link.get())

window=Tk()
window.geometry("700x200")
window.title("URL Shortener")

enter_url_txt=Label(window,text="Enter the link you want to shorten.")
long_url=Entry(window,background="white",width=100)
shorten_btn=Button (window,text="Shorten",command=shorten)
short_link_txt=Label(window,text="The new shortened link is:",fg="systembuttonface")
short_link=Entry(window,background="white",width=100,bd=0,bg="systembuttonface")
copy=Button(window,text="",command=copy,bd=0,bg="systembuttonface")

enter_url_txt.pack(pady=20)
long_url.pack()
shorten_btn.pack(pady=20)
short_link_txt.pack()
short_link.pack(pady=20)
copy.pack()
window.mainloop()



