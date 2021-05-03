from tkinter import *

root = Tk()
#for the title of the application
root.title("Advance Calculator")

#for inserting the icone


e = Entry(root,width = 55, borderwidth = 15,bg = "white" )
e.grid(row = 0,column = 0,columnspan = 6, padx = 13, pady = 19)


# for additation of two number
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "add":
        e.insert(0, f_num + int(second_number))
    if math =="subtraction":
        e.insert(0, f_num - int(second_number))
    if math =="division":
        e.insert(0, f_num / int(second_number))
    if math =="multiply":
        e.insert(0, f_num * int(second_number))

#for two number subtraction

def button_subtraction():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

#for two number division
def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

#for two number multiply
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)

def button_clear():
    e.delete(0,END)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))

# for defining the button in calculator
button1 = Button(root,text = "1", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(1))
button2 = Button(root,text = "2", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(2))
button3 = Button(root,text = "3", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(3))
button4 = Button(root,text = "4", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(4))
button5 = Button(root,text = "5", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(5))
button6 = Button(root,text = "6", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(6))
button7 = Button(root,text = "7", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(7))
button8 = Button(root,text = "8", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(8))
button9 = Button(root,text = "9", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(9))
button0 = Button(root,text = "0", bg = "gray", padx = 35,pady = 15,command= lambda:button_click(0))

#this is for addintion and subtraction,multiply and division

button_equal = Button(root,text = "=", bg = "gray", padx = 35,pady = 15,command= button_equal)
button_clear = Button(root,text = "clearall", bg = "gray", padx = 35,pady = 15,command= button_clear)
button_add = Button(root,text = "+", bg = "gray", padx = 35,pady = 15,command= button_add)
button_subtraction = Button(root,text = "-", bg = "gray", padx = 35,pady = 15,command=button_subtraction)
button_division= Button(root,text = "/", bg = "gray", padx = 35,pady = 15,command=button_division)
button_multiply= Button(root,text = "*", bg = "gray", padx = 35,pady = 15,command= button_multiply)

#putting button on the screen
button1.grid(row=3,column = 0)
button2.grid(row=3,column = 1)
button3.grid(row=3,column = 2)

button4.grid(row=2,column = 0)
button5.grid(row=2,column = 1)
button6.grid(row=2,column = 2)

button7.grid(row=1,column = 0)
button8.grid(row=1,column = 1)
button9.grid(row=1,column = 2)

button0.grid(row=4,column = 0)
button_clear.grid(row=1,column = 3, columnspan = 1)
button_add.grid(row=2,column = 3)
button_equal.grid(row=4,column = 3, columnspan = 1)
button_subtraction.grid(row=3,column = 3)
button_division.grid(row=4,column = 2)
button_multiply.grid(row=4,column = 1)


#for closing the screen
root.mainloop()