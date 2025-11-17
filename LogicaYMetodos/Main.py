from LogicaYMetodos.Arbol import ArbolGeneral


class Control:
    def __init__(self):
        self.arbol = ArbolGeneral()
        self.carpetaActual = self.arbol.raiz

    def main(self):
        self.arbol.agregarContraseña("Amazon", "Fabricio", "12345", None)
        self.arbol.agregarContraseña("Prime", "Damian", "54321", None)
        self.arbol.agregarContraseña("Computrabajo", "Ana", "aaaaa", None)
        self.arbol.agregarCarpeta("Redes sociales", None)
        self.arbol.agregarCarpeta("Cuentas bancarias", None)


# para que no se ejecute al ser importado, solo cunado otro lo ocupe
if __name__ == "__main__":
    obj = Control()
    obj.main()
