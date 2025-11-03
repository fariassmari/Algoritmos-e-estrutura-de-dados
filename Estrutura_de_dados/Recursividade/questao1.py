def calcular(numero, n):
    if n == 0:
        return 1
    elif n > 0:
        return numero * calcular(numero, n-1)
    elif n < 0: 
        return 1 / calcular(numero, -n)
    
teste = calcular(3, -3)
print(teste)
