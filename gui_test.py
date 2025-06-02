import tkinter as tk
root = tk.Tk()
root.title("Tkinter Test")
root.geometry("300x200")
tk.Label(root, text="If you see this, GUI works!").pack(expand=True)
root.mainloop()
