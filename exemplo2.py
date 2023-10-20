from tkinter .ttk import *
from tkinter import *

fonte = ("Cooper Black", "14")
window = Tk()
window.title("Escolha seu avatar")
window.geometry("400x300")
rotulo1 = Label(window, text="Escolha seu avatar", pady=20, font=fonte)
rotulo1.pack()
container1 = Frame(window, pady=20, padx=10)
container1.pack()
combo = Combobox(container1)
combo["values"] = ("arlequina", "chaplin", "gueixa", "ninja", "zorro")
combo["state"] = "readonly"
combo.current(0)
combo.pack(side=LEFT)

rotulo2 = Label(container1)

window.mainloop()