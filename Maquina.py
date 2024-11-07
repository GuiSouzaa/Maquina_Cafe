class Maquina:
    def __init__(self, ativo):
        self.ativo = ativo
        self.acucar = 0

    def ligar(self):
        if not self.ativo:
            self.ativo = True
            print("A maquina está LIGADA")
        

    def desligar(self):
        
        if self.ativo:
            self.ativo = False
            print('Maquina está DESLIGADA')

    def definir_acucar(self):
        qtnAcucar = input('Digite a quantidade de açucar: 1g, 2g ou 3g')

        if qtnAcucar == '1':
            self.acucar = 1
            print('1g de açucar inserido')

        elif qtnAcucar == '2':
            self.acucar = 2
            print('2g de açucar')

        elif qtnAcucar == '3':
            self.acucar = 3
            print('3g de açucar inserido')

        else:
            self.acucar = 0
            print('0 açucar')
