import tkinter as tk

# Создается новое окно с заголовком "Введите домашний адрес".
window = tk.Tk()
window.title("Address Entry Form")

# Создается новая рамка `frm_form` для ярлыков с текстом и
# Однострочных полей для ввода информации об адресе.
frame_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Помещает рамку на окно приложения.
frame_form.pack()

labels = [
    "Имя:",
    "Фамилия:",
    "Адрес 1:",
    "Адрес 2:",
    "Город:",
    "Регион:",
    "Почтовый индекс:",
    "Страна:",
]

# Цикл для списка ярлыков полей.
for index, key in enumerate(labels):
    # Создает ярлык с текстом из списка ярлыков.
    label = tk.Label(master=frame_form, text=key)
    # Создает текстовое поле которое соответствует ярлыку.
    entry = tk.Entry(master=frame_form, width=50)
    # Использует менеджер геометрии grid для размещения ярлыков и
    # текстовых полей в строку, чей индекс равен idx.
    label.grid(row=index, column=0, sticky="e")
    entry.grid(row=index, column=1)

# Создает новую рамку `frm_buttons` для размещения в ней
# кнопок "Отправить" и "Очистить". Данная рамка заполняет
# все окно в горизонтальном направлении с
# отступами в 5 пикселей горизонтально и вертикально.
frame_buttons = tk.Frame()
frame_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Создает кнопку "Отправить" и размещает ее
# справа от рамки `frm_buttons`.
button_submit = tk.Button(master=frame_buttons, text="Submit")
button_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Создает кнопку "Очистить" и размещает ее
# справа от рамки `frm_buttons`.
btn_clear = tk.Button(master=frame_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()