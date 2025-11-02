index = int(input('Index= '))

try:
    notas = [9.0, 8.0, 7.0]
    print(notas[index])
except IndexError:
    print('Indice invalido')
else:
    print('Acesso realizado com sucesso!!')
finally:
    print('Indexação dinâmica tratada')
print('Continua depois do try-except-finally')