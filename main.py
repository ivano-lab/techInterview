from soma_pares import soma_pares
from encontrar_dois_numeros import encontrar_dois_numeros
from busca_binaria import busca_binaria

def main():
    # Teste da função somar_numeros_pares
    numeros_pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = soma_pares(numeros_pares)
    print(f"A soma dos números pares na lista é: {resultado}")

    # Teste da função encontrar_dois_numeros
    numeros = [2, 4, 6, 8, 10, 12]
    valor_alvo = 12
    numeros_encontrados = encontrar_dois_numeros(numeros, valor_alvo)
    if numeros_encontrados is not None:
        print(f"Dois números que somam {valor_alvo}: {numeros_encontrados[0]} e {numeros_encontrados[1]}")
    else:
        print("Não foi possível encontrar dois números que somam o valor alvo.")

    # Teste da função busca_binaria
    arr = [1, 3, 5, 7, 9]
    alvo = 7
    indice = busca_binaria(arr, alvo)
    if indice != -1:
        print(f"O elemento {alvo} está presente no índice {indice} do array.")
    else:
        print(f"O elemento {alvo} não foi encontrado no array.")

if __name__ == '__main__':
    main()
