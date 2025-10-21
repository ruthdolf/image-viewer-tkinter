from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Photo')

def fwd():
    global img_lbl, i, status
    
    img_lbl.grid_forget()
    i += 1
    if i >= len(img_list):
        i = 0
    img_lbl = Label(image=img_list[i])
    img_lbl.grid(row=0, column=0, columnspan=3)
    
    status.config(text="Image "+ str(i+1) + "  of " + str(len(img_list)))
        

def back():
    global img_lbl, i, status
    
    img_lbl.grid_forget()
    i -= 1
    if i < 0:
        i= len(img_list) -1
    img_lbl = Label(image=img_list[i])
    img_lbl.grid(row=0, column=0, columnspan=3)
    
    status.config(text="Image "+ str(i+1) + "  of " + str(len(img_list)))

#add images
i = 0
img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))
img_list = [img1, img2, img3, img4, img5]

#initial image
img_lbl = Label(image=img_list[i])
img_lbl.grid(row=0, column=0, columnspan=3) 


#initial status 
status = Label(root, text="Image "+ str(i+1) + "  of " + str(len(img_list)))
status.grid(row=1, column=0, sticky="EW", columnspan=3)



#buttons
backbtn = Button(root, text='<<', command=back)
fwdbtn = Button(root, text=">>", command=fwd)
quitbtn = Button(root, text="Quit program", command=root.quit)

backbtn.grid(row=1, column=0, sticky=W)
fwdbtn.grid(row=1, column=2, sticky=E)
quitbtn.grid(row=2, column=1)

# Configure grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()