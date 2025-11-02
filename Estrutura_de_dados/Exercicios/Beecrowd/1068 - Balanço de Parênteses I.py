class Pilha:
    def __init__(self):
        self.__itens = []

    def empilhar(self, item):
        self.__itens.append(item)

    def desempilhar(self):
        if not self.eh_vazio():
            return self.__itens.pop()
    
    def eh_vazio(self):
        return len(self.__itens) == 0
    
class Verificador:
    def __init__(self, expressao=''):
        self.__expressao = expressao

    @property 
    def expressao(self):
        return self.__expressao
    
    @expressao.setter
    def expressao(self, expressao):
        self.__expressao = expressao

    def verificar(self):
        pilha = Pilha()

        for parentese in self.__expressao:
            if parentese == '(':
                pilha.empilhar(parentese)
            elif parentese == ')':
                if pilha.eh_vazio():
                    return'incorrect'
                pilha.desempilhar()

        return 'correct' if pilha.eh_vazio() else 'incorrect'


### MAIN
if __name__ == '__main__':
    verificador = Verificador()

    try:
        while True:
            verificador.expressao = input()
            print(verificador.verificar())
    except EOFError:
        pass