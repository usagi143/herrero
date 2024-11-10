## Puedes crear un frame el cual se muestren el estado de los trabajos
## servicios realizadas
## Cantidad de reporte
## como la metodos de paga 

import customtkinter as ctk
from PIL import Image, ImageTk

class Dashboard:
    def __init__(self, menu):
        self.menu = menu
        
        self.creacion_informacion_trabajo()
        self.creacion_informacion_ventas()

    def creacion_informacion_trabajo(self):
        #--------------trabajo-------------

        self.frame_informacion_trabajo = ctk.CTkFrame(self.menu, width=250, height=200, fg_color="transparent", border_width=1, border_color="black")
        self.frame_informacion_trabajo.place(x=0, y=0)

        self.label_informacion_trabajos = ctk.CTkLabel(self.frame_informacion_trabajo, text="Trabajos", font=("arial", 18), text_color="black", fg_color="transparent")
        self.label_informacion_trabajos.place(relx=0.10, rely= 0.02)

        self.label_informacion_terminado = ctk.CTkLabel(self.frame_informacion_trabajo, text="terminados n", font=("arial", 13), text_color="black", fg_color="transparent")
        self.label_informacion_terminado.place(relx=0.10, rely= 0.25)

        self.label_informacion_proceso = ctk.CTkLabel(self.frame_informacion_trabajo, text="En proceso n", font=("arial", 13), text_color="black", fg_color="transparent")
        self.label_informacion_proceso.place(relx=0.10, rely= 0.5)

        self.label_informacion_empezar = ctk.CTkLabel(self.frame_informacion_trabajo, text="A empezar n", font=("arial", 13), text_color="black", fg_color="transparent")
        self.label_informacion_empezar.place(relx=0.10, rely= 0.75)

        # def on_hover(event):
        #     self.frame_informacion_trabajo.configure(fg_color="lightblue")

        # def on_leave(event):
        #     self.frame_informacion_trabajo.configure(fg_color="transparent")

        # self.frame_informacion_trabajo.bind("<Enter>", on_hover)
        # self.frame_informacion_trabajo.bind("<Leave>", on_leave)
        

        #--------------clientes--------------

        self.frame_informacion_clientes = ctk.CTkFrame(self.menu, width=200, height=90, fg_color="transparent", border_width=1, border_color="black")
        self.frame_informacion_clientes.place(x=270, y=0)

        photo = ctk.CTkImage(Image.open("assets/interfaz/user.png"), size=(40, 40))
        image_label = ctk.CTkLabel(self.frame_informacion_clientes, image=photo, text="")
        image_label.place(relx=0.05, rely=0.25)

        self.label_informacion_cantidad_titulo = ctk.CTkLabel(self.frame_informacion_clientes, text="Cantidad clientes", font=("arial", 18), text_color="black", fg_color="transparent" )
        self.label_informacion_cantidad_titulo.place(relx= 0.25, rely=0.20)

        self.label_informacion_cantidad = ctk.CTkLabel(self.frame_informacion_clientes, text="n", font=("arial",14), text_color="black", fg_color="transparent" )
        self.label_informacion_cantidad.place(relx= 0.30, rely=0.48)
    
    def creacion_informacion_ventas(self):
        self.frame_ventas = ctk.CTkFrame(self.menu, width=200, height=90, 
                                         fg_color="transparent", border_width=1, border_color="black")
        self.frame_ventas.place(x=270, y=110)

    def creacion_informacion_reportes():
        pass

    