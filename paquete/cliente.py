# Primer modulo

class Cliente:
    def __init__(self, nombre, edad, direccion, email, contraseña):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.email = email
        self.contraseña = contraseña

    def __str__(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}, Email: {self.email}"

    def cambiar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"La dirección de {self.nombre} ha sido actualizada a: {self.direccion}")

    def cambiar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"Se ha actualizado la dirección de email de {self.nombre} a {self.email}")
