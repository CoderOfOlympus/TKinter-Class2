import tkinter as tk
root = tk.Tk()
root.title("Class 2")

root.geometry("300x200")
def on_buttton_click():
    label.config(text = "Button clicked")
def on_key_press(event):
    label.config(text = f"key pressed:{event.char}")
def on_mouse_enter(event):
    label.config(text = "Mouse entered")    
def on_mouse_leave(event):
    label.config(text = "Mouse left")
    

label = tk.Label(root,text = "Press a button or a key.",font = ("Arial",12))
label.pack(pady=20)
button=tk.Button(root,text = "Click",command=on_buttton_click)
button.pack(pady = 10)

root.bind("<KeyPress>",on_key_press)
button.bind("<Enter>",on_mouse_enter)
button.bind("<Leave>",on_mouse_leave)


root.mainloop()
