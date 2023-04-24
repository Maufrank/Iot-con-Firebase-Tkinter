from tkinter import Tk, Frame, Label, StringVar, IntVar,Checkbutton, Button, ttk, Scrollbar

miVentana= Tk()
miVentana.title("Detector de colores")
miVentana.resizable(0,0)
miVentana.geometry("550x600")
estado_color = StringVar()
back_color = StringVar()
conx = StringVar()

conect = StringVar()
estaCorriendo = True
registrosT = StringVar()
modo = StringVar()
mode = 'n'




frame1 = Frame(miVentana)
frame1.pack(fill='both', expand=True)

frame2 = Frame(miVentana)
frame2.pack(fill='both', expand=True)

frame4 = Frame(miVentana)
frame4.pack(fill='both', expand=True)

frame3 = Frame(miVentana)
frame3.pack(fill='both', expand=True)



    

Label(frame1, text="..:: Detector de color ::..").grid(row=0,column=2, padx=5, pady=5, sticky="we")
Label(frame1, textvariable=estado_color, width=10, borderwidth=2, relief="groove", fg="white", bg="black", font=("Courier New", 15, "bold")).grid(row=2, column=2, padx=5, pady=5, sticky="we")
Label(frame1, text="..:: Estado ::..").grid(row=3,column=2, padx=5, pady=5, sticky="we")
Label(frame2, text="..:: Colores ::..").grid(row=5,column=2, padx=5, pady=5, sticky="we")
Label(frame4, text="..:: Filtros ::..").grid(row=0,column=2, padx=5, pady=5, sticky="we")


# Label(frame3, textvariable=registrosT, width=43, borderwidth=2, relief="groove", bg="white", fg="black", font=("Courier New", 15, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky="we")
Label(frame3, textvariable=conx).grid(row=3,column=0, padx=5, pady=5, sticky="we")


scroll = Scrollbar(frame3, orient="vertical")

tabla = ttk.Treeview(frame3,  columns=('1', '2', '3', '4', '5', '6'), yscrollcommand=scroll.set)



tabla.grid(row=2,column=0, padx=5, pady=5, sticky="we")
scroll.grid(row=2, column=1, sticky='ns')
scroll.config(command=tabla.yview)

tabla.column("#0", width=40, anchor="center")
tabla.column("1", width=80, anchor="center")
tabla.column("2", width=80, anchor="center")
tabla.column("3", width=80, anchor="center")
tabla.column("4", width=80, anchor="center")
tabla.column("5", width=80, anchor="center")
tabla.column("6", width=80, anchor="center")


tabla.heading("#0", text="Id")
tabla.heading("1", text="Color")
tabla.heading("2", text="C. Rojo")
tabla.heading("3", text="C. Verde")
tabla.heading("4", text="C. Azul")
tabla.heading("5", text="Fecha")
tabla.heading("6", text="Hora")



boton1 = Button(frame1, width=10, text="Manual")
boton1.grid(row=4,column=1, padx=50, pady=3)

boton2 = Button(frame1, width=10, text="Automatico")
boton2.grid(row=4,column=3, padx=50, pady=3)

rojo = Button(frame2, width=10, text="Rojo")
rojo.grid(row=6,column=0, padx=10, pady=5)

blanco = Button(frame2, width=10, text="Blanco")
blanco.grid(row=6,column=1, padx=10, pady=5)

naranja = Button(frame2, width=10, text="Naranja")
naranja.grid(row=6,column=2, padx=10, pady=5)

verde = Button(frame2, width=10, text="Verde")
verde.grid(row=6,column=3, padx=10, pady=5)

azul = Button(frame2, width=10, text="Azul")
azul.grid(row=6,column=4, padx=10, pady=5)


consultaRojo = Button(frame4, width=8, text="Rojo")
consultaRojo.grid(row=1,column=0, padx=5, pady=5)

consultaBlanco = Button(frame4, width=8, text="Blanco")
consultaBlanco.grid(row=1,column=1, padx=5, pady=5)

consultaNaranja = Button(frame4, width=8, text="Naranja")
consultaNaranja.grid(row=1,column=2, padx=5, pady=5)

consultaVerde = Button(frame4, width=8, text="Verde")
consultaVerde.grid(row=1,column=3, padx=5, pady=5)

consultaAzul = Button(frame4, width=8, text="Azul")
consultaAzul.grid(row=1,column=4, padx=5, pady=5)

sinFiltro = Button(frame4, width=8, text="S/F")
sinFiltro.grid(row=1,column=5, padx=5, pady=5)

masRojo = Button(frame4, width=10, text="Con mas\nrojo")
masRojo.grid(row=2,column=0, padx=5, pady=5)

menosRojo = Button(frame4, width=10, text="Con menos\nrojo")
menosRojo.grid(row=2,column=1, padx=5, pady=5)

# masAzul = Button(frame4, width=10, text="Con mas\nazul")
# masAzul.grid(row=2,column=4, padx=5, pady=5)

# menosAzul = Button(frame4, width=10, text="Con menos\nazul")
# menosAzul.grid(row=2,column=5, padx=5, pady=5)

# masVerde = Button(frame4, width=10, text="Con mas\nverde")
# masVerde.grid(row=2,column=2, padx=5, pady=5)

# menosVerde = Button(frame4, width=10, text="Con menos\nverde")
# menosVerde.grid(row=2,column=3, padx=5, pady=5)

def insertar_tabla(datos):
    registros = tabla.get_children()
    for registro in registros:
        tabla.delete(registro)
    for dato in datos:
        tabla.insert("", 0, text=dato[0], values=(dato[1], dato[2], dato[3], dato[4], dato[5], dato[6],))




# miVentana.mainloop()