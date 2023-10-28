import sqlite3

class Sala_Controller:

  def __init__(self, conexion):
    self.conexion = conexion

  def crear_tabla_sala(self):
    try:
      self.conexion.cursor.execute('''
              CREATE TABLE IF NOT EXISTS SALA(
                  id INTEGER PRIMARY KEY,
                  numero INTEGER,
                  fila INTEGER,
                  columnas INTEGER,
                  capacidad INTEGER
              )
          ''')

      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al crear la tabla de Salas: {e}")
      return False

  def mostrar_salas(self):
    try:
      self.conexion.cursor.execute("SELECT * FROM SALA")
      salas = self.conexion.cursor.fetchall()
      return salas
    except sqlite3.Error as e:
      print(f"Error al mostrar salas: {e}")
      return []

  def ingresar_sala(self, numero, fila, columnas, capacidad):
    if not (isinstance(numero, int) and isinstance(fila, int)
            and isinstance(columnas, int) and isinstance(capacidad, int)):
      return False

    try:
      self.conexion.cursor.execute(
          "INSERT INTO SALA (numero, fila, columnas, capacidad) VALUES (?, ?, ?, ?)",
          (numero, fila, columnas, capacidad))
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al ingresar la sala: {e}")
      return False

  def modificar_sala(self, id, numero, fila, columnas, capacidad):
    if not (isinstance(id, int) and isinstance(numero, int)
            and isinstance(fila, int) and isinstance(columnas, int)
            and isinstance(capacidad, int)):
      return False

    try:
      self.conexion.cursor.execute(
          "UPDATE SALA SET numero=?, fila=?, columnas=?, capacidad=? WHERE id=?",
          (numero, fila, columnas, capacidad, id))
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al modificar la sala: {e}")
      return False

  def eliminarSala(self, id_sala):
    try:
      self.conexion.cursor.execute("DELETE FROM SALA WHERE id = ?",
                                   (id_sala, ))
      self.conexion.conexion.commit()
      return True
    except sqlite3.Error as e:
      print(f"Error al eliminar la sala: {e}")
      return False

  def traerNumeroSalaPorId(self, id_sala):
    try:
      self.conexion.cursor.execute("SELECT numero FROM sala WHERE id = ?",
                                   (id_sala, ))
      numero_sala = self.conexion.cursor.fetchone()
      return numero_sala[0] if numero_sala else "Sala no encontrada"
    except sqlite3.Error as e:
      print(f"Error al obtener el numero de sala: {e}")
      return None

  def obtener_capacidad_por_id_sala(self, id_sala):
    try:
      cursor = self.conexion.cursor()
      cursor.execute("SELECT capacidad FROM sala WHERE id = ?", (id_sala, ))
      capacidad = cursor.fetchone()
      if capacidad is not None:
        return capacidad[0]
      else:
        print(f"No se encontro una sala con ID {id_sala}")
        return None
    except sqlite3.Error as e:
      print(f"Error al obtener la capacidad de la sala: {e}")
      return None
