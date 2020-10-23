import tkinter as tk
import random as rnd


def convert():
    """
    Конвертирует значение из градусов по Фаренгейту в градусы
    по Цельсию и выводит результат в ярлык lbl_result.
    """
    fahrenheit = entry_fahrenheit.get()

    if fahrenheit:
        celsius = (5 / 9) * (float(fahrenheit) - 32)
        label_celsius["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    else:
        window_warn = tk.Tk()
        window_warn.title("ОШИБКА!")
        tk.Label(master=window_warn, text="Введите значение", fg="red", width=50).grid()


window = tk.Tk()
window.title("Temp")
window.resizable(width=False, height=False)

# Создание рамки для ввода значения по Фаренгейту через виджет однострочного текстового поля вместе с ярлыком.
frame_entry = tk.Frame(master=window)
frame_entry.grid(row=0, column=0, padx=10)

entry_fahrenheit = tk.Entry(master=frame_entry, width=10)
entry_fahrenheit.grid(row=0, column=0, sticky="e")

label_fahrenheit = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}", width=3)
label_fahrenheit.grid(row=0, column=1, sticky="w")

button_convert = tk.Button(master=window, text="\N{RIGHTWARDS ARROW}", command=convert)
button_convert.grid(row=0, column=1, pady=10)

label_celsius = tk.Label(master=window, text="---")
label_celsius.grid(row=0, column=2, padx=10)

window.mainloop()