import sqlite3


class Pelicula_Controller:

    def __init__(self, conexion):
        self.conexion = conexion

    def crear_tabla_pelicula(self):
        try:
            self.conexion.cursor.execute('''
                CREATE TABLE IF NOT EXISTS PELICULA(
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    descripcion TEXT,
                    idioma TEXT,
                    duracion INT,
                    fecha_estreno TEXT,
                    precio REAL,
                    categoria TEXT
                )
            ''')
            self.conexion.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al crear la tabla de Peliculas: {e}")
            return False

    def mostrar_peliculas(self):
        try:
            self.conexion.cursor.execute("SELECT * FROM PELICULA")
            peliculas = self.conexion.cursor.fetchall()
            return peliculas
        except sqlite3.Error as e:
            print(f"Error al mostrar peliculas: {e}")
            return []

    def mostrarNombrePelicula(self, id):
        try:
            self.conexion.cursor.execute("SELECT nombre FROM PELICULA where id=?", (id,))
            peliculas = self.conexion.cursor.fetchall()
            return peliculas
        except sqlite3.Error as e:
            print(f"Error al mostrar el nombre de las peliculas: {e}")
            return []

    def ingresar_pelicula(self, nombre, descripcion, idioma, duracion,
                          fecha_estreno, precio, categoria):
        if not (isinstance(nombre, str) and isinstance(descripcion, str)
                and isinstance(idioma, str) and isinstance(duracion, int)
                and isinstance(fecha_estreno, str) and isinstance(precio, float)
                and isinstance(categoria, str)):
            return False

        try:
            self.conexion.cursor.execute(
                "INSERT INTO PELICULA (nombre, descripcion, idioma, duracion, fecha_estreno, precio, categoria) VALUES (?,?,?,?,?,?,?)",
                (nombre, descripcion, idioma, duracion, fecha_estreno, precio,
                 categoria))
            self.conexion.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al ingresar la pelicula: {e}")
            return False

    def filtrar_peliculas_por_categoria(self, categoria):
        try:
            self.conexion.cursor.execute(
                "SELECT * FROM PELICULA WHERE categoria = ?", (categoria,))
            peliculas = self.conexion.cursor.fetchall()
            return peliculas
        except sqlite3.Error as e:
            print(f"Error al filtrar peliculas por categoria: {e}")
            return []

    def modificar_pelicula(self, id, nombre, descripcion, idioma, duracion,
                           fecha_estreno, precio, categoria):
        if not (isinstance(nombre, str) and isinstance(descripcion, str)
                and isinstance(idioma, str) and isinstance(duracion, int)
                and isinstance(fecha_estreno, str) and isinstance(precio, float)
                and isinstance(categoria, str)):
            return False
        try:
            self.conexion.cursor.execute(
                "UPDATE PELICULA SET nombre=?, descripcion=?, idioma=?, duracion=?, fecha_estreno=?, precio=?, categoria=? WHERE id = ?",
                (nombre, descripcion, idioma, duracion, fecha_estreno, precio,
                 categoria, id))
            self.conexion.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al modificar la pelicula: {e}")
            return False

    def eliminar_pelicula(self, id):
        if not isinstance(id, int):
            return False

        try:
            self.conexion.cursor.execute("DELETE FROM PELICULA WHERE id = ?", (id,))
            self.conexion.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al eliminar la pelicula: {e}")
            return False

    def menu_pelicula(self):
        opcion_pelicula = 0

        while opcion_pelicula != "6":
            opcion_pelicula = input(
                "Menu Pelicula\n1- Ingresar Pelicula\n2- Mostrar Pelicula\n3- Modificar Pelicula\n4- Eliminar Pelicula\n5- Filtrar por categoria\n6- Volver al Menu Principal: "
            )

            if opcion_pelicula == "1":
                nombre = input("Ingrese nombre de la Pelicula: ")
                descripcion = input("Ingrese la descripcion de la Pelicula: ")
                idioma = input("Ingrese el idioma de la Pelicula: ")
                duracion = int(input("Ingrese la duracion de la Pelicula: "))
                fecha_estreno = input("Ingrese la fecha de estreno de la Pelicula: ")
                precio = float(input("Ingrese precio de la Pelicula: "))
                categoria = input("Ingrese la categoria: ")
                if self.ingresar_pelicula(nombre, descripcion, idioma, duracion,
                                          fecha_estreno, precio, categoria):
                    print("Pelicula ingresada con exito.")
                else:
                    print("Error al ingresar la pelicula.")
            elif opcion_pelicula == "2":
                peliculas = self.mostrar_peliculas()
                if peliculas:
                    for pelicula in peliculas:
                        print(
                            f"Nombre: {pelicula[1]}, Descripcion: {pelicula[2]}, Idioma: {pelicula[3]}, Duracion: {pelicula[4]}, Fecha de Estreno: {pelicula[5]}, Precio: {pelicula[6]}, Categoria: {pelicula[7]}, ID: {pelicula[0]}"
                        )
                else:
                    print("No hay peliculas registradas.")
            elif opcion_pelicula == "3":
                id_pelicula = input("Ingrese ID de la pelicula a modificar: ")
                nombre = input("Ingrese nuevo nombre: ")
                descripcion = input("Ingrese nueva descripcion: ")
                idioma = input("Ingrese nuevo idioma: ")
                duracion = int(input("Ingrese nueva duracion: "))
                fecha_estreno = input("Ingrese nueva fecha de estreno: ")
                categoria = input("Ingrese la categoria: ")
                precio = float(input("Ingrese nuevo precio: "))
                if self.modificar_pelicula(id_pelicula, nombre, descripcion, idioma,
                                       duracion, fecha_estreno, precio, categoria):
                    print("Pelicula modificada con exito.")
                else:
                    print("Error al modificar la pelicula.")
            elif opcion_pelicula == "4":
                id_pelicula = input("Ingrese ID de la pelicula a eliminar: ")
                if self.eliminar_pelicula(id_pelicula):
                    print("Pelicula eliminada con exito.")
                else:
                    print("Error al eliminar la pelicula.")
            elif opcion_pelicula == "5":
                categoria_filtrada = input("Ingrese la categoria a filtrar: ")
                peliculas_filtradas = self.filtrar_peliculas_por_categoria(
                    categoria_filtrada)
                if peliculas_filtradas:
                    print("Peliculas en la categoria seleccionada:")
                    for pelicula in peliculas_filtradas:
                        print(
                            f"Nombre: {pelicula[1]}, Descripcion: {pelicula[2]}, Idioma: {pelicula[3]}, Duracion: {pelicula[4]}, Fecha de Estreno: {pelicula[5]}, Precio: {pelicula[6]}, ID: {pelicula[0]}"
                        )
                else:
                    print("No se encontraron peliculas en la categoria especificada.")
            elif opcion_pelicula == "6":
                print("Volviendo al Menu Principal.")
            else:
                print("Opcion no valida. Intentalo de nuevo.")
