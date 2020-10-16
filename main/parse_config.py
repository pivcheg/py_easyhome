import xmltodict
import tkinter as tk

xml_file = open("config.xml", "rb")
dict_parsed = xmltodict.parse(xml_file)

# for main in dict_parsed:
#     #print(dict_parsed[main])
#     for keys in dict_parsed[main]:
#         #print(keys, dict_parsed[main][keys])
#         pass

ip_address_1 = dict_parsed['config']['ipaddress']['@value']
ip_address_2 = dict_parsed['config']['ipaddress2']['@value']
ip_port_1 = dict_parsed['config']['ipport']['@value']
ip_port_2 = dict_parsed['config']['ipport2']['@value']
offset = dict_parsed['config']['offset']['@value']
draw_type = dict_parsed['config']['drawtype']['@value']
hide_navigation_bar = dict_parsed['config']['hidenavigationbar']['@value']
show_settings = dict_parsed['config']['show_settings']['@value']
width = dict_parsed['config']['width']['@value']
wnd_view = dict_parsed['config']['wndview']['@value']
zoom_height = dict_parsed['config']['zoomheight']['@value']
zoom_width = dict_parsed['config']['zoomwidth']['@value']

print(f"IP_1: {ip_address_1}:{ip_port_1}")
print(f"IP_2: {ip_address_2}:{ip_port_2}")
print(f"Offset: {offset}")
print(f"Draw type: {draw_type}")
print(f"Hide navigation bar: {hide_navigation_bar}")
print(f"Show settings: {show_settings}")
print(f"Width: {width}")
print(f"Wndview: {wnd_view}")
print(f"Zoomheight: {zoom_height}")
print(f"Zoomwidth: {zoom_width}")

window = tk.Tk()

frame_a = tk.Frame(master=window, borderwidth=5, relief=tk.SUNKEN)
frame_a.pack()

greeting = tk.Label(text="config.xml", master=frame_a)
greeting.pack()

entry_a = tk.Label(master=frame_a, width=40, fg="black", bg="white", text=f"IP_1: {ip_address_1}")
entry_a.pack()

window = tk.Tk()

frame1 = tk.Frame(master=window, height=150, width=50, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, height=50, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


frame3 = tk.Frame(master=window, height=100, width=150, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


xml_file.close()

window.mainloop()