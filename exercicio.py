from tkinter.ttk import *
from tkinter import *

window = Tk()
window.title("Escolha seu combo")
window.geometry("700x800")
container1 = Frame(window)
container1.pack()

rotuloLanche = Label(container1, text="Lanche")
rotuloLanche["font"] = ("", "12", "bold")
rotuloLanche.pack(side=LEFT)
comboLanche = Combobox(container1)
comboLanche["values"] = ("Burger", "Noodles", "Pizza")
comboLanche.current(0)
comboLanche.pack(side=LEFT, padx=10)

##########################################################

container2 = Frame(window)
container2.pack()

rotuloPorcao = Label(container2, text="Porção")
rotuloPorcao["font"] = ("", "12", "bold")
rotuloPorcao.pack(side=LEFT)
comboPorcao = Combobox(container2)
comboPorcao["values"] = ("Fritas", "Nuggets", "Milho")
comboPorcao.current(0)
comboPorcao.pack(side=LEFT, padx=10)

##########################################################

container3 = Frame(window)
container3.pack()

rotuloBebida = Label(container3, text="Bebida")
rotuloBebida["font"] = ("", "12", "bold")
rotuloBebida.pack(side=LEFT)
comboBebida = Combobox(container3)
comboBebida["values"] = ("Suco", "Shake")
comboBebida.current(0)
comboBebida.pack(side=LEFT, padx=10)


##########################################################

containerImagens = Frame(window)
containerImagens.pack()

escolha1 = PhotoImage(file="./cardapio/escolha.png")
escolha2 = PhotoImage(file="./cardapio/escolha.png")
escolha3 = PhotoImage(file="./cardapio/escolha.png")

label1 = Label(containerImagens, image=escolha1)
label2 = Label(containerImagens, image=escolha2)
label3 = Label(containerImagens, image=escolha3)
label2.pack(side=LEFT, padx=20, pady=60)
label3.pack(side=LEFT, padx=20, pady=60)
label1.pack(side=LEFT, padx=20, pady=60)

##########################################################

containerButton = Frame(window)
containerButton.pack()






window.mainloop()
