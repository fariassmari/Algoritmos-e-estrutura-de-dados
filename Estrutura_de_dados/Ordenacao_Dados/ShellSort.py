def shellSort(tabela):
    count = len(tabela) // 2

    while count > 0:
        for start in range(count):
            for i in range(start+count, len(tabela), count):
                value, position = tabela[i], i
                while position >= count and tabela[position-count] > value:
                    tabela[position], position = tabela[position-count], position-count

                tabela[position] = value
            count = count // 2

