
from Vista_Administrador import Vista_Administrador
from Vista_Empleado import Vista_Empleado


class Login:

  def __init__(self):
    pass

  def iniciarSesion(self):
    tipoUsuario = 0

    usuario = input("Ingrese su nombre de Usuario: ")
    passw = input("Ingrese su Password: ")
    if usuario == "1" and passw == "1":
      tipoUsuario = 1
      
    elif usuario == "2" and passw == "2":
      tipoUsuario = 2
    if tipoUsuario == 1:
      admin = Vista_Administrador()
      admin.menu_admin()

    elif tipoUsuario == 2:
      empleado = Vista_Empleado()
      empleado.menu_empleado()
    else:
      print("Usuario desconocido")
