import tkinter as tk

def on_digit_click(digit):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(digit))

def on_backspace_click():
    current = entry.get()
    if len(current) > 0:
        entry.delete(len(current) - 1)

def on_clear_click():
    entry.delete(0, tk.END)

def on_operator_click(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + operator)

def on_equal_click():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.configure(bg="lightgray")

entry = tk.Entry(root, justify="right", font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=6)
entry.config(bg="white", fg="black")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 5),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 5),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 5),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 5),
    ("back\nspace", 4, 5),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 16))
    button.grid(row=row, column=col)
    
    if text.isdigit() or text == ".":
        button.config(command=lambda digit=text: on_digit_click(digit))
    elif text in "+-*/":
        button.config(command=lambda operator=text: on_operator_click(operator))
    elif text == "=":
        button.config(command=on_equal_click)
    elif text == "back\nspace":
        button.config(command=on_backspace_click)
    else:
        button.config(command=on_clear_click)

    button.config(bg="orange", fg="white")
    
root.mainloop()
