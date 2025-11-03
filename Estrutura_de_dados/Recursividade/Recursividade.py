def soma(n):
    if n <= 1:
        return n
    else:
        return n + soma(n-1)
    
soma1 = soma(4)
print(soma1)
