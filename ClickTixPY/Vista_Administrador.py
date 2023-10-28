from Pelicula_Controller import Pelicula_Controller
from Categoria_Controller import Categoria_Controller
from Connection import Connection


class Vista_Administrador:
    def __init__(self):
        pass

    def gestionar_abm(self):
        while True:
            print("Gestionar ABM")
            print("1. ABM Pelicula")
            print("2. ABM Funciones")
            print("3. ABM Empleados")
            print("4. ABM Promociones")
            print("5. ABM Categorias")
            print("6. Volver al menu anterior")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                conexion = Connection("ClickTix.db")
                pelicula = Pelicula_Controller(conexion)
                pelicula.menu_pelicula()
            elif opcion == "2":
                print("Realizando ABM Funciones...")
            elif opcion == "3":
                print("Realizando ABM Empleados...")
            elif opcion == "4":
                print("Realizando ABM Promociones...")
            elif opcion == "5":
                conexion = Connection("ClickTix.db")
                categoria = Categoria_Controller(conexion)
                categoria.menu_categoria()
            elif opcion == "6":
                break
            else:
                print("Opcion no valida. Por favor, elija una opcion valida.")

    def generar_reportes(self):
        while True:
            print("Generar Reportes")
            print("1. Por Semana")
            print("2. Por Mes")
            print("3. Por Ano")
            print("4. Por Pelicula")
            print("5. Por Sucursal")
            print("6. Volver al menu anterior")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                print("Generando informe por semana...")
            elif opcion == "2":
                print("Generando informe por mes...")
            elif opcion == "3":
                print("Generando informe por ano...")
            elif opcion == "4":
                print("Generando informe por pelicula...")
                pelicula = input("Ingrese el nombre de la pelicula: ")
                submenu_opcion = input(
                    "Seleccione una opcion para la pelicula (1. Semana, 2. Mes, 3. Ano): "
                )
                if submenu_opcion == "1":
                    print("Generando informe por semana para la pelicula", pelicula)
                elif submenu_opcion == "2":
                    print("Generando informe por mes para la pelicula", pelicula)
                elif submenu_opcion == "3":
                    print("Generando informe por ano para la pelicula", pelicula)
                else:
                    print(
                        "Opcion no valida. Por favor, elija una opcion valida para la pelicula."
                    )
            elif opcion == "5":
                print("Generando informe por sucursal...")
                sucursal = input("Ingrese el nombre de la sucursal: ")
                submenu_opcion = input(
                    "Seleccione una opcion para la sucursal (1. Semana, 2. Mes, 3. Ano): "
                )
                if submenu_opcion == "1":
                    print("Generando informe por semana para la sucursal", sucursal)
                elif submenu_opcion == "2":
                    print("Generando informe por mes para la sucursal", sucursal)
                elif submenu_opcion == "3":
                    print("Generando informe por ano para la sucursal", sucursal)
                else:
                    print(
                        "Opcion no valida. Por favor, elija una opcion valida para la sucursal."
                    )
            elif opcion == "6":
                break
            else:
                print("Opcion no valida. Por favor, elija una opcion valida.")

    def menu_admin(self):
        while True:
            print("Menu del Administrador")
            print("1. Gestionar ABM")
            print("2. Generar Reportes")
            print("3. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.gestionar_abm()
            elif opcion == "2":
                self.generar_reportes()
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opcion no valida. Por favor, elija una opcion valida.")
