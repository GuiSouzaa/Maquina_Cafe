from Maquina import Maquina
from Cafe import Cafe
from CafeLeite import CafeLeite
from principal import ligar_maquina
from principal import escolherTipo

if __name__ == "__main__":
    # maquina01 = Maquina(False)
    # maquina01.ligar()

    # #classe cafe
    # maquinaCafe = Cafe('cafe')
    # maquinaCafe.escolhido()

    # #cafe com leite
    # maquinaCafeComLeite = CafeLeite()
    # maquinaCafeComLeite.escolhido()

    maquina01 = Maquina(False)
    ligar_maquina(maquina01)
    
    cafe = Cafe("café")
    cafeleite = CafeLeite()

    
    escolherTipo(maquina01, cafe, cafeleite)