import sqlite3

class Connection:

    def __init__(self, nombreBD):
        self.conexion = sqlite3.connect(nombreBD)
        self.cursor = self.conexion.cursor()

    def CrearTablaEmpleado(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS EMPLEADO(
              id INTEGER PRIMARY KEY,
              nombre TEXT,
              apellido TEXT,
              dni TEXT
            )
        ''')
        self.conexion.commit()

    def PeliculaPorId(self, id):
        self.cursor.execute("SELECT * FROM PELICULA WHERE id = ?", (id,))
        pelicula = self.cursor.fetchone()
        return pelicula

    def ClientePorId(self, id):
        self.cursor.execute("SELECT * FROM CLIENTE WHERE id = ?", (id,))
        cliente = self.cursor.fetchone()
        return cliente

    def CrearTablaPelicula(self):
        self.cursor.execute('''
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
        self.conexion.commit()

    def filtrarPeliculaPorCategoria(self, categoria):
        self.cursor.execute("SELECT * FROM PELICULA WHERE categoria = ?", (categoria,))
        peliculas = self.cursor.fetchall()
        return peliculas

    def CrearVenta(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS VENTA(
              id INTEGER PRIMARY KEY,
              id_producto INTEGER,
              id_cliente INTEGER,
              cantidad INTEGER,
              precio DOUBLE,
              FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id),
              FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id)
            )
        ''')
        self.conexion.commit()

    def MostrarVentas(self):
        self.cursor.execute("SELECT * FROM VENTA")
        ventas = self.cursor.fetchall()
        return ventas

    def MostrarVentasPorIdCliente(self, idCliente):
        self.cursor.execute("SELECT * FROM VENTA WHERE id_cliente = ?", (idCliente,))
        ventas = self.cursor.fetchall()
        return ventas

    def IngresarCliente(self, nombre, apellido, dni):
        self.cursor.execute(
            "INSERT INTO CLIENTE (nombre,apellido,dni) VALUES (?,?,?)",
            (nombre, apellido, dni))
        self.conexion.commit()

    def MostrarClientes(self):
        self.cursor.execute("SELECT * FROM CLIENTE")
        clientes = self.cursor.fetchall()
        return clientes

    def ModificarCliente(self, nombre, apellido, dni, id):
        self.cursor.execute(
            "UPDATE CLIENTE SET nombre=?,apellido=?,dni=? WHERE id = ?",
            (nombre, apellido, dni, id))
        self.conexion.commit()

    def EliminarCliente(self, id):
        self.cursor.execute("DELETE FROM CLIENTE WHERE id = ?", (id,))
        self.conexion.commit()

    def IngresarPelicula(self, nombre, descripcion, idioma, duracion, fecha_estreno, precio, categoria):
        self.cursor.execute(
            "INSERT INTO PELICULA (nombre,descripcion,idioma,duracion,fecha_estreno,precio,categoria) VALUES (?,?,?,?,?,?,?)",
            (nombre, descripcion, idioma, duracion, fecha_estreno, precio, categoria))
        self.conexion.commit()

    def MostrarPelicula(self):
        self.cursor.execute("SELECT * FROM PELICULA")
        peliculas = self.cursor.fetchall()
        return peliculas

    def ModificarPelicula(self, id, nombre, descripcion, idioma, duracion, fecha_estreno, precio, categoria):
        self.cursor.execute(
            "UPDATE PELICULA SET nombre=?, descripcion=?, idioma=?, duracion=?, fecha_estreno=?, precio=?, categoria=? WHERE id = ?",
            (nombre, descripcion, idioma, duracion, fecha_estreno, precio, categoria, id))
        self.conexion.commit()

    def EliminarPelicula(self, id):
        self.cursor.execute("DELETE FROM PELICULA WHERE id = ?", (id,))
        self.conexion.commit()

    def CerrarBD(self):
        self.cursor.close()
        self.conexion.close()
