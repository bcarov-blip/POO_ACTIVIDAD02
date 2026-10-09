
class Persona:
    def __init__(self, nombre, apellido, documento, anio_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.anio_nacimiento = anio_nacimiento

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Documento de identidad:", self.documento)
        print("Año de nacimiento:", self.anio_nacimiento)
        print("-----------------------------")

def main():
    # Crear dos personas
    persona1 = Persona("Carlos", "Ramírez", "123456789", 2005)
    persona2 = Persona("María", "Gómez", "987654321", 2006)

    # Mostrar los datos de las personas
    print("DATOS DE LA PERSONA 1")
    persona1.mostrar_datos()

    print("DATOS DE LA PERSONA 2")
    persona2.mostrar_datos()

if __name__ == "__main__":
    main()