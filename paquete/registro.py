from paquete.cliente import Cliente

baseDeDatos = {}

# Funcion para nuevo registro

def registrar_usuario():
    while True:
        nombre_usuario = input("Ingrese el nombre de usuario: ").strip()
        if nombre_usuario == "":
            print("El nombre de usuario no puede estar en blanco. Intente de nuevo.")
        elif nombre_usuario in baseDeDatos:
            print("El usuario ya existe. Intente con otro nombre.")
        else:
            while True:
                contraseña = input("Ingrese la contraseña: ")
                if contraseña == "":
                    print("La contraseña no puede estar en blanco. Intente de nuevo.")
                else:
                    edad = input("Ingrese la edad: ")
                    direccion = input("Ingrese la direccion: ")
                    email = input("Ingrese el email: ")

                    # Crear una instancia en Cliente
                    cliente = Cliente(nombre_usuario, edad, direccion, email, contraseña)
                    
                    # Almacenar el cliente en baseDeDatos
                    baseDeDatos[nombre_usuario] = cliente
                    print(f"Usuario {nombre_usuario} registrado con éxito.")
                    return

# Funcion para mostrar registros existentes

def mostrar_usuarios():
    if baseDeDatos:
        print("Usuarios registrados:")
        for usuario, cliente in baseDeDatos.items():
            print(cliente)
    else:
        print("Actualmente no hay usuarios registrados.")

# Funcion para el login de usuarios

def login_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    if nombre_usuario in baseDeDatos:
        contraseña = input("Ingrese la contraseña: ")
        if baseDeDatos[nombre_usuario].contraseña == contraseña:
            print("Inicio de sesion exitoso.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("El usuario no existe.")