from tkinter import*
import pyshorteners
root=Tk()
root.title("URL Shortener using Python")
root.geometry("800x500")
root['bg']=('#f0f8ff')
def shorturl():
    user_url = url.get()
    s = pyshorteners.Shortener().tinyurl.short(user_url)
    urlEntry.insert(END,s)
Label(root, text="URL Shortener", font=("Garamond 20 bold"),fg="#04408d" ).pack(pady= 20 )
frame1 = Frame(root)
Label(frame1, text="Paste URL  ", font="Garamond 15 bold").pack(side=LEFT)
url=Entry(frame1,width=50, font=("Garamond 15 bold"), )
url.pack()
frame1.pack(pady=15)
Button(root,bg="#bcc2fb", text="Generate Link",font=("Garamond 12 bold"),command=shorturl ).pack(pady=15)
frame2 = Frame(root)
Label(frame2,text="Copy URL  ",font=("Garamond 15 bold")).pack(side=LEFT)
urlEntry = Entry(frame2,width=50,fg="blue",font=("Garamond 15 "))
urlEntry.pack()
frame2.pack(pady=15)
root.mainloop()

