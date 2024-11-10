import customtkinter as ctk
import sqlite3
from PIL import Image

def crear_frames_trabajos(menu, TrabajoMostrar, eleccion_frame):
    lugar = {"x":20, "y":4}

    for widget in menu.winfo_children():          
        widget.destroy()

    
    if eleccion_frame == 1:
        trabajos = Trabajos(menu)

        photo = ctk.CTkImage(Image.open("assets/trabajo_interfaz/angle-left.png"), size=(25, 25))
        cambiar_submenu = ctk.CTkButton(menu, image=photo,width=25, height=25 ,
                                        fg_color="transparent",text= "", hover_color="white" ,
                                        command=lambda:crear_frames_trabajos(menu, TrabajoMostrar, 0))
        cambiar_submenu.place(relx=0.02, rely=0.9)
        

    else: 
        mostrar_trabajo = TrabajoMostrar(menu, lugar)

        photo = ctk.CTkImage(Image.open("assets/trabajo_interfaz/angle-right.png"), size=(25, 25))
        cambiar_submenu = ctk.CTkButton(menu, image=photo,width=25, height=25 ,
                                        fg_color="transparent",text= "", hover_color="white" ,
                                        command=lambda:crear_frames_trabajos(menu, TrabajoMostrar, 1))
        cambiar_submenu.place(relx=0.95, rely=0.9)

        widgets_ingreso_trabajo(menu)
        crear_frame_trabajo_modificar(menu)


def widgets_ingreso_trabajo(menu):    
        frame_ingresar_vehiculo = ctk.CTkFrame(menu, width=550, height=280, fg_color="transparent", border_color="black", border_width=1)
        frame_ingresar_vehiculo.place(x=570, y=10)

        #----------------

        titulo_vehiculos = ctk.CTkLabel(frame_ingresar_vehiculo, text="Ingresar trabajo", font=("arial", 18))
        titulo_vehiculos.place(x=210, y=10)

        entry_vehiculo_matricula = ctk.CTkEntry(frame_ingresar_vehiculo, width=100, border_color="#000000", border_width=1, corner_radius=5, placeholder_text="Matrícula")
        entry_vehiculo_matricula.place(x=20, y=45)

        entry_vehiculo_poseedor = ctk.CTkButton(frame_ingresar_vehiculo, width=100, fg_color="white", border_width=1, 
                                                    text_color="black", border_color="#000000", corner_radius=5, hover_color="white", 
                                                    text="poseedor")
        entry_vehiculo_poseedor.place(x=140, y=45)

        entry_vehiculo_color = ctk.CTkEntry(frame_ingresar_vehiculo, width=110, border_color="#000000", border_width=1, corner_radius=5, placeholder_text="color")
        entry_vehiculo_color.place(x=260, y=45)

        entry_vehiculo_marca = ctk.CTkEntry(frame_ingresar_vehiculo, width=350, border_color="#000000", border_width=1, corner_radius=5, placeholder_text="marca")
        entry_vehiculo_marca.place(x=20, y=90)

        entry_vehiculo_modelo = ctk.CTkEntry(frame_ingresar_vehiculo, width=350, border_color="#000000", border_width=1, corner_radius=5, placeholder_text="modelo")
        entry_vehiculo_modelo.place(x=20, y=130)

        ##----------------

        entry_trabajo_descripcion = ctk.CTkTextbox(frame_ingresar_vehiculo, width=510, height=100, border_color="#000000", border_width=1, corner_radius=5, activate_scrollbars=False)
        entry_trabajo_descripcion.place(x=20, y=170)

        entry_trabajo_costo = ctk.CTkEntry(frame_ingresar_vehiculo, width=150, border_color="#000000", border_width=1, corner_radius=5, placeholder_text="Costo")
        entry_trabajo_costo.place(x=380, y=90)

        entry_trabajo_encargado = ctk.CTkEntry(frame_ingresar_vehiculo, width=150, border_color="#000000", border_width=1, corner_radius=5, placeholder_text="Encargado")
        entry_trabajo_encargado.place(x=380, y=45)

        entry_trabajo_pieza = ctk.CTkButton(frame_ingresar_vehiculo, width=150, fg_color="white", border_width=1, 
                                                    text_color="black", border_color="#000000", corner_radius=5, hover_color="white", 
                                                    text="pieza")
        entry_trabajo_pieza.place(x=380, y=130)

def crear_frame_trabajo_modificar(menu):
    frame = ctk.CTkFrame(menu, fg_color="transparent", border_width=1, border_color="black")
    frame.place(x=570, rely=0.60)

    estado_opciones = ["Pausado", "En proceso"]
    estado_combobox = ctk.CTkComboBox(frame, values=estado_opciones)
    estado_combobox.set("Pausado") 
    estado_combobox.grid(row=0, column=1, pady=10, padx=10)

    # Caja de texto para la descripción
    descripcion_textbox = ctk.CTkTextbox(frame, width=250, height=100, border_width=1, border_color="black")
    descripcion_textbox.grid(row=0, column=0, pady=10, padx=10, rowspan=2)

    # Función para guardar el estado y la descripción
    def guardar_informacion():
        estado = estado_combobox.get()
        descripcion = descripcion_textbox.get()
        print(f"Estado seleccionado: {estado}")
        print(f"Descripción: {descripcion}")

    # Botón para guardar cambios
    guardar_button = ctk.CTkButton(frame, text="Guardar Cambios", command=guardar_informacion)
    guardar_button.grid(row=1, column=1, pady=20)

class Trabajos:
    def __init__(self, menu):
        self.menu = menu

    #-------------Metodos para la creacion de los widgets-------------

    def widgets_cambiar_estado(self):
        pass


    def buscar_cliente(self):
        pass
