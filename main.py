from paquete.registro import registrar_usuario, mostrar_usuarios, login_usuario

# Menu principal

def menu():
    while True:
        print("Bienvenido! que desea hacer?")
        print("1. Registrar un nuevo usuario")
        print("2. Mostrar usuarios existentes")
        print("3. Login")
        print("4. Salir")
        opcion = input("Seleccione una opcion numerica valida: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login_usuario()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")

menu()