def busca_binaria(arr, alvo):
    baixo = 0
    alto = len(arr) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1
