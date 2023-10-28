from Pelicula_Controller import Pelicula_Controller
from Ticket_Controller import Ticket_Controller
from Turno_Controller import Turno_Controller
from Dimension_Controller import Dimension_Controller
from Funcion_Controller import Funcion_Controller
from Sala_Controller import Sala_Controller
from Connection import Connection 
import datetime

class Vista_Empleado:

    def __init__(self):
        pass

    def retirar_tickets(self):
        while True:
            print("Retirar Tickets")
            print("1. Escanear QR")
            print("2. Ingresar Codigo Manualmente")
            print("3. Volver al menu anterior")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1" or opcion == "2":
                print("Imprimiendo ticket...")
            elif opcion == "3":
                break
            else:
                print("Opcion no valida. Por favor, elija una opcion valida.")

    def obtener_entero_valido(self, mensaje):
        while True:
            entrada = input(mensaje)
            if entrada.isdigit():
                return int(entrada)
            else:
                print("Por favor, ingrese un numero entero valido.")

    def vender_entradas(self):
        print("\nVender Entradas\n")
        conexion = Connection("ClickTix.db")
        pelicula = Pelicula_Controller(conexion)
        funcion = Funcion_Controller(conexion)
        dimension = Dimension_Controller(conexion)
        sala = Sala_Controller(conexion)
        while True:
            print("\nSeleccione una funcion o ingrese 0 para salir:\n")
            conexion = Connection("ClickTix.db")
            funcion = Funcion_Controller(conexion)
            listFunciones = funcion.mostrar_funcionesAB()
            for funcionIn in listFunciones:
                print(
                    f"ID:{funcionIn[0]} | Fecha:{funcionIn[1]} | Pelicula: {funcionIn[2]} | Numero de Sala: {funcionIn[3]} | Dimension: {funcionIn[4]} | Horario: {funcionIn[5]} | Disponibilidad: {funcionIn[6]}"
                )
            print("")
            seleccion = self.obtener_entero_valido(
                "Ingrese el numero de ID de la funcion a la cual desea comprar su entrada: "
            )
            if seleccion == 0:
                print("Volviendo al menu anterior...")
                break
            funcion_id = seleccion
            listFunciones = funcion.mostrar_funciones()
            seEncontro = False
            idFuncionEncontrada = 0
            idSalaEncontrada = 0
            for f in listFunciones:
                if f[0] == funcion_id:
                    idFuncionEncontrada = f[0]
                    idSalaEncontrada = f[1]
                    seEncontro = True
                    break
            if seEncontro:
                cantidadTickets = self.obtener_entero_valido(
                    "Ingrese la cantidad de tickets que quiere sacar de esta funcion: "
                )
                if cantidadTickets == 0:
                    print("Volviendo al Menu de venta...\n")
                    break
                if (
                    funcion.obtener_disponibilidad(idFuncionEncontrada) != -1
                    and funcion.obtener_disponibilidad(idFuncionEncontrada) >= cantidadTickets
                ):
                    ticket = Ticket_Controller(conexion)
                    for _ in range(cantidadTickets):
                        ticket.ingresar_ticket(idFuncionEncontrada, datetime.date.today())
                    funcion.restarDisponibilidad(idFuncionEncontrada, cantidadTickets)
                    funcionTicket = funcion.mostrarFuncionPorId(idFuncionEncontrada)
                    if funcionTicket is not None:
                        fecha = funcionTicket[0][1]
                        pelicula = funcionTicket[0][2]
                        numero_sala = funcionTicket[0][3]
                        dimension = funcionTicket[0][4]
                        horario = funcionTicket[0][5]
                        print("\n\n<======= T I C K E T =======>")
                        print("Fecha:    {}".format(fecha))
                        print("Pelicula: {}".format(pelicula))
                        print("Sala:     {}".format(numero_sala))
                        print("Dimension: {}".format(dimension))
                        print("Horario:  {}".format(horario))
                        print("<======= Disfruta la funcion =======>\n\n")
                        break
                else:
                    print(
                        "ERROR: No hay disponibilidad suficiente, solo quedan ",
                        funcion.obtener_disponibilidad(idFuncionEncontrada),
                        " lugares!\n",
                    )
            else:
                print("No se encontro el ID de la funcion")

    def menu_empleado(self):
        while True:
            print("Menu del Empleado")
            print("1. Retirar Tickets")
            print("2. Vender Entradas")
            print("3. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.retirar_tickets()
            elif opcion == "2":
                self.vender_entradas()
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opcion no valida. Por favor, elija una opcion valida.")
