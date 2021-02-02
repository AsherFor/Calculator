from tkinter import *

master = Tk()
master.title("My First Window")
master.geometry("160x130")
master.configure(background = "deep sky blue")

#Function to test button press
def test_line():
    print("Button Press")

#Buttons
#Add Button
add = Button(master, text = "+", command = test_line, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
add.grid(row = 1, column = 4)

#Subtract Button
subtract = Button(master, text = "-", command = test_line, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
subtract.grid(row = 2, column = 4)

#Multiply Button
multiply = Button(master, text = "*", command = test_line, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
multiply.grid(row = 3, column = 4)

#Divide Button
divide = Button(master, text = "/", command = test_line, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
divide.grid(row = 4, column = 4)

#Claculate Button
calculate = Button(master, text = "=", command = test_line, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
calculate.grid(row = 4, column = 2)

#Buttons 0
Zero = Button(master, text = "0", command = test_line, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
Zero.grid(row = 4, column = 1)

#Loop to create numbers 1-9
number = 1
for i in range(1, 4):
    for j in range(3):
        num_to_string = str(number)
        button_name = "button" + num_to_string
        print(button_name)
        button_name = Button(master, text = number, command = test_line, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
        button_name.grid(row = i, column = j)
        number = number + 1


String_input_value = StringVar(master, value='')
Total_box = Entry(master,textvariable=String_input_value)
Total_box.grid(row=0, columnspan=4, sticky=W + E)

master.mainloop() #Always put at the end