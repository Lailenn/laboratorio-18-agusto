class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo_inicial):
        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial

    def __depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo:.2f}")
        else:
            print("El monto de depósito debe ser positivo.")

    def __retirar(self, monto):
        if monto > 0:
            if monto <= self.__saldo:
                self.__saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo:.2f}")
            else:
                print("Fondos insuficientes para el retiro.")
        else:
            print("El monto de retiro debe ser positivo.")

    def mostrar_detalles(self):
        print(
            f"\nDetalles de la Cuenta:\n"
            f"Titular: {self.__titular}\n"
            f"Número de Cuenta: {self.__numero_cuenta}\n"
            f"Saldo Actual: ${self.__saldo:.2f}\n"
        )

    def operar(self):
        opcion = input("\n¿Desea realizar una operación? (depósito/retiro/mostrar: ").strip().lower()
        if opcion == "depósito":
            monto = float(input("Ingrese el monto a depositar: "))
            self.__depositar(monto)
        elif opcion == "retiro":
            monto = float(input("Ingrese el monto a retirar: "))
            self.__retirar(monto)
        elif opcion == "mostrar":
            self.mostrar_detalles()
        else:
            print("Opción no válida.")

def registrar_cuenta():
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
    
    return CuentaBancaria(titular, numero_cuenta, saldo_inicial)

print("Registro de la primera cuenta:")
cuenta1 = registrar_cuenta()
while True:
    cuenta1.operar()

    respuesta = input("¿Desea repetir el proceso? (1 = sí/2 = no): ").strip().lower()
    if respuesta != "1":
        break 


