import tkinter as tk
from time import strftime

 
def update_time():
    time_string = strftime('%I:%M:%S %p')
    clock_label.config(text=time_string)
    clock_label.after(1000, update_time)

# Set up the main window
root = tk.Tk()
root.title("🕒 Digital Clock")
root.geometry("800x300")
root.resizable(False, False)
root.configure(bg="#121212")

# Centered clock label
clock_label = tk.Label(
    root,
    font=("DS-Digital", 100),  
    background="#121212",
    foreground="#00FF00",
    padx=20,
    pady=20
)
clock_label.pack(expand=True)

# Start the clock
update_time()
root.mainloop()
