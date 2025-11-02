lista = [30, 40, 50, 60, 70]
lista.append(80)
lista.append(90)
lista.insert(0, 20)

print(lista) # [20, 30, 40, 50, 60, 70, 80, 90]

lista.pop() # Remove o ultimo indice
lista.pop(4) # Remove o elemento do indice 4
print(lista) # [20, 30, 40, 50, 70, 80]

lista.remove(20) # Remove o elemento 20
print(lista) # [30, 40, 50, 70, 80]

print(lista.index(70, 2, 4)) # 3

print(lista.count(80)) # 1

lista.sort(reverse=True)
print(lista) # [80, 70, 50, 40, 30]

lista.sort(reverse=False)
print(lista) # [30, 40, 50, 70, 80]

nomes = ['thiago', 'ana', 'carla', 'emonel', 'maria']
nomes.sort(key=len) # Ordena pelo tamanho
print(nomes)