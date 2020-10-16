import tkinter as tk

window = tk.Tk()
window.title("Введите домашний адрес")

# window.rowconfigure(0, minsize=50)
# window.columnconfigure(0, minsize=30)
# window.columnconfigure(1, minsize=30)
# window.columnconfigure(2, minsize=10)

frame_info = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=2)
frame_info.pack()

label_name = tk.Label(master=frame_info, text="Имя:")
entry_name = tk.Entry(master=frame_info, width=50)
label_name.grid(row=0, column=0, sticky="e")
entry_name.grid(row=0, column=1)

label_surname = tk.Label(master=frame_info, text="Фамилия:")
entry_surname = tk.Entry(master=frame_info, width=50)
label_surname.grid(row=1, column=0, sticky="e")
entry_surname.grid(row=1, column=1)

label_address_1 = tk.Label(master=frame_info, text="Адрес1:")
entry_address_1 = tk.Entry(master=frame_info, width=50)
label_address_1.grid(row=2, column=0, sticky="e")
entry_address_1.grid(row=2, column=1)

label_address_2 = tk.Label(master=frame_info, text="Адрес2:")
entry_address_2 = tk.Entry(master=frame_info, width=50)
label_address_2.grid(row=3, column=0, sticky="e")
entry_address_2.grid(row=3, column=1)

label_city = tk.Label(master=frame_info, text="Город:")
entry_city = tk.Entry(master=frame_info, width=50)
label_city.grid(row=4, column=0, sticky="e")
entry_city.grid(row=4, column=1)

label_region = tk.Label(master=frame_info, text="Регион:")
entry_region = tk.Entry(master=frame_info, width=50)
label_region.grid(row=5, column=0, sticky="e")
entry_region.grid(row=5, column=1)

label_postal = tk.Label(master=frame_info, text="Почтовый индекс:")
entry_postal = tk.Entry(master=frame_info, width=50)
label_postal.grid(row=6, column=0, sticky="e")
entry_postal.grid(row=6, column=1)

label_country = tk.Label(master=frame_info, text="Страна:")
entry_country = tk.Entry(master=frame_info, width=50)
label_country.grid(row=7, column=0, sticky="e")
entry_country.grid(row=7, column=1)

frame_buttons = tk.Frame(master=window)
frame_buttons.pack(fill="x", ipadx=5, ipady=5)

button_clear = tk.Button(master=frame_buttons, text="Очистить")
button_send = tk.Button(master=frame_buttons, text="Отправить")
button_send.pack(side="right", ipadx=15, ipady=10)
button_clear.pack(side="right", ipadx=15, ipady=10)



window.mainloop()

