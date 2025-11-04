def espaco(palavra):
    if palavra == '':
        return 0
    else:
        for c in palavra:
            if c == ' ':
                return 1 + espaco(c)
            else:
                return 0