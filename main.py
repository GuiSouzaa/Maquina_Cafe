from Maquina import Maquina
from Cafe import Cafe
from CafeLeite import CafeLeite
from principal import escolherTipo

if __name__ == "__main__":
   
    maquina01 = Maquina(False) #Estado da maquina ligado/desligado
    maquina01.ligar()
    maquina01.definir_acucar()
    cafe = Cafe('')
    cafeleite = CafeLeite('')
    escolherTipo(maquina01, cafe, cafeleite)