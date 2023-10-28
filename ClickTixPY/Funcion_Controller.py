
import sqlite3
from Sala_Controller import Sala_Controller

class Funcion_Controller:

  def __init__(self, conexion):
    self.conexion = conexion

  def crear_tabla_funcion(self):
    try:
      self.conexion.cursor.execute('''
              CREATE TABLE IF NOT EXISTS FUNCION (
              id INTEGER PRIMARY KEY,
              fecha DATE,
              id_dimension INTEGER,
              id_pelicula INTEGER,
              id_sala INTEGER,
              idioma_funcion TEXT,
              turno_id INTEGER,
              disponibilidad INTEGER,
              FOREIGN KEY (id_dimension) REFERENCES dimension(id),
              FOREIGN KEY (id_pelicula) REFERENCES pelicula(id),
              FOREIGN KEY (id_sala) REFERENCES sala(id),
              FOREIGN KEY (turno_id) REFERENCES turno(id)
            )
          ''')
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al crear la tabla de Funciones: {e}")
      return False

  def obtener_disponibilidad(self, id_funcion):

    self.conexion.cursor.execute(
        "SELECT disponibilidad FROM funcion WHERE id = ?", (id_funcion, ))
    disponibilidad_actual = self.conexion.cursor.fetchone()

    if disponibilidad_actual is not None:
      return int(disponibilidad_actual[0])
    else:
      return -1

  def restarDisponibilidad(self, id_funcion, cantidad_a_restar):
    try:
      self.conexion.cursor.execute(
          "SELECT disponibilidad FROM funcion WHERE id = ?", (id_funcion, ))
      disponibilidad_actual = self.conexion.cursor.fetchone()

      if disponibilidad_actual is not None:
        disponibilidad_actual = disponibilidad_actual[0]
        if disponibilidad_actual >= cantidad_a_restar:
          nueva_disponibilidad = disponibilidad_actual - cantidad_a_restar
          self.conexion.cursor.execute(
              "UPDATE funcion SET disponibilidad = ? WHERE id = ?",
              (nueva_disponibilidad, id_funcion))
          self.conexion.conexion.commit()

          return nueva_disponibilidad
        else:
          return "La disponibilidad actual no es suficiente para restar."
      else:
        return "Funcion no encontrada"
    except sqlite3.Error as e:
      print(f"Error al restar disponibilidad de la funcion: {e}")
      return None

  def mostrar_funciones(self):
    try:
      self.conexion.cursor.execute("SELECT * FROM funcion")
      dimensiones = self.conexion.cursor.fetchall()
      return dimensiones
    except sqlite3.Error as e:
      print(f"Error al mostrar funciones: {e}")
      return []

  def ingresar_funcion(self, fecha, idDimension, idPelicula, idSala, idIdioma,
                       idTurno):
    try:
      sala_instancia = Sala_Controller(self.conexion.conexion)
      self.conexion.cursor.execute(
          "INSERT INTO funcion (fecha,id_dimension,id_pelicula,id_sala,idioma_funcion,turno_id,disponibilidad) VALUES (?,?,?,?,?,?,?)",
          (fecha, idDimension, idPelicula, idSala, idIdioma, idTurno,
           sala_instancia.obtener_capacidad_por_id_sala(idSala)))
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al ingresar la funcion: {e}")
      return False

  def modificar_funcion(self, fecha, idDimension, idPelicula, idSala, idIdioma,
                        idTurno, id):
    try:
      self.conexion.cursor.execute(
          "UPDATE funcion SET fecha= ? ,id_dimension=?,id_pelicula=?,id_sala=?,idioma_funcion=?,turno_id WHERE id = ?",
          (fecha, idDimension, idPelicula, idSala, idIdioma, idTurno, id))
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al modificar la dimension: {e}")
      return False

  def eliminar_funcion(self, id):
    if not isinstance(id, int):
      return False
    try:
      self.conexion.cursor.execute("DELETE FROM funcion WHERE id = ?", (id, ))
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al eliminar la funcion: {e}")
      return False

  def mostrar_funcionesAB(self):
    try:
      self.conexion.cursor.execute("""
            SELECT f.id, f.fecha, p.nombre, s.numero, d.nombre, t.horario, f.disponibilidad
            FROM funcion f
            JOIN pelicula p ON f.id_pelicula = p.id
            JOIN sala s ON f.id_sala = s.id
            JOIN dimension d ON f.id_dimension = d.id
            JOIN turno t ON f.turno_id = t.id
        """)
      funcion_info = self.conexion.cursor.fetchall()
      return funcion_info
    except sqlite3.Error as e:
      print(f"Error al mostrar funciones: {e}")
      return []

  def mostrarFuncionPorId(self, funcion_id):
    try:
      self.conexion.cursor.execute(
          """
            SELECT f.id, f.fecha, p.nombre AS nombre_pelicula, s.numero AS numero_sala, 
                   d.nombre AS nombre_dimension, t.horario AS horario_turno
            FROM funcion f
            JOIN pelicula p ON f.id_pelicula = p.id
            JOIN sala s ON f.id_sala = s.id
            JOIN dimension d ON f.id_dimension = d.id
            JOIN turno t ON f.turno_id = t.id
            WHERE f.id = ?
        """, (funcion_id, ))
      funcion_info = self.conexion.cursor.fetchall()
      return funcion_info
    except sqlite3.Error as e:
      print(f"Error al mostrar la funcion: {e}")
      return None



def menu_funcion(self):
    opcion_dimension = 0
    while opcion_dimension != "4":
        opcion_dimension = input(
            "Menu funcion\n1- Ingresar Dimension\n2- Mostrar Dimensiones\n3- Modificar Dimension\n4- Volver al Menu Principal\n"
        )
        if opcion_dimension == "1":
            nombre = input("Ingrese nombre de la Dimension: ")
            precio = float(input("Ingrese precio de la Dimension: "))
            if self.ingresar_funcion(nombre, precio):
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

    




