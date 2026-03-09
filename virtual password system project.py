import tkinter as tk
from tkinter import messagebox
import random

# Variables initialization
real_password = "2006"
entered_password = ""
attempts_count = 0 

# 1. Shuffle keypad characters
def generate_keypad():
    chars = list("0123456789ABC@#") 
    random.shuffle(chars)
    return chars

# Button click logic
def press(char):
    global entered_password
    entered_password += str(char)
    display_var.set("*" * len(entered_password))

# 2. Clear button logic
def clear_entry():
    global entered_password
    entered_password = ""
    display_var.set("")

# 3. Login logic with Attempt Limit
def check_password():
    global entered_password, attempts_count
    
    if entered_password == real_password:
        messagebox.showinfo("Success", "Access Granted!")
        attempts_count = 0
        root.destroy()
    else:
        attempts_count += 1
        remaining = 3 - attempts_count
        if attempts_count >= 3:
            messagebox.showerror("Locked", "you entered it wrong 3 times! System Locked.")
            root.destroy()
        else:
            messagebox.showwarning("Denied", f"Wrong Password! {remaining} chances left.")
            clear_entry()

# GUI window setup
root = tk.Tk()
root.title("Virtual Password System")
root.geometry("350x550")

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify="center", state="readonly")
display.pack(pady=20, padx=10)

frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=20)

# Configure grid columns to be equal size
for i in range(3):
    frame.grid_columnconfigure(i, weight=1)

chars = generate_keypad()
row, col = 0, 0

for char in chars:
    # 'sticky="nsew"' makes buttons uniform in size
    btn = tk.Button(frame, text=str(char), width=5, height=2, font=("Arial", 12, "bold"),
                    command=lambda c=char: press(c))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    
    col += 1
    if col > 2:
        col = 0
        row += 1

# Login Button (Green)
check_btn = tk.Button(root, text="Login", font=("Arial", 12, "bold"), 
                      bg="#4CAF50", fg="white", width=20, command=check_password)
check_btn.pack(pady=10)

# Clear Button (Red)
clear_btn = tk.Button(root, text="Clear", font=("Arial", 12, "bold"), 
                      bg="#f44336", fg="white", width=20, command=clear_entry)
clear_btn.pack(pady=5)

root.mainloop()

