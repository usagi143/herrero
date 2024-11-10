import sqlite3
from tkinter import messagebox

def crear_tablas():

    #la relacion de los empleados y autos deben ser distintas
    tabla_empleados = """ 
    CREATE TABLE IF NOT EXISTS empleado(
        dni INTEGER PRIMARY KEY NOT NULL,
        nombre TEXT NOT NULL,
        telefono INTEGER NOT NULL,
        puesto_del_empleado TEXT NOT NULL,
        
        FOREIGN KEY(dni) REFERENCES trabajos(dni_encargado)
    );
    """
    
    tabla_trabajos = """
    CREATE TABLE IF NOT EXISTS trabajos(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        cliente_id INTEGER NOT NULL,
        descripcion TEXT NOT NULL,
        costo_total FLOAT NOT NULL,
        estado TEXT NOT NULL,   
        dni_encargado INTEGER NOT NULL,
        piezas_id INTEGER NOT NULL,

        FOREIGN KEY (id) REFERENCES reportes(trabajo_id)
        FOREIGN KEY (piezas_id) REFERENCES piezas(pieza_id)
        FOREIGN KEY(cliente_id) REFERENCES clientes(cliente_id)
    );
    """

    tabla_clientes = """
    CREATE TABLE IF NOT EXISTS cliente(
        cliente_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT NOT NULL,
        telefono INTEGER NOT NULL,
        direccion TEXT NOT NULL,
        matricula_auto TEXT NOT NULL,
        activo INTEGER NOT NULL
    );
    """

    tabla_vehiculo =  """
    CREATE TABLE IF NOT EXISTS vehiculo(
        matricula TEXT PRIMARY KEY NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        color TEXT NOT NULL,
        poseedor INTEGER NOT NULL,

        FOREIGN KEY(poseedor) REFERENCES cliente(poseedor)   
    );
    """

    tabla_reportes = """
    CREATE TABLE IF NOT EXISTS reportes(
        id_reportes INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        cliente_id INTEGER NOT NULL,
        costo FLOAT NOT NULL,
        fecha DATE NOT NULL,
        descripcion TEXT,
        metodo_pago TEXT NOT NULL,
        trabajo_id INTEGER NOT NULL,

        FOREIGN KEY(trabajo_id) REFERENCES trabajos(id)
    );
    """

    tabla_pieza = """
    CREATE TABLE IF NOT EXISTS piezas(
        pieza_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        trabajo_id INTEGER,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        precio INTEGER NOT NULL,
        FOREIGN KEY (trabajo_id) REFERENCES trabajos(id)
    );
    """
    
    with sqlite3.connect("taller_base_datos.db") as conn:
        cursor = conn.cursor()

        cursor.execute(tabla_empleados)
        cursor.execute(tabla_trabajos)
        cursor.execute(tabla_clientes)
        cursor.execute(tabla_vehiculo)
        cursor.execute(tabla_reportes)
        cursor.execute(tabla_pieza)
        #cursor.execute("INSERT INTO cliente (nombre, telefono, direccion, matricula_auto) VALUES (?, ?, ?, ?)", ("Carlos López", 987654321, "Av. Siempre Viva 742", "XYZ987"))
        print("base de datos creada con exito")

def insertar_usuario(nombre, telefono, direccion, matricula_auto):
        try:
            with sqlite3.connect("taller_base_datos.db") as conn:
                cursor = conn.cursor()
                consulta = """
                INSERT INTO cliente (nombre, telefono, direccion, matricula_auto, activo)
                VALUES (?, ?, ?, ?, 1)
                """
                cursor.execute(consulta, (nombre, telefono, direccion, matricula_auto))
                conn.commit()
                messagebox.showinfo(title="Exito", message="Usuario agregado con exito")
        except sqlite3.Error:
            messagebox.showinfo(title="Error", message="Fallo al agregar el usuario")


def recojer_usuarios():
    usuarios = []
    try:
        with sqlite3.connect("taller_base_datos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT cliente_id, nombre, telefono, direccion, matricula_auto FROM cliente WHERE activo = 1")
            usuarios = cursor.fetchall()
    except sqlite3.Error as e:
        print("Error al obtener usuarios:", e)
    return usuarios

def borrar_usuario(id):
    if id is None or id == "":
        print("seleccione un cliente")
        return
    try:
        with sqlite3.connect("taller_base_datos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE cliente SET activo = 0 WHERE id=?", (id))
            usuarios = cursor.fetchall()
            print("borrado exitoso")
    except sqlite3.Error as e:
        print("Error al obtener usuarios:", e)
    return usuarios