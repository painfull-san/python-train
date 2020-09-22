import tkinter as tk
import datetime

root = tk.Tk()

lab = tk.Label(root)
lab.pack()

def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    root.after(1000, clock)

clock()

root.mainloop()
