class Electronica:
    def __init__(self, tipo, modelo, capacidad, color, pantalla, bateria, costo):
        self.tipo = tipo
        self.modelo = modelo
        self.capacidad = capacidad
        self.color = color
        self.pantalla = pantalla
        self.bateria = bateria
        self.costo = costo
        self.marca = "PHR"
        self.origen = "Importado"
        self.precio_venta = self.estimar_precio_venta()

    def estimar_precio_venta(self):
        return self.costo * 1.7

    def detalles_electronica(self):
        return (
            f"\nCaracterísticas del dispositivo:\n"
            f"Tipo: {self.tipo}\n"
            f"Modelo: {self.modelo}\n"
            f"Capacidad: {self.capacidad}\n"
            f"Color: {self.color}\n"
            f"Tamaño de Pantalla: {self.pantalla}\n"
            f"Capacidad de Batería: {self.bateria}\n"
            f"Marca: {self.marca}\n"
            f"Origen: {self.origen}\n"
            f"Precio de Compra: ${self.costo:.2f}\n"
            f"Precio de Venta: ${self.precio_venta:.2f}\n"
        )


def registrar_electronica():
    tipo = input("Ingrese el tipo de dispositivo (Celular/Tablet/Portátil): ")
    modelo = input("Ingrese el modelo del dispositivo: ")
    capacidad = input("Ingrese la capacidad del dispositivo (e.g., 128GB, 8GB RAM): ")
    color = input("Ingrese el color del dispositivo: ")
    pantalla = input("Ingrese el tamaño de la pantalla (e.g., 6.5 pulgadas): ")
    bateria = input("Ingrese la capacidad de la batería (e.g., 4000mAh): ")
    costo = float(input("Ingrese el precio de compra del dispositivo: "))
    
    return Electronica(tipo, modelo, capacidad, color, pantalla, bateria, costo)


print("Registro del primer dispositivo:")
electronica1 = registrar_electronica()
print(electronica1.detalles_electronica())

print("\nRegistro del segundo dispositivo:")
electronica2 = registrar_electronica()
print(electronica2.detalles_electronica())
