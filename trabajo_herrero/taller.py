import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk
import tkinter as tk

from creacion_base_datos import crear_tablas, recojer_usuarios, borrar_usuario

#submenus
from submenus.dashboard import Dashboard
from submenus.clientes import Clientes
from submenus.trabajos import crear_frames_trabajos
from submenus.salida import Salidas

#https://www.flaticon.com/uicons/interface-icons
 
#---------Creacion frame para clientes---------

#id, nombre, telefono, direccion, matricula
import customtkinter as ctk
from PIL import Image
import sqlite3
import tkinter.ttk as ttk

import customtkinter as ctk
from PIL import Image
import sqlite3
import tkinter.ttk as ttk

class ClientesMostrar:
    def __init__(self, menu, lugar_place):
        self.seleccion = ""
        self.menu = menu
        self.lugar_place = lugar_place

        self.contenedor = ctk.CTkFrame(self.menu, width=420, height=500, fg_color="transparent") 
        self.contenedor.place(**self.lugar_place)

        self.widgets_clientes_eliminar()
        self.crear_widgets_clientes(1)

    def crear_widgets_clientes(self, eleccion):
        if eleccion == 1:
            self.usuarios = self.buscar_cliente()
        columnas = ["Id", "Nombre", "Telefono", "Direccion", "Matricula"]

        style = ttk.Style(self.contenedor)
        style.configure("Custom.Treeview",
                        background="#670010",  
                        foreground="#FFFFFF",  
                        rowheight=35,          
                        font=("Proxima Soft", 11)) 
        style.map("Custom.Treeview", background=[('selected', '#FF3936')])  

        style.configure("Custom.Treeview.Heading",
                        background="#FF7673", 
                        foreground="#000000",  
                        font=("Proxima Soft", 12, 'bold'))

        treeview = ttk.Treeview(self.contenedor, columns=columnas, show="headings", style="Custom.Treeview")
        treeview.grid(row=0, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

        column_widths = {"Id": 70, "Nombre": 150, "Telefono": 130, "Direccion": 180, "Matricula": 130}
        for col in columnas:
            treeview.heading(col, text=col)
            treeview.column(col, width=column_widths[col], anchor="center", stretch=False)
        
        for value in self.usuarios:
            treeview.insert("", "end", values=value)

        for row in treeview.get_children():
            index = treeview.index(row)
            tag = "even_row" if index % 2 == 0 else "odd_row"
            color = "#670010" if tag == "even_row" else "#4A0010"
            treeview.tag_configure(tag, background=color)
            treeview.item(row, tags=tag)

        def seleccionar_fila():
            selected_item = treeview.selection()
            if selected_item:
                item_values = treeview.item(selected_item, "values")
                self.seleccion = item_values[1]

        button = ctk.CTkButton(self.contenedor, text="Seleccionar trabajo", fg_color='white', 
                            text_color="black", border_width=1, border_color="black",hover_color="white",
                            font=("Proxima Soft", 18), command=seleccionar_fila)
        button.grid(row=1, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

    def actualizar_seleccion(self, id):
        self.seleccion = id

    def buscar_cliente(self, nombre=""):
        try:
            with sqlite3.connect("taller_base_datos.db") as conn:
                cursor = conn.cursor()
                query = "SELECT cliente_id, nombre, telefono, direccion, matricula_auto FROM cliente"
                if nombre:
                    query += " WHERE nombre LIKE ?"
                    cursor.execute(query, (f"%{nombre}%",))
                else:
                    cursor.execute(query)
                usuarios = cursor.fetchall()
        except sqlite3.Error as e:
            usuarios = []
        return usuarios

    def realizar_busqueda(self):
        nombre_buscado = self.buscador.get()
        self.usuarios = self.buscar_cliente(nombre=nombre_buscado)
        self.crear_widgets_clientes(0)

    def widgets_clientes_eliminar(self):        
        # Botón de borrar pequeño
        photo_trash = ctk.CTkImage(Image.open("assets/interfaz/trash.png"), size=(20, 20))
        borrar = ctk.CTkButton(self.contenedor, image=photo_trash, text="", width=28, height=28, 
                               fg_color="white", hover_color="white", 
                               command=lambda: borrar_usuario(self.seleccion))
        borrar.grid(row=2, column=6, padx=(2, 5), pady=5, sticky="e")

        # Campo de entrada de búsqueda grande, ocupando aproximadamente 75% del espacio
        self.buscador = ctk.CTkEntry(self.contenedor, width=565, corner_radius=5, 
                                     border_width=1, border_color="black", 
                                     placeholder_text="Buscar por Nombre")
        self.buscador.grid(row=2, column=0, columnspan=4, pady=5)

        # Botón de imagen de búsqueda pequeño
        photo_search = ctk.CTkImage(Image.open("assets/interfaz/search.png"), size=(20, 20))
        image_buscador = ctk.CTkButton(self.contenedor, image=photo_search, text="", 
                                       width=28, height=28, fg_color="white", 
                                       hover_color="white", command=self.realizar_busqueda)
        image_buscador.grid(row=2, column=4, pady=5 )


#---------Clase mostrar trabajo---------

class TrabajoMostrar:
    def __init__(self, menu, lugar_place):
        self.menu = menu
        self.values = self.recoger_informacion_trabajo()
        self.frame_trabajos = ctk.CTkFrame(self.menu, width=420, height=450, fg_color="transparent") 
        self.frame_trabajos.place(**lugar_place)

        self.crear_treeview_trabajos()

    def recoger_informacion_trabajo(self):
        try:
            with sqlite3.connect("taller_base_datos.db") as conn:
                cursor = conn.cursor()
                query = "SELECT id, cliente_id, costo_total, estado, dni_encargado FROM cliente"
                cursor.execute(query)
                trabajos = cursor.fetchall()
        except sqlite3.Error as e:
            trabajos = []
        return trabajos
    
    def crear_treeview_trabajos(self):
        columnas = ["Id", "Cliente", "Costo total", "Estado", "Encargado"]

        style = ttk.Style(self.frame_trabajos)
        style.configure("Custom.Treeview",
                        background="#670010",  
                        foreground="#FFFFFF",  
                        rowheight=35,          
                        font=("Proxima Soft", 11)) 
        style.map("Custom.Treeview", 
                background=[('selected', '#FF3936')])  

        style.configure("Custom.Treeview.Heading",
                        background="#FF7673", 
                        foreground="#000000",  
                        font=("Proxima Soft", 12, 'bold'))

        treeview = ttk.Treeview(self.frame_trabajos, columns=columnas, show="headings", style="Custom.Treeview")
        treeview.grid(row=0, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

        # Ajustar el ancho de las columnas

        column_widths = {"Id": 70, "Cliente": 120, "Costo total": 100, "Estado": 100, "Encargado": 130}
        for col in columnas:
            treeview.heading(col, text=col)
            treeview.column(col, width=column_widths[col], anchor="center", stretch=False)

        for value in self.values:
            treeview.insert("", "end", values=value)

        # Estilo para las filas alternadas (aplicando colores de fondo)
        for row in treeview.get_children():
            index = treeview.index(row)  # Obtener el índice de la fila
            if index % 2 == 0:  # Si el índice es par
                treeview.tag_configure(f"even_row", background="#670010")  # Rojo oscuro
            else:  # Si el índice es impar
                treeview.tag_configure(f"odd_row", background="#4A0010")  
                treeview.item(row, tags="odd_row")

        # Agregar un botón para seleccionar una fila
        def seleccionar_fila():
            selected_item = treeview.selection()
            if selected_item:
                item_values = treeview.item(selected_item, "values")

                # actualizar_seleccion(item_values[1])  # Por ejemplo, usando el "nombre" como parámetro
        button = ctk.CTkButton(self.frame_trabajos, text="Seleccionar trabajo", fg_color=("lightblue"), 
                                        text_color=("#000000","#FFFFFF"), hover_color=("#FF3936","#4A0010"), 
                                        font=("Proxima Soft", 18), command=seleccionar_fila)
        button.grid(row=1, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

class CrearMostrarPieza:
    def __init__(self):
        pass    

#----------------Programa principal----------------
    
class Taller(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Taller chapa y pintura")
        self.geometry("1200x600")
        
        x = (self.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.winfo_screenheight() // 2) - (600 // 2)
        self.geometry(f"1200x600+{x}+{y}")
        self.resizable(False, False)
        self.configure(fg_color="white") 

        self.frame_principal()
        self.frame_submenu()
        self.cambiar_submenu("Salidas")

    def frame_principal(self):
        self.contenedor_principal = ctk.CTkFrame(self, width=1150, height=500, fg_color="white", border_width= 1)
        self.contenedor_principal.place(x=25, y = 75)
        
    def frame_submenu(self):
        diseños_botones = {"fg_color":"white", "text_color":"black",  "border_color":"black", "width":100, "height":30, "hover_color":"white", "font":("arial", 20)} 
        posicion_y = 0.25

        self.contenedor_submenu = ctk.CTkFrame(self, width=1200, height= 50,  border_color="black",corner_radius=0, border_width= 1, fg_color="white")
        self.contenedor_submenu.place(x=0, y=0)

        photo = ctk.CTkImage(Image.open("assets/interfaz/search.png"), size=(25, 25))

        self.boton_submenu_dashboard =  ctk.CTkButton(self.contenedor_submenu, text="Dashboard",command=lambda : self.cambiar_submenu("Dashboard"), **diseños_botones)
        self.boton_submenu_dashboard.place(relx=0.2, rely=posicion_y)

        self.boton_submenu_cliente = ctk.CTkButton(self.contenedor_submenu, text="Cliente", command=lambda : self.cambiar_submenu("Cliente"), **diseños_botones)
        self.boton_submenu_cliente.place(relx=0.35, rely=posicion_y)

        self.boton_submenu_trabajo = ctk.CTkButton(self.contenedor_submenu, text="Trabajos", command=lambda : self.cambiar_submenu("Trabajos"), **diseños_botones)
        self.boton_submenu_trabajo.place(relx=0.50, rely=posicion_y)


        self.boton_submenu_inventario = ctk.CTkButton(self.contenedor_submenu, text="Salidas", command=lambda : self.cambiar_submenu("Salidas"), **diseños_botones)
        self.boton_submenu_inventario.place(relx=0.65, rely=posicion_y)


        photo = ctk.CTkImage(Image.open("assets/interfaz/menu-burger.png"), size=(25, 25))
        self.boton_submenu_configuracion = ctk.CTkButton(self.contenedor_submenu, 
                                        text="", image = photo, command=self.configuraciones,
                                        **diseños_botones)
        self.boton_submenu_configuracion.place(relx = 0.91, rely=posicion_y-0.03)

    def cambiar_submenu(self, eleccion):
        
        for widget in self.contenedor_principal.winfo_children():          
            widget.destroy()

        # self.contenedor_principal.configure(border_width=0, ) if eleccion == "Dashboard" else self.contenedor_principal.configure(border_width=1)    
        self.contenedor_principal.configure(border_width=0)
        if eleccion == "Dashboard":
            dashboard = Dashboard(self.contenedor_principal)

        if eleccion ==  "Cliente":
            clientes = Clientes(self.contenedor_principal, ClientesMostrar)
           
        if eleccion == "Trabajos":
            # trabajos = Trabajos(self.contenedor_principal)
            crear_frames_trabajos(self.contenedor_principal, TrabajoMostrar, 0)

        if eleccion == "Salidas":
            salidas = Salidas(self.contenedor_principal, TrabajoMostrar)
 
    def configuraciones(self):
        # Definimos los estilos para botones y etiquetas
        estilos_botones = {"fg_color": "white", "text_color": "black", "border_width": 1,
                        "border_color": "black", "width": 200, "height": 40, "hover_color": "#f0f0f0",
                        "font": ("Arial", 16, "bold")}
        estilos_labels = {"fg_color": "transparent", "text_color": "black", "font": ("Arial", 18)}

        # Contenedor principal de configuraciones
        self.contenedor_configuraciones = ctk.CTkFrame(self, width=350, height=500, fg_color="#f8f8f8", border_width=2)
        self.contenedor_configuraciones.place(x=850, y=15)

        # Ícono del usuario y etiqueta de administrador
        photo_user = ctk.CTkImage(Image.open("assets/interfaz/user.png"), size=(30, 30))
        image_usuario = ctk.CTkLabel(self.contenedor_configuraciones, image=photo_user, text="", width=30, height=30, fg_color="#f8f8f8")
        image_usuario.place(relx=0.05, rely=0.1)

        persona_administradora = ctk.CTkLabel(self.contenedor_configuraciones, text="Administrador", **estilos_labels)
        persona_administradora.place(relx=0.2, rely=0.1)

        # Botón para cerrar el panel de configuraciones (ícono de cruz)
        photo_close = ctk.CTkImage(Image.open("assets/interfaz/cross.png"), size=(20, 20))
        self.cerrar_configuracion = ctk.CTkButton(self.contenedor_configuraciones, fg_color="transparent", width=25, height=25,
                                                text="", image=photo_close, hover_color="#f8f8f8",
                                                command=self.contenedor_configuraciones.destroy)
        self.cerrar_configuracion.place(relx=0.85, rely=0.05)

        # Espacio entre el título y los botones
        espacio = 0.3

        # Botón para reiniciar la base de datos
        self.reiniciar_base_datos = ctk.CTkButton(self.contenedor_configuraciones, text="Reiniciar base de datos",
                                                **estilos_botones)
        self.reiniciar_base_datos.place(relx=0.15, rely=espacio)

        # Botón para exportar la base de datos
        self.boton_exportar = ctk.CTkButton(self.contenedor_configuraciones, text="Exportar base de datos",
                                            **estilos_botones)
        self.boton_exportar.place(relx=0.15, rely=espacio + 0.2)

        # Botón para cerrar la aplicación
        self.cerrar_aplicacion = ctk.CTkButton(self.contenedor_configuraciones, text="Cerrar aplicación", **estilos_botones,
                                            command=self.destroy)
        self.cerrar_aplicacion.place(relx=0.15, rely=espacio + 0.4)

        # Espacio de información en la parte inferior
        info_label = ctk.CTkLabel(self.contenedor_configuraciones, text="Configuraciones de la aplicación",
                                **estilos_labels, font=("Arial", 12, "italic"))
        info_label.place(relx=0.15, rely=0.85)

        


crear_tablas()

taller = Taller()
taller.mainloop()

