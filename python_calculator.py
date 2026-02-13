# # Simple Calculator

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("Choose operation:")
# print("1. Addition (+)")
# print("2. Subtraction (-)")
# print("3. Multiplication (*)")
# print("4. Division (/)")

# choice = input("Enter choice (1/2/3/4): ")

# if choice == '1':
#     print("Result:", num1 + num2)

# elif choice == '2':
#     print("Result:", num1 - num2)

# elif choice == '3':
#     print("Result:", num1 * num2)

# elif choice == '4':
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error! Division by zero.")

# else:
#     print("Invalid choice")


import tkinter as tk

def button_click(value):
    if value == "=":
        try:
            entry_var.set(eval(entry_var.get()))
        except:
            entry_var.set("Error")
    elif value == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + value)


root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")   # default size
root.resizable(True, True) # ✅ maximize enabled

entry_var = tk.StringVar()
entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 24),
    justify="right",
    bd=10
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10)

buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
    ("C",5,0)
]

for text, row, col in buttons:
    tk.Button(
        root,
        text=text,
        font=("Arial", 16),
        width=5,
        height=2,
        command=lambda t=text: button_click(t)
    ).grid(row=row, column=col, padx=5, pady=5)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

