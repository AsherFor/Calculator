from tkinter import *

master = Tk()
master.title("My First Window")
master.geometry("160x130")
master.configure(background = "deep sky blue")

#Function to test button press
def test_line():
    print("Button Press")


def print_box_val(numb):
    # print(numb)
    String_input_value_saved = String_input_value.get()
    print(String_input_value_saved)
    input_box_str = String_input_value_saved + str(numb)
    String_input_value.set(input_box_str)

def do_math():
    # print("do math")
    String_input_value_saved = String_input_value.get()
    print(String_input_value_saved)
    eval(String_input_value_saved)
    total = eval(String_input_value_saved)
    String_input_value_saved.set(total)



#Buttons
#Add Button
plus_sign = "+"
add = Button(master, text = "+", command = lambda plus_sign = plus_sign: print_box_val(plus_sign), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
add.grid(row = 1, column = 4)

#Subtract Button
minus_sign = "-"
subtract = Button(master, text = "-", command = lambda minus_sign = minus_sign: print_box_val(minus_sign), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
subtract.grid(row = 2, column = 4)

#Multiply Button
times_sign = "*"
multiply = Button(master, text = "*", command = lambda times_sign = times_sign: print_box_val(times_sign), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
multiply.grid(row = 3, column = 4)

#Divide Button
div_sign = "/"
divide = Button(master, text = "/", command = lambda div_sign = div_sign: print_box_val(div_sign), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
divide.grid(row = 4, column = 4)

#Claculate Button
calculate = Button(master, text = "=", command = do_math, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
calculate.grid(row = 4, column = 2)

#Buttons 0
Zero_sign = "0"
Zero = Button(master, text = "0", command = lambda Zero_sign = Zero_sign: Zero_sign(Zero_sign), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue") #try taking out zerosign = zerosign
Zero.grid(row = 4, column = 1)

#Loop to create numbers 1-9
number = 1
for i in range(1, 4):
    for j in range(3):
        num_to_string = str(number)
        button_name = "button" + num_to_string
        # print(button_name)
        button_name = Button(master, text = number, command=lambda number=number: print_box_val(number), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
        button_name.grid(row = i, column = j)
        number = number + 1


String_input_value = StringVar(master, value='')
Total_box = Entry(master,textvariable=String_input_value)
Total_box.grid(row=0, columnspan=4, sticky=W + E)

master.mainloop() #Always put at the end