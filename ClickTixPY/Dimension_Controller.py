import sqlite3

class Dimension_Controller:

  def __init__(self, conexion):
    self.conexion = conexion

  def crear_tabla_dimension(self):
    try:
      self.conexion.cursor.execute('''
              CREATE TABLE IF NOT EXISTS DIMENSION(
                  id INTEGER PRIMARY KEY,
                  nombre TEXT,
                  precio REAL
              )
          ''')
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al crear la tabla de Dimensiones: {e}")
      return False

  def mostrar_dimensiones(self):
    try:
      self.conexion.cursor.execute("SELECT * FROM DIMENSION")
      dimensiones = self.conexion.cursor.fetchall()
      return dimensiones
    except sqlite3.Error as e:
      print(f"Error al mostrar dimensiones: {e}")
      return []

  def mostrarNombreDimension(self, id):
    try:
      self.conexion.cursor.execute("SELECT NOMBRE FROM DIMENSION WHERE id=?",
                                   (id, ))
      dimension = self.conexion.cursor.fetchone()
      return dimension
    except sqlite3.Error as e:
      print(f"Error al traer horario turnos: {e}")
      return ''

  def ingresar_dimension(self, nombre, precio):
    try:
      self.conexion.cursor.execute(
          "INSERT INTO DIMENSION (nombre, precio) VALUES (?, ?)",
          (nombre, precio))
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al ingresar la dimension: {e}")
      return False

  def modificar_dimension(self, id, nombre, precio):
    if not (isinstance(nombre, str) and isinstance(precio, float)
            and isinstance(id, int)):
      return False
    try:
      self.conexion.cursor.execute(
          "UPDATE DIMENSION SET nombre=?, precio=? WHERE id = ?",
          (nombre, precio, id))
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al modificar la dimension: {e}")
      return False

  def eliminar_dimension(self, id):
    if not isinstance(id, int):
      return False
    try:
      self.conexion.cursor.execute("DELETE FROM DIMENSION WHERE id = ?",
                                   (id, ))
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al eliminar la dimension: {e}")
      return False

  def menu_dimension(self):
    opcion_dimension = 0
    while opcion_dimension != "4":
      opcion_dimension = input(
          "Menu Dimension\n1- Ingresar Dimension\n2- Mostrar Dimensiones\n3- Modificar Dimension\n4- Volver al Menu Principal\n"
      )
      if opcion_dimension == "1":
        nombre = input("Ingrese nombre de la Dimension: ")
        precio = float(input("Ingrese precio de la Dimension: "))
        if self.ingresar_dimension(nombre, precio):
          print("Dimension ingresada con exito.")
        else:
          print("Error al ingresar la dimension.")
      elif opcion_dimension == "2":
        dimensiones = self.mostrar_dimensiones()
        if dimensiones:
          for dimension in dimensiones:
            print(
                f"Nombre: {dimension[1]}, Precio: {dimension[2]}, ID: {dimension[0]}"
            )
        else:
          print("No hay dimensiones registradas.")
      elif opcion_dimension == "3":
        id_dimension = input("Ingrese ID de la dimension a modificar: ")
        nombre = input("Ingrese nuevo nombre: ")
        precio = float(input("Ingrese nuevo precio: "))
        if self.modificar_dimension(id_dimension, nombre, precio):
          print("Dimension modificada con exito.")
        else:
          print("Error al modificar la dimension.")
      elif opcion_dimension == "4":
        print("Volviendo al Menu Principal.")
      else:
        print("Opcion no valida. Intentalo de nuevo.")
