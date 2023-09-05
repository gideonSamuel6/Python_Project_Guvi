import tkinter as tk
from math import *

root = tk.Tk()
root.title("Scientific Calculator")

def button_click(event):
    current_text = display.get()
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            result = eval(current_text)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif button_text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, button_text)

display = tk.Entry(root, font=('Arial', 20))
display.grid(row=0, column=0, columnspan=4)

button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3)
]

for (text, row, col) in button_texts:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 15))
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)

root.mainloop()
