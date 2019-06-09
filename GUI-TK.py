from tkinter import *

raiz=Tk()

mi_frame=Frame(raiz,width=300,height=300)
mi_frame.pack()
#botones-----------------
boton_cimientos=Button(mi_frame,text="CIMIENTO")
boton_cimientos.grid(row=1,column=0)
boton_paredes=Button(mi_frame,text="PAREDES")
boton_paredes.grid(row=1,column=1)
boton_contrapiso=Button(mi_frame,text="CONTRAPISO")
boton_contrapiso.grid(row=1,column=2)
boton_techos=Button(mi_frame,text="TECHOS")
boton_techos.grid(row=1,column=3)
#Entrys--------------------con Labels
label_ancho=Label(mi_frame,text="ingresa el ancho")
label_ancho.grid(row=0,column=0)
cuadro_ancho=Entry(mi_frame)
cuadro_ancho.grid(row=0,column=1)
label_largo=Label(mi_frame,text="ingresa el largo")
label_largo.grid(row=0,column=2)
cuadro_largo=Entry(mi_frame)
cuadro_largo.grid(row=0,column=3)
#checkbutton-----------------------------
#checkCIMIENTOS--------------
check_zapatacorrida=Checkbutton(mi_frame,text="zapata corrida ",onvalue=1,offvalue=0)
check_zapatacorrida.grid(row=2,column=0,sticky="W")
check_viga=Checkbutton(mi_frame,text="Vigas",onvalue=1,offvalue=0)
check_viga.grid(row=3,column=0,sticky="W")
check_pilotin=Checkbutton(mi_frame,text="pilotines",onvalue=1,offvalue=0)
check_pilotin.grid(row=4,column=0,sticky="W")
check_contrapiso=Checkbutton(mi_frame,text="contrapiso",onvalue=1,offvalue=0)
check_contrapiso.grid(row=5,column=0,sticky="W")
#checkPAREDES--------------
check_lad_comun=Checkbutton(mi_frame,text="ladrillo comun ",onvalue=1,offvalue=0)
check_lad_comun.grid(row=2,column=1,sticky="W")
check_lad_bloque=Checkbutton(mi_frame,text="bloques",onvalue=1,offvalue=0)
check_lad_bloque.grid(row=3,column=1,sticky="W")
check_tabique=Checkbutton(mi_frame,text="tabiques",onvalue=1,offvalue=0)
check_tabique.grid(row=4,column=1,sticky="W")

#text field--------------------------
texto_detalle=Text(mi_frame,height=8)
texto_detalle.grid(row=6,column=0,padx=10,pady=10,columnspan=4)


raiz.mainloop()