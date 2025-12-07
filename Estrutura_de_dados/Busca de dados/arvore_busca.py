class Dado:
  def __init__(self):
    self.__chave = None
    self.__indice = None

  @property
  def chave(self):
    return self.__chave

  @chave.setter
  def chave(self, valor):
    self.__chave = valor

  @property
  def indice(self):
    return self.__indice

  @indice.setter
  def indice(self, valor):
    self.__indice = valor

def recebe_registro(registros, chave):
    registros.append(chave)

class No:
    def __init__(self, dado):
        self.__dado = dado
        self.__dir = None
        self.__esq = None

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, valor):
        self.__dado = valor

    @property
    def esq(self):
        return self.__esq

    @esq.setter
    def esq(self, valor):
        self.__esq = valor

    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, valor):
        self.__dir = valor

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, valor):
        self.__registro = valor

class Arvore_Binaria:
  def __init__(self):
    self.__root = None

  @property
  def root(self):
    return self.__root

  @root.setter
  def root(self, root):
    self.__root = root

  # -------- INSERÇÃO EM BST --------
  def inserir(self, dado):
    novo_no = No(dado)

    if self.__root is None:
      self.__root = novo_no
      return 

    atual = self.__root
    while True:
      if dado.chave < atual.dado.chave:
        if atual.esq is None:
          atual.esq = novo_no
          return
        atual = atual.esq
      else:
        if atual.dir is None:
          atual.dir = novo_no
          return
        atual = atual.dir
        
  def em_ordem(self, no):
    if no != None:
      self.em_ordem(no.esq)
      print(no.dado)
      self.em_ordem(no.dir)

  def pre_ordem(self, no):
    if no != None:
      print(no.dado)
      self.pre_ordem(no.esq)
      self.pre_ordem(no.dir)

  def pos_ordem(self, no):
    if no != None:
      self.pos_ordem(no.esq)
      self.pos_ordem(no.dir)
      print(no.dado)


def cria_arvore(chaves):
    arvore = None
    p = None
    q = None

    item = Dado()

    item.chave = chaves[0]
    item.indice = 0
    arvore = No(item)

    for i in range(1, len(chaves)):
        p = q = arvore

        while chaves[i] != p.dado.chave and q != None:
            p = q
            if chaves[i] < p.dado.chave:
                q = p.esq
            else:
                q = p.dir

        item = Dado()
        item.chave = chaves[i]
        item.indice = i

        q = No(item)

        if chaves[i] < p.dado.chave:
            p.esq = q
        else:
            p.dir = q
        
    return arvore

def cria_rec(chaves, inicio, fim):
  if inicio <= fim:
    meio = (inicio + fim) // 2

    raiz = Dado()
    raiz.chave = chaves[meio]
    raiz.indice = meio

    arvore = No(raiz)

    arvore.esq = cria_rec(chaves, inicio, meio-1)
    arvore.dir = cria_rec(chaves, meio+1, fim)

    return arvore
  return None

def imprimir_arvore(arvore, nivel=0):
  if arvore is not None:
    imprimir_arvore(arvore.esq, nivel + 1)
    print(arvore.dado.chave)
    imprimir_arvore(arvore.dir, nivel + 1)
    
def encontra_indice(chave, arvore):
  if arvore == None:
    return -1
  if chave == arvore.dado.chave:
    return arvore.dado.indice
  elif chave < arvore.dado.chave:
    return encontra_indice(chave, arvore.esq)
  else:
    return encontra_indice(chave, arvore.dir)

def encontra_indice_insere(chave, arvore, registros):
  if arvore == None:
    item = Dado()
    item.chave = chave
    item.indice = len(registros)

    novo_no = No(item)
    registros.append(item)
    return novo_no, item.indice
  if chave == arvore.dado.chave:
    return arvore, arvore.dado.indice
  elif chave < arvore.dado.chave:
    novo, indice = encontra_indice_insere(chave, arvore.esq, registros)
    arvore.esq = novo
    return arvore, indice
  else:
    novo, indice = encontra_indice_insere(chave, arvore.dir, registros)
    arvore.dir = novo
    return arvore, indice

def remover(chave, arvore):
  if arvore == None:
     return None
  if chave < arvore.dado.chave:
    arvore.esq = remover(chave, arvore.esq)
    return arvore
  elif chave > arvore.dado.chave:
    arvore.dir = remover(chave, arvore.dir)

  # Não possui nenhum filho
  if arvore.esq == None and arvore.dir == None:
      return None
  
  # Possui um filho
  if arvore.esq == None:
    return arvore.dir 
  if arvore.dir == None:
    return arvore.esq

  # Possui dois filhos
  sucessor = arvore.dir
  while sucessor.esq is not None:
     sucessor = sucessor.esq

  arvore.dado = sucessor.dado

  arvore.dir = remover(sucessor.dado.chave, arvore.dir)    
  return arvore
      
  
if __name__ == '__main__':

  chaves = [1, 5, 6, 12, 15, 17, 18, 27, 28, 40]
  registros = []

  print(chaves)

  resultado = None
  for chave in chaves:
    resultado, indice = encontra_indice_insere(chave, resultado, registros)

  imprimir_arvore(resultado)

  print("Índice da chave 40 =", encontra_indice(40, resultado))

  resultado, indice = encontra_indice_insere(30, resultado, registros)
  print("Nova chave inserida no índice =", indice)
'''
  resultado = cria_rec(chaves, 0, len(chaves)-1)

  imprimir_arvore(resultado)
  indice = encontra_indice(40, resultado)
  print(indice)

  arvore, indice2 = encontra_indice_insere(60, resultado, registros)
  print("Nova chave inserida no índice =", indice2)

  menor = menor_valor(arvore.root)
  print(menor) 
  maior = maior_valor(arvore.root)
  print(maior)
  #cresc = crescente(arvore.root)
  #decresc = decrescente(arvore.root)

  busca_b = busca_binaria_rec(chaves, 17, 0, len(ord)-1)
  print(busca_b)'''
  
