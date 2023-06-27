def encontrar_dois_numeros(lista, valor_alvo):
    complementos = set()

    for num in lista:
        complemento = valor_alvo - num
        if complemento in complementos:
            return [complemento, num]
        complementos.add(num)

    return None
