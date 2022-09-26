class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance


    def __str__(self):
        return f"Cliente; {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: €{self.balance}"

    def depositar(self,deposito):
        self.balance += deposito
        print("Deposito aceptado")

    def retirada(self, retirada):
        if self.balance >= retirada:
            self.balance -= retirada
            print("Retirada realizada")
        else:
            print("Fondos insuficientes")

def crear_cliente():
    nombre_cl = input("ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl,apellido_cl, numero_cuenta)
    return cliente

def inicio():

    print('*' * 50)
    print('*' * 5 + " Bienvenido a tu cuenta bancaria " + '*' * 5)
    print('*' * 50)
    print('\n')

    mi_cliente = crear_cliente()
    print(mi_cliente)

    opcion = 0

    while opcion != "S":
        print("Elige una opcion: Depositas (D), Retirar (R), o Salir (S)")

        opcion = input()

        if opcion == "D":
            cantidad_dep = int(input("Cantidad a depositar: "))
            mi_cliente.depositar(cantidad_dep)
        elif opcion == "R":
            cantidad_ret = int(input("Cantidad a retirar: "))
            mi_cliente.retirada(cantidad_ret)
        print(mi_cliente)

    print("Gracias por operar en Banco Python")

inicio()