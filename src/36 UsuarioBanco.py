class UsuarioBanco:

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            raise ValueError("No hay saldo suficiente para retirar dinero.")

    def transferir_dinero(self, otro_usuario, cantidad):
        if otro_usuario.saldo >= cantidad:
            otro_usuario.saldo -= cantidad
            self.saldo += cantidad
        else:
            raise ValueError("El usuario no tiene saldo suficiente para transferir.")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad


# Caso de uso

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 60, True)

bob.agregar_dinero(20)

# Bob transfiere 80 a Alicia
alicia.transferir_dinero(bob, 80)

alicia.retirar_dinero(50)

print("Saldo Alicia:", alicia.saldo)
print("Saldo Bob:", bob.saldo)