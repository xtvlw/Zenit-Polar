#_[N_F]_
import tkinter as tk

window = tk.Tk()

def ButtonClick():
    zenit, polar = 'zenit', 'polar'
    final_message, n = '', 0
    message = str(box.get())
    for i in range(len(message)):
        x = message[n]
        if x in zenit:
            x = int(zenit.find(message[n]))
            final_message += polar[x]
        elif x in polar:
            x = int(polar.find(message[n]))
            final_message += zenit[x]
        else:
            final_message += message[n]
        n += 1
    label["text"] = final_message


box = tk.Entry(window, width=47)
box.place(x=5, y=5)

button = tk.Button(window, width=40,
                   text="Crypt/Decrypt",
                   command=ButtonClick)
button.place(x=5, y=55)

label = tk.Label(window, width=40,
                 text='message')
label.place(x=5, y=105)


window.title("Zenit Polar")
window.geometry("300x150")
window.mainloop()
