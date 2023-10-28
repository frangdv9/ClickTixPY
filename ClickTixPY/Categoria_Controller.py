import sqlite3

class Categoria_Controller:
    def __init__(self, conexion):
        self.conexion = conexion

    def crear_tabla_categoria(self):
        try:
            self.conexion.cursor.execute('''
                CREATE TABLE IF NOT EXISTS CATEGORIA(
                    id INTEGER PRIMARY KEY,
                    nombre TEXT
                )
            ''')
            self.conexion.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al crear la tabla de Categorias: {e}")
            return False

    def mostrar_categorias(self):
        try:
            self.conexion.cursor.execute("SELECT * FROM CATEGORIA")
            categorias = self.conexion.cursor.fetchall()
            return categorias
        except sqlite3.Error as e:
            print(f"Error al mostrar categorias: {e}")
            return []

    def ingresar_categoria(self, nombre):
        if not isinstance(nombre, str):
            return False
        try:
            self.conexion.cursor.execute("INSERT INTO CATEGORIA (nombre) VALUES (?)",
                                         (nombre, ))
            self.conexion.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al ingresar la categoria: {e}")
            return False

    def modificar_categoria(self, id, nombre):
        if not (isinstance(nombre, str) and isinstance(id, int)):
            return False
        try:
            self.conexion.cursor.execute(
                "UPDATE CATEGORIA SET nombre=? WHERE id = ?", (nombre, id))
            self.conexion.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al modificar la categoria: {e}")
            return False

    def eliminar_categoria(self, id):
        if not isinstance(id, int):
            return False
        try:
            self.conexion.cursor.execute("DELETE FROM CATEGORIA WHERE id = ?",
                                         (id, ))
            self.conexion.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al eliminar la categoria: {e}")
            return False

    def menu_categoria(self):
        opcion_categoria = 0
        while opcion_categoria != "6":
            opcion_categoria = input(
                "Menu Categoria\n1- Ingresar Categoria\n2- Mostrar Categorias\n3- Modificar Categoria\n4- Eliminar Categoria\n5- Volver al Menu Principal: "
            )
            if opcion_categoria == "1":
                nombre = input("Ingrese nombre de la Categoria: ")
                if self.ingresar_categoria(nombre):
                    print("Categoria ingresada con exito.")
                else:
                    print("Error al ingresar la categoria.")
            elif opcion_categoria == "2":
                categorias = self.mostrar_categorias()
                if categorias:
                    for categoria in categorias:
                        print(f"Nombre: {categoria[1]}, ID: {categoria[0]}")
                else:
                    print("No hay categorias registradas.")
            elif opcion_categoria == "3":
                id_categoria = input("Ingrese ID de la categoria a modificar: ")
                nombre = input("Ingrese nuevo nombre: ")
                if self.modificar_categoria(id_categoria, nombre):
                    print("Categoria modificada con exito.")
                else:
                    print("Error al modificar la categoria.")
            elif opcion_categoria == "4":
                id_categoria = input("Ingrese ID de la categoria a eliminar: ")
                if self.eliminar_categoria(id_categoria):
                    print("Categoria eliminada con exito.")
                else:
                    print("Error al eliminar la categoria.")
            elif opcion_categoria == "5":
                print("Volviendo al Menu Principal.")
            else:
                print("Opcion no valida. Intantalo de nuevo.")
