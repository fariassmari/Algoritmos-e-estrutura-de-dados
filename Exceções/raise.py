def fproblema(var):
    raise ZeroDivisionError

try:
    fproblema(4)
except ZeroDivisionError:
    print('Erro na divisão')

print('Fim do programa!!')

# Exemplo2
def fproblema(var):
    try:
        return 1/var
    except ZeroDivisionError:
        print('Erro na divisão')
        raise
try:
    fproblema(0)
except ZeroDivisionError:
    print('Erro tratado aqui')
print('Fim do programa')