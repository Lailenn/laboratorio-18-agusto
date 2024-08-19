class Vehiculo:
    def __init__(self, marca, modelo, año, color, combustible, transmision, motor, origen, costo):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.combustible = combustible
        self.transmision = transmision
        self.motor = motor
        self.origen = origen
        self.costo = costo
        self.precio_venta = self.estimar_precio_venta()
        self.ruedas = 4
        self.capacidad = 5

    def estimar_precio_venta(self):
        return self.costo * 1.4

    def detalles_vehiculo(self):
        return (
            f"\nCaracterísticas del vehículo:\n"
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Año: {self.año}\n"
            f"Color: {self.color}\n"
            f"Tipo de Combustible: {self.combustible}\n"
            f"Transmisión: {self.transmision}\n"
            f"Motor: {self.motor}\n"
            f"Origen: {self.origen}\n"
            f"Ruedas: {self.ruedas}\n"
            f"Capacidad de pasajeros: {self.capacidad}\n"
            f"Precio de Compra: ${self.costo:.2f}\n"
            f"Precio de Venta: ${self.precio_venta:.2f}\n"
        )


def registrar_vehiculo():
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    año = input("Ingrese el año del vehículo: ")
    color = input("Ingrese el color del vehículo: ")
    combustible = input("Ingrese el tipo de combustible (Gasolina/Diesel/Eléctrico): ")
    transmision = input("Ingrese el tipo de transmisión (Automática/Manual): ")
    motor = input("Ingrese el tipo de motor (e.g., 1.8L): ")
    origen = input("Ingrese el origen del vehículo (Nacional/Importado): ")
    costo = float(input("Ingrese el precio de compra del vehículo: "))
    
    return Vehiculo(marca, modelo, año, color, combustible, transmision, motor, origen, costo)


print("Registro del primer vehículo:")
vehiculo1 = registrar_vehiculo()
print(vehiculo1.detalles_vehiculo())

print("\nRegistro del segundo vehículo:")
vehiculo2 = registrar_vehiculo()
print(vehiculo2.detalles_vehiculo())
