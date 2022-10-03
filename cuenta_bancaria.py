


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
        return f"Cliente; {self.nombre} {self.apellido}\nBalance de la cuenta {self.numero_cuenta}: €{self.balance}"

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
    while True:
        
        nombre_cl = input("Ingrese su nombre: ") 
        print("\n")       
        apellido_cl = input("Ingrese su apellido: ")
        print("\n") 
        if nombre_cl.isalpha() == True and apellido_cl.isalpha() == True:
            print(f"Hola {nombre_cl} {apellido_cl}, un placer verte de nuevo")
            print("\n") 
            break

        else:
            print("-- Nombre o Apellido incorrectos --")
            print("\n") 
        
    

    while True:
        
        numero_cuenta = input("Ingrese su numero de cuenta de 8 digitos: ")
        print("\n") 
        if numero_cuenta.isnumeric() == True:           
            print("\n") 
            
            if int(numero_cuenta) == int(numero_cuenta) in range(9999999,99999999):
                print(f'Tu numero de cuenta es {numero_cuenta}')
                break
            else:
                print("-- Numero de cuenta incorrecto !!\n recuerda que el numero no puede empezar por '0'\n y debe contener '8' digitos --")
                print("\n") 
               
        else:   
            print("-- Recuerda que solo puedes poner digitos --") 
            print("\n")       
            
                
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

    while True:
        while opcion != "S":
            print("Elige una opcion: Depositas (D), Retirar (R), o Salir (S)")
            print("\n") 

            opcion = input()

            if opcion == "D" or opcion == "d":
                cantidad_dep = (input("Cantidad a depositar: "))
                print("\n") 
                if cantidad_dep.isnumeric() == True:
                    mi_cliente.depositar(int(cantidad_dep))
                else:
                    print("-- Recuerda que solo puedes depositar dinero --")
                    print("\n") 
                
            elif opcion == "R" or opcion == "r":
                cantidad_ret = (input("Cantidad a retirar: "))
                print("\n") 
                if cantidad_ret.isnumeric() == True:
                    mi_cliente.retirada(int(cantidad_ret))
                else:
                    print("-- Recuerda que solo puedes retirar dinero --")
                    print("\n") 
                
            print(mi_cliente)

        print("\n") 
        print("Gracias por operar en Banco Python")
        break

inicio()
