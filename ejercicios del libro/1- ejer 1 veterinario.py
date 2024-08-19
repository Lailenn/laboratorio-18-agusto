class Veterinaria:
    def __init__(self, peso=0, nombre="", raza="", color="", edad=0, genero=""):
        self.estado = "NO ATENDIDO"
        self.peso = peso
        self.tamano = self.tamano()
        self.nombre = nombre
        self.raza = raza  
        self.color = color
        self.edad = edad
        self.genero = genero

    def tamano(self):
        return "Perro Pequeño" if self.peso <= 10 else "Perro Grande"

    def modificar_estado_inicial(self):
        self.estado = "ATENDIDO"

    def entrada_datos(self):
        print("----------------------------------------------------------")
        self.nombre = input("Nombre del Perro: ")
        self.raza = input("Ingrese qué raza: ")
        self.color = input("Ingrese el color : ")
        self.edad = int(input("Ingrese la edad: "))
        self.peso = int(input("Ingrese el peso en kg: "))
        self.genero = input("Ingrese el género de ")
        self.tamano = self.tamano()
        print("----------------------------------------------------------")


    def muestra_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Color: {self.color}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Género: {self.genero}")
        print(f"Estado: {self.estado}")

perro = Veterinaria()
perro.entrada_datos()
perro.cambiar_estado()
perro.muestra_datos()
