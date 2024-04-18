import tkinter as tk
from tkinter import *

calculation = ""

# every symbol pressed will be stored into calculation variable through this function
def add_to_calculation(symbol):
    global calculation
    if symbol == '÷':
        symbol = '/'  # Replace '÷' with '/'
    elif symbol == 'x':
        symbol = '*'  # Replace 'x' with '*'
    elif symbol == '%':
        symbol = '/100'
    calculation += str(symbol)
    display_text = calculation.replace('/', ' ÷ ').replace('*', ' × ')  # Format for display
    text_result.delete(1.0, "end")
    # updates the display ui for the symbols
    text_result.insert(1.0, display_text)

# actual calculation starts here
def evaluate_calculation():
    global calculation
    try:
        # eval may cause security problems if trying to go public
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# removes everything for the screen display
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# self explanatory
root = tk.Tk()
# for the image use your own file source below is merely an example
img = PhotoImage(file='C:/folder/calculator_icon.png')
root.iconphoto(False, img)
root.title("Calculator")
root.configure(background='white')
root.geometry("300x275")
root.resizable(width=False, height=False)
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="lightgray")
text_result.grid(columnspan=5)

# button gallore
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=3, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=3, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=3, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=4, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=4, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=4, column=3)
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=5, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=5, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=5, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=6, column=1)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=6, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=5, column=4)
btn_times = tk.Button(root, text="\u00D7", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_times.grid(row=4, column=4)  # Unicode for multiplication symbol
btn_divide = tk.Button(root, text="\u00F7", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=3, column=4)  # Unicode for division symbol
btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_decimal.grid(row=6, column=2)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 14), bg="#99c3ff")
btn_equals.grid(row=6, column=3)
btn_clear = tk.Button(root, text="AC", command=clear_field, width=5, font=("Arial", 14), bg="orange")
btn_clear.grid(row=2, column=1)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=2, column=2)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=2, column=3)
btn_percentage = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), width=5, font=("Arial", 14))
btn_percentage.grid(row=2, column=4)

# repeats the window so it doesn't just close after opening
root.mainloop()
