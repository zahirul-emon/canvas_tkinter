from tkinter import *

root = Tk()
root.title("Canvas")
root.geometry("650x550")
root.configure(bg = "violet")
my_canv = Canvas(root, width = 650, height = 550, bg = "yellow")
my_canv.place(x = 0, y = 0)

#Shape drawing functions
def draw_line(event):
    global click, x1, y1
    if click == 0:
        x1 = event.x
        y1 = event.y
        click = 1
    else:
         x2 = event.x
         y2 = event.y
         my_canv.create_line(x1, y1, x2, y2, fill = "red", width = 2)
         click = 0
         
def draw_oval(event):
    global click, x1, y1
    if click == 0:
        x1 = event.x
        y1 = event.y
        click = 1
    else:
         x2 = event.x
         y2 = event.y
         my_canv.create_oval(x1, y1, x2, y2, fill = "pink", width = 2)
         click = 0

def draw_rect(event):
    global click, x1, y1
    if click == 0:
        x1 = event.x
        y1 = event.y
        click = 1
    else:
         x2 = event.x
         y2 = event.y
         my_canv.create_rectangle(x1, y1, x2, y2, outline = "red",fill = "purple", width = 2)
         click = 0
#Binding funtions to Button-1   
def OptionMenuSelect(event):
    if var.get() == "oval":
       my_canv.bind("<Button-1>", draw_oval)
       
    elif var.get() == "line":
        my_canv.bind("<Button-1>", draw_line)
        
    elif var.get() == "rectangle":
        my_canv.bind("<Button-1>", draw_rect)
    
        
    
#Button functions
def clear():
    my_canv.delete("all")
    
def exit_():
    root.destroy()
    
def white():
    my_canv["bg"] = "white"
    
def yellow():
    my_canv["bg"] = "yellow"
    
def green():
    my_canv["bg"] = "green"       
        


#Buttons    
Button(root, text = "clear all", command = clear, bg = "#03befc").place(x = 200)
Button(root, text = "exit", command = exit_, bg = "red").place(x = 250)
Button(root, text = "White Screen", command = white, bg = "white").place(x = 300)
Button(root, text = "Yellow Screen", command = yellow, bg = "yellow").place(x = 400)
Button(root, text = "Green Screen", command = green, bg = "green").place(x = 500)

click = 0    
var = StringVar()
var.set("What you want to draw?")
options = [var, "line","oval","rectangle"]
OptionMenu(root, *options, command = OptionMenuSelect).place(x = 0, y = 0)
root.mainloop()
