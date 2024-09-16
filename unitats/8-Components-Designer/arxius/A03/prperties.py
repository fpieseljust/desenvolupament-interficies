class Componente:
    def __init__(self, atributo):
        self.__atributo = atributo

    @property
    def atributo(self):
        return self.__atributo
    
    @atributo.setter
    def atributo(self, nuevo_atributo):
        if nuevo_atributo > 0 and isinstance(nuevo_atributo, int):
            self.__atributo = nuevo_atributo
        else:
            print("Por favor, ingrese un valor entero positivo para el atributo")

componente = Componente(10)
print(componente.atributo)
componente.atributo = -1
print(componente.atributo)
componente.atributo = 20
print(componente.atributo)