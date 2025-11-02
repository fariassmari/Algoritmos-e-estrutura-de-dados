from questao1 import No, Lista_Encadeada

def pertinencia(valor, lista):
    p = lista.inicio
    while p != None:
        if p.dado == valor:
            return True
        p = p.prox
    return False

def uniao(A, B):
    resultado = Lista_Encadeada()
    p = A.inicio
    while p != None:
        resultado.adicionar_final(No(p.dado))
        p = p.prox
    
    q = B.inicio
    while q != None:
        if not pertinencia(q.dado, resultado):
            resultado.adicionar_final(No(q.dado))
        q = q.prox
    return resultado

def intersecao(A, B):
    resultado = Lista_Encadeada()
    p = A.inicio
    while p != None:
        if pertinencia(p.dado, B) and not pertinencia(p.dado, resultado):
            resultado.adicionar_final(No(p.dado))
        p = p.prox
    return resultado

def diferenca(A, B):
    resultado = Lista_Encadeada()
    p = A.inicio
    while p != None:
        if not pertinencia(p.dado, B):
            resultado.adicionar_final(No(p.dado))
        p = p.prox
    return resultado

A = Lista_Encadeada()
A.adicionar_final(No(1))
A.adicionar_final(No(2))
A.adicionar_final(No(3))
A.adicionar_final(No(5))
A.adicionar_final(No(6))

B = Lista_Encadeada()
B.adicionar_final(No(3))
B.adicionar_final(No(4))
B.adicionar_final(No(5))
B.adicionar_final(No(6))
B.adicionar_final(No(7))

print("A:")
print(A)
print("B:")
print(B)

print("União:")
uni = uniao(A, B)
print(uni)     # 1 2 3 4 5

print("Interseção:")
inter = intersecao(A, B)
print(inter)   # 3

print("Diferença A-B:")
dif1 = diferenca(A, B)
print(dif1)    # 1 2

print("Diferença B-A:")
dif2 = diferenca(B, A)
print(dif2)   # 4 5