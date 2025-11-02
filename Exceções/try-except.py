a = int(4)
b = int(2)

try:
    print(a/b)
    print('Sucesso')

except ZeroDivisionError:
    print('Divisão por zero!!!')

except ValueError:
    print('Digite um inteiro válido')

except:
    print('Erro na programação')

print('Fim do programa!!')