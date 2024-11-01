class Maquina:
    def __init__(self, tipos):
        self.tipos = tipos
        self.ativo = tipos

    def ligar(self):
        if not self.ativo:
            self.ativo = True
            print("A maquina está LIGADA")
        

    def desligar(self):
        
        if not self.ativo:
            self.ativo = False
            print('Maquina está DESLIGADA')
