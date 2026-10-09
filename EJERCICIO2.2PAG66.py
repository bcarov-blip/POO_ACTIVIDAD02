from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    # Constructor
    def __init__(
        self,
        nombre=None,
        cantidad_satelites=0,
        masa=0.0,
        volumen=0.0,
        diametro=0,
        distancia_media_sol=0,
        tipo=None,
        observable=False
    ):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_media_sol = distancia_media_sol
        self.tipo = tipo
        self.observable = observable

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Cantidad de satelites:", self.cantidad_satelites)
        print("Masa (kg):", self.masa)
        print("Volumen (km cubicos):", self.volumen)
        print("Diametro (km):", self.diametro)
        print("Distancia media al Sol (millones de km):",
              self.distancia_media_sol)
        print("Tipo de planeta:",
              self.tipo.value if self.tipo else "No especificado")
        print("Observable a simple vista:",
              "Si" if self.observable else "No")
        
    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        UA_KM = 149597870
        distancia_km = self.distancia_media_sol * 1_000_000
        return distancia_km > 3.4 * UA_KM
    
def main():
    # Crear dos planetas
    planeta1 = Planeta(
        "Tierra",
        1,
        5.972e24,
        1.08321e12,
        12742,
        149.6,
        TipoPlaneta.TERRESTRE,
        True
    )

    planeta2 = Planeta(
        "Jupiter",
        95,
        1.898e27,
        1.4313e15,
        139820,
        778.5,
        TipoPlaneta.GASEOSO,
        True
    )

    planetas = [planeta1, planeta2]

    for planeta in planetas:
        print("\n===== DATOS DEL PLANETA =====")
        planeta.imprimir_datos()

        print("Densidad (kg/km cubicos):",
              planeta.calcular_densidad())

        print("Es un planeta exterior:",
              "Si" if planeta.es_planeta_exterior() else "No")


if __name__ == "__main__":
    main()