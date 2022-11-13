from tkinter import *
import instaloader

insta = instaloader.Instaloader()

def click():
    account = userInfo.get()
    insta.download_profile(account,profile_pic_only=True)

root = Tk()
root.title("Insta Bot Profile Donwloader")

logo = PhotoImage(file="InstaLogo.png")
image = Label(root,image = logo)
image.grid(pady=10)

title = Label(root,text = "Insta Profile Image Downloader",font=("Times New Roman",32,"bold"))
title.grid(padx=12,pady=17)

user = Label(root,text = " Username Account",font=("arial",16,"bold"))
user.grid(pady=8)

userInfo = Entry(root,font=("arial",14,"bold"),bd=3)
userInfo.grid()

button = Button(root,text = "Download Photo",font=("arial",15,"bold"),command = click)
button.grid(pady=10)

root.mainloop()