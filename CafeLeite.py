from Cafe import Cafe
class CafeLeite(Cafe):
    def __init__(self):
        super().__init__("cafe com leite")

    def escolhido(self):
        print('o sabor escolhido foi cafe com leite')