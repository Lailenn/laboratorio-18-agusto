class ArticuloPapeleria:
    def __init__(self, tipo_cuaderno="Desconocido", tipo_lapiz="Desconocido", costo=0):
        self.tipo_cuaderno = tipo_cuaderno
        self.tipo_lapiz = tipo_lapiz
        self.marca_cuaderno = "Hojitas"
        self.marca_lapiz = "Rayas"
        self.costo = costo
        self.precio = self.definir_precio()

    def definir_precio(self):
        return self.costo * 1.30

    def ingresar_datos(self):
        cuaderno_opcion = input("Ingrese '50' para Cuaderno de 50 Hojas o '100' para Cuaderno de 100 Hojas: ")
        self.tipo_cuaderno = "50 Hojas" if cuaderno_opcion == "50" else "100 Hojas" if cuaderno_opcion == "100" else "Desconocido"
        
        lapiz_opcion = input("Ingrese 'grafito' para Lápiz de Grafito o 'color' para Lápiz de Color: ").lower()
        self.tipo_lapiz = "Lápiz de Grafito" if lapiz_opcion == "grafito" else "Lápiz de Color" if lapiz_opcion == "color" else "Desconocido"
        
        self.costo = float(input("Ingrese el costo del artículo: "))
        self.precio = self.definir_precio()

    def desplegar_datos(self):
        print("\nInformación del artículo:")
        print(f"Marca de Cuaderno: {self.marca_cuaderno}")
        print(f"Cuaderno: {self.tipo_cuaderno}")
        print(f"Marca de Lápiz: {self.marca_lapiz}")
        print(f"Lápiz: {self.tipo_lapiz}")
        print(f"Costo: ${self.costo:.2f}")
        print(f"Precio de Venta: ${self.precio:.2f}")


articulo_a = ArticuloPapeleria()
articulo_a.ingresar_datos()
articulo_a.desplegar_datos()

articulo_b = ArticuloPapeleria()
articulo_b.ingresar_datos()
articulo_b.desplegar_datos()
