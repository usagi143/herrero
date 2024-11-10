import customtkinter as ctk

class Salidas:
    def __init__(self, menu, VerTrabajo):
        self.menu = menu
        self.place= {"relx":0.45, "y":10}

        ver_trabajo = VerTrabajo(self.menu, self.place)
        self.widgets_infromacion_salida()

        #agregar boton de finalizar trabajo

    def widgets_infromacion_salida(self):
        salida_frame_informacion =  ctk.CTkFrame(self.menu, width=400, height=450, border_width=1, border_color="black")
        salida_frame_informacion.place( relx=0.10, y=10)

        #agregar label de informacion total de instrumentos
        #agregar label de valor venta
        #agregar label de cuanto se gano por esa venta
        #agregar cuantos trabajos a hecho el ancargado de el trabajo