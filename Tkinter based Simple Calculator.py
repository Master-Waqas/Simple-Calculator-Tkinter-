from tkinter import *
root = Tk()
root.title("Calculator")

def Calculate():
    a = int(enter_number_1.get())
    b = int(enter_number_2.get())
    op = enter_opt.get()
    print (a)
    ans = Label(root, text="Answer: ", font=("calibri", 15, "bold"), fg="red")
    ans.grid(row=4, column=1)

    if op == "+":
        ans = Label(root, text=a + b, font=("calibri", 15, "bold"), fg="red")
        ans.grid(row=4, column=2)
    elif op == "-":
        ans = Label(root, text=a - b, font=("calibri", 15, "bold"), fg="red")
        ans.grid(row=4, column=2)
    elif op == "*":
        ans = Label(root, text=a * b, font=("calibri", 15, "bold"), fg="red")
        ans.grid(row=4, column=2)
    elif op == "/":
        ans = Label(root, text=a / b, font=("calibri", 15, "bold"), fg="red")
        ans.grid(row=4, column=2)
    else:
        ans = Label(root, text="WRONG CREDENTIALS . . . .", font=("calibri", 15, "bold"), fg="red")
        ans.grid(row=4, column=1)

number_1 = Label(root, text = "Enter 1st Number:", font = ("calibri", 15, "bold"))
number_1.grid(row = 0, column = 1)

enter_number_1 = Entry(font = ("calibri", 15, "bold"))
enter_number_1.grid(row = 0, column = 2, pady = 5)

number_2 = Label(root, text = "Enter 2nd Number:", font = ("calibri", 15, "bold"))
number_2.grid(row = 1, column = 1)

enter_number_2 = Entry(font = ("calibri", 15, "bold"))
enter_number_2.grid(row = 1, column = 2, pady = 5)

opt = Label(root, text = "Enter Operator:\n +,-,*,/", font = ("calibri", 10, "bold"))
opt.grid(row = 2, column = 1)

enter_opt = Entry(font = ("calibri", 15, "bold"))
enter_opt.grid(row = 2, column = 2, pady = 5)


calc = Button(root, text = "Calculate", font = ("calibri", 15, "bold"), bg = "black", fg = "gold", command = Calculate)
calc.grid(row = 3, column = 1, pady = 5)


root.mainloop()