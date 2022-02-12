from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Image viewer")
#root.iconbitmap('C:/Users/MARK/Downloads/palm.ico')

# Variables

img_num = 0

#Functions

def enter():
    global my_image
    global my_image_label
    global img_list
    global img_num
    img_num = int(e.get())
    if img_num < 1 or img_num > len(img_list):
        msg=messagebox.showerror("","You must pick valid picture number!")
        e.delete(0,END)
    else:
        my_image = ImageTk.PhotoImage(Image.open(img_list[img_num -1]).resize((400,500),Image.BOX))
        my_image_label = Label(image=my_image).grid(row = 0, column = 0, columnspan = 3)
        e.delete(0,END)
        #Widget updates
        status = Label(root,text="Image "+ str(img_num) + " of " + str(len(img_list)),relief=SUNKEN,bd = 3, anchor = E)

        #Widget layout
        status.grid(row = 4, column = 0, columnspan = 3,sticky = W+E)
   
    
    return

def backward(img_num):
     global my_image
     global img_list
     global my_image_label
     
     my_image = ImageTk.PhotoImage(Image.open(img_list[img_num -2]).resize((400,500),Image.BOX))
     my_image_label = Label(image=my_image).grid(row = 0, column = 0, columnspan = 3)
     img_num -=1

     #Widget updates
     open_button = Button(root, text="Open file", command= lambda:open(img_num),bg="red")
     status = Label(root,text="Image "+ str(img_num) + " of " + str(len(img_list)),relief=SUNKEN,bd = 3, anchor = E)
     back_button = Button(root, text = "<<" , command = lambda: backward(img_num))
     forward_button = Button(root, text = ">>" , command = lambda: forward(img_num))
     enter_button = Button(root,text="Enter",command = enter)
     #Widget layout

     back_button.grid(row = 1 , column = 0)
     forward_button.grid(row = 1 , column = 2)
     status.grid(row = 4, column = 0, columnspan = 3,sticky = W+E)

     if img_num == 0:
         img_num = len(img_list)
         #Widget updates
         my_image = ImageTk.PhotoImage(Image.open(img_list[img_num -1]).resize((400,500),Image.BOX))
         my_image_label = Label(image=my_image).grid(row = 0, column = 0, columnspan = 3)
         status = Label(root,text="Image "+ str(img_num) + " of " + str(len(img_list)),relief=SUNKEN,bd = 3, anchor = E)
         #Widget layout
         status.grid(row = 4, column = 0, columnspan = 3,sticky = W+E)
         
         
     


def forward(img_num):
    
     global my_image
     global img_list
     global my_image_label

     if img_num == len(img_list):
         img_num = 0
         my_image = ImageTk.PhotoImage(Image.open(img_list[img_num]).resize((400,500),Image.BOX))
         my_image_label = Label(image=my_image).grid(row = 0, column = 0, columnspan = 3)
         img_num +=1
         #Widget updates
         open_button = Button(root, text="Open file", command= lambda:open(img_num),bg="red")
         status = Label(root,text="Image "+ str(img_num) + " of " + str(len(img_list)),relief=SUNKEN,bd = 3, anchor = E)
         back_button = Button(root, text = "<<" , command = lambda: backward(img_num))
         forward_button = Button(root, text = ">>" , command = lambda: forward(img_num))
         enter_button = Button(root,text="Enter",command = enter)
         #Widget layout

         back_button.grid(row = 1 , column = 0)
         forward_button.grid(row = 1 , column = 2)
         status.grid(row = 4, column = 0, columnspan = 3,sticky = W+E)
     else:
         my_image = ImageTk.PhotoImage(Image.open(img_list[img_num]).resize((400,500),Image.BOX))
         my_image_label = Label(image=my_image).grid(row = 0, column = 0, columnspan = 3)
         img_num +=1

         #Widget updates
         open_button = Button(root, text="Open file", command= lambda:open(img_num),bg="red")
         status = Label(root,text="Image "+ str(img_num) + " of " + str(len(img_list)),relief=SUNKEN,bd = 3, anchor = E)
         back_button = Button(root, text = "<<" , command = lambda: backward(img_num))
         forward_button = Button(root, text = ">>" , command = lambda: forward(img_num))
         enter_button = Button(root,text="Enter",command = enter)
         #Widget layout

         back_button.grid(row = 1 , column = 0)
         forward_button.grid(row = 1 , column = 2)
         status.grid(row = 4, column = 0, columnspan = 3,sticky = W+E)
          
        
def exit():
    global response
    response = messagebox.askyesno("","Are you sure you want to exit?")
    if response == True:
        root.destroy()
    

def open(img_num):
    global my_image
    global img_list
    global my_image_label
    
    root.filename = filedialog.askopenfilename(initialdir = "C:/Users/MARK/Desktop/לימודים/WEB/projects/KillaSynth/images", title ="Select a file",filetypes=(("png files","*.png"),("jpg files","*jpg")))
    my_image = ImageTk.PhotoImage(Image.open(root.filename).resize((400,500),Image.BOX))
    img_num +=1
    
    
    my_image_label = Label(image=my_image).grid(row = 0, column = 0, columnspan = 3)
    img_list.append(root.filename)
    

    #Widget updates
    open_button = Button(root, text="Open file", command= lambda:open(img_num),bg="red")
    status = Label(root,text="Image "+ str(img_num) + " of " + str(len(img_list)),relief=SUNKEN,bd = 3, anchor = E)
   
    #Widget layout
    status.grid(row = 4, column = 0, columnspan = 3,sticky = W+E)
    open_button.grid(row= 1 , column = 1)
    
    if img_num > 1:
         back_button = Button(root, text = "<<" , command = lambda: backward(img_num))
         forward_button = Button(root, text = ">>" , command = lambda: forward(img_num))
         enter_button = Button(root,text="Enter",command = enter)

         back_button.grid(row = 1 , column = 0)
         forward_button.grid(row = 1 , column = 2)
         enter_button.grid(row = 2, column = 2)

    
    





# image list

img_list = []


# Widgets
open_button = Button(root, text="Open file", command= lambda:open(img_num),bg="red")
back_button = Button(root, text = "<<" , command = backward,state=DISABLED)
forward_button = Button(root, text = ">>" , command = forward,state=DISABLED)
exit_button = Button(root,text = "Exit", command = exit)
enter_button = Button(root,text="Enter",command = enter,state = DISABLED) 

# labels
status = Label(root,text="Image "+ str(img_num) + " of " + str(len(img_list)),relief=SUNKEN,bd = 3, anchor = E)
label = Label(root,text="Jump to: ")
e= Entry(root)

# Widgets layout
open_button.grid(row= 1 , column = 1)
back_button.grid(row = 1 , column = 0)
forward_button.grid(row = 1 , column = 2)
exit_button.grid(row = 3 , column = 1,padx=10,pady=10)
label.grid(row = 2, column = 0)
e.grid(row = 2 , column = 1)
status.grid(row = 4, column = 0, columnspan = 3,sticky = W+E)
enter_button.grid(row = 2, column = 2)

          
root.mainloop()
