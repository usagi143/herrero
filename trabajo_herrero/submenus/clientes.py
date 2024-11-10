#agregar cual es cliente que mas solicita trabajos

import customtkinter as ctk
import sqlite3
from PIL import Image

import sys
sys.path.append('..')
from creacion_base_datos import insertar_usuario, borrar_usuario

class Clientes:
    def __init__(self, menu, VerClientes):
        self.ver_clientes = VerClientes(menu, {"x":20, "y":20})
        self.menu = menu

        self.widgets_clientes_ingresar()
        self.widgets_clientes_modificar()
    #----------Crear widgets----------

    def widgets_clientes_ingresar(self):
        self.frame_ingresar_cliente = ctk.CTkFrame(self.menu, width=240, height=300, fg_color="white", border_width=1, border_color="black" )
        self.frame_ingresar_cliente.place(x=720, y= 190)

        titulo_ingresar_clientes = ctk.CTkLabel(self.frame_ingresar_cliente, text="Ingrese usuario", width=200,
                                                 font=("arial", 14), justify="center")
        titulo_ingresar_clientes.place(relx=0.1, rely= 0.03)

        nombre_entry = ctk.CTkEntry(self.frame_ingresar_cliente, width=200, placeholder_text="Nombre")
        nombre_entry.place(relx=0.1, rely=0.18)  

        telefono_entry = ctk.CTkEntry(self.frame_ingresar_cliente, width=200, placeholder_text="Telefono")
        telefono_entry.place(relx=0.1, rely=0.35) 

        direccion_entry = ctk.CTkEntry(self.frame_ingresar_cliente, width=200, placeholder_text="direccion")
        direccion_entry.place(relx=0.1, rely=0.52)  

        matricula_entry = ctk.CTkEntry(self.frame_ingresar_cliente, width=200, placeholder_text="Matricula")
        matricula_entry.place(relx=0.1, rely=0.69)  

        def enviar_datos():
            nombre = nombre_entry.get()
            telefono = telefono_entry.get()
            direccion = direccion_entry.get()
            matricula_auto = matricula_entry.get()

            insertar_usuario(nombre, telefono, direccion, matricula_auto)

            self.ver_clientes.crear_widgets_clientes(1)

        enviar_button = ctk.CTkButton(self.frame_ingresar_cliente, width=200, text="Guardar Cliente", command=enviar_datos)
        enviar_button.place(relx=0.1, rely=0.85) 
    
    def widgets_clientes_modificar(self):
        self.frame_modificador_cliente = ctk.CTkFrame(self.menu, width=240, height=150, fg_color="white", border_width=1, border_color="black")
        self.frame_modificador_cliente.place(x=720, y=20)

        label_titulo_modificar = ctk.CTkLabel(self.frame_modificador_cliente, text="Modificar usuario", width=200,
                                            font=("Arial", 14), justify="center")
        label_titulo_modificar.place(x=20, y=5)

        ingresar_nombre_nuevo = ctk.CTkEntry(self.frame_modificador_cliente, width=200, placeholder_text="Nombre")
        ingresar_nombre_nuevo.place(x=20, y=35)  

        ingresar_telefono_nuevo = ctk.CTkEntry(self.frame_modificador_cliente, width=200, placeholder_text="Telefono")
        ingresar_telefono_nuevo.place(x=20, y=70) 

        def enviar_datos():
            nombre = ingresar_nombre_nuevo.get()
            telefono = ingresar_telefono_nuevo.get()
            print(f"Datos enviados: Nombre: {nombre}, Teléfono: {telefono}")

        modificar_boton = ctk.CTkButton(self.frame_modificador_cliente, width=200, text="Guardar Cliente", command=enviar_datos)
        modificar_boton.place(x=20, y=105) 
    
    #----------Funcionalidades----------