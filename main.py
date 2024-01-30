from tkinter import *

win = Tk()  # This is to create a basic window
win.geometry("312x324")  # this is for the size of the window
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")

# Darker theme colors
bg_color = "#212121"  # Dark background color
btn_bg_color = "#424242"  # Darker button background color
btn_fg_color = "white"  # Button text color
entry_bg_color = "#333"  # Darker entry background color
entry_fg_color = "white"  # Entry text color

###################Starting with functions ####################
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
    except (ZeroDivisionError, ArithmeticError, SyntaxError) as e:
        input_text.set("Error")
    expression = ""

expression = ""
input_text = StringVar()

# Creating a frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2, bg=bg_color)
input_frame.pack(side=TOP)

# Creating an input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg=entry_bg_color,
                    bd=0, justify=RIGHT, foreground=entry_fg_color)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(win, width=312, height=272.5, bg=bg_color)
btns_frame.pack()

# Button styles for the darker theme
btn_style = {"width": 10, "height": 3, "bd": 0, "cursor": "hand2", "foreground": btn_fg_color}

# First row
clear = Button(btns_frame, text="C", fg=btn_fg_color, bg=btn_bg_color, command=bt_clear, **btn_style).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click("/"), **btn_style).grid(row=0, column=3, padx=1, pady=1)

# Second row
seven = Button(btns_frame, text="7", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(7), **btn_style).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(8), **btn_style).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(9), **btn_style).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click("*"), **btn_style).grid(row=1, column=3, padx=1, pady=1)

# Third row
four = Button(btns_frame, text="4", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(4), **btn_style).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(5), **btn_style).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(6), **btn_style).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click("-"), **btn_style).grid(row=2, column=3, padx=1, pady=1)

# Fourth row
one = Button(btns_frame, text="1", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(1), **btn_style).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(2), **btn_style).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(3), **btn_style).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click("+"), **btn_style).grid(row=3, column=3, padx=1, pady=1)

# Fifth row
zero = Button(btns_frame, text="0", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click(0), width=21, height=3, bd=0, cursor="hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text=".", fg=btn_fg_color, bg=btn_bg_color, command=lambda: btn_click("."), **btn_style).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg=btn_fg_color, bg=btn_bg_color, command=bt_equal, **btn_style).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
