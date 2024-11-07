from Maquina import Maquina

def ligar_maquina(maquina):
    botao = input('ligar/Desligar')

    if botao.lower() == 'ligar':
        maquina.ligar()

    elif botao.lower() == 'desligar':
        maquina.desligar()
    else:
        print('Comando invalido')


def escolherTipo(maquina, cafe, cafeleite):

    if not maquina.ativo:
        print('Maquina desligada, volte mais tarde')
        return
    
    tipo = input('cafe(1) / cafeLeite(2)')

    if tipo.lower() == '1':
        cafe.escolhido()
    
    elif tipo.lower() == '2':
        cafeleite.escolhido()
    else:
        print('Escolha invalida')
