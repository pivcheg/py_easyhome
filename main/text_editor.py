import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


def open_file():
    """Открывает файл для редактирования"""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filepath:
        return

    text_editor.delete("1.0", tk.END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_editor.insert(tk.END, text)

    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Сохраняем текущий файл как новый файл."""
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = text_editor.get("1.0", tk.END)
        output_file.write(text)

    window.title(f"Simple Text Editor - {filepath}")


window = tk.Tk()
window.title("Text editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

frame_left_panel = tk.Frame(master=window, relief="raised", bd=2)
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
