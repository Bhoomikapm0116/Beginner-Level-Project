import tkinter as tk
import time
from tkinter import messagebox

def countdown(t):
    def update_timer():
        nonlocal t
        if t > 0:
            hrs, rem = divmod(t, 3600)  
            mins, secs = divmod(rem, 60) 
            timer_label.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
            canvas.itemconfig(circle, outline="green", width=2 + t % 10)
            t -= 1
            root.after(1000, update_timer)
        else:
            timer_label.config(text="00:00:00")
            canvas.itemconfig(circle, outline="red", width=4)
            messagebox.showinfo("Timer Finished", "Completed!")

    update_timer()

def start_timer():
    try:
        time_input = entry.get()
        if ":" in time_input: 
            time_parts = time_input.split(":")
            if len(time_parts) == 3: 
                hrs, mins, secs = map(int, time_parts)
                t = hrs * 3600 + mins * 60 + secs  
            elif len(time_parts) == 2:  
                mins, secs = map(int, time_parts)
                t = mins * 60 + secs 
            else:
                raise ValueError("Invalid time format. Please use hh:mm:ss or mm:ss.")
        else:
            t = int(time_input) 
        
        if t <= 0:
            raise ValueError("Please enter a positive number.")
        countdown(t)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

root = tk.Tk()
root.title("Countdown Timer")

timer_label = tk.Label(root, text="00:00:00", font=("Times New Roman", 40), fg="black")
timer_label.pack(pady=20)

canvas = tk.Canvas(root, width=200, height=200, bg="black", highlightthickness=0)
canvas.pack()
circle = canvas.create_oval(50, 50, 150, 150, outline="green", width=2)

frame = tk.Frame(root)
frame.pack(pady=20)
entry = tk.Entry(frame, font=("Times New Roman", 20), width=8)
entry.pack(side="left", padx=10)
start_button = tk.Button(frame, text="Start Timer", command=start_timer, font=("Times New Roman", 14), bg="pink")
start_button.pack(side="left")

root.mainloop()
