def KelvinToFahrenheit(temperatura):
    assert (temperatura >= 0), 'Mais frio do que o zero absoluto!'
    return ((temperatura-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
#print(KelvinToFahrenheit(-5))

import math
try:
    x = float(input('x= '))
    assert x>=0.0
    x=math.sqrt(x)
    print('Raiz:',x)

except AssertionError:
    print(x,'é invalido')

print('Fim do programa')