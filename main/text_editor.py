import tkinter as tk


def open_file():
    pass


def save_file():
    pass


window = tk.Tk()
window.title("Text editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

frame_left_panel = tk.Frame(master=window)
frame_left_panel.grid(row=0, column=0, padx=10, sticky="sn")

button_open = tk.Button(master=frame_left_panel, command=open_file, text="Open")
button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

button_save = tk.Button(master=frame_left_panel, command=save_file, text="Save as")
button_save.grid(row=1, column=0, sticky="ew", padx=5)

# frame_right_panel = tk.Frame(master=window, padx=10)
# frame_right_panel.grid(row=0, column=1, sticky="nsew")

text_editor = tk.Text(master=window)
text_editor.grid(row=0, column=1, sticky="nsew")

window.mainloop()
