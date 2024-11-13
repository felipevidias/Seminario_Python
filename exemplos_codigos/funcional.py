# Funções puras
def soma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

# Função funcional que aplica outra função a uma lista
def aplica_funcao_lista(funcao, lista):
    return list(map(funcao, lista))

def main():
    numeros = [1, 2, 3, 4, 5]

    # Soma 10 a cada elemento da lista
    resultado_soma = aplica_funcao_lista(lambda x: soma(x, 10), numeros)

    # Multiplica cada elemento da lista por 2
    resultado_multiplica = aplica_funcao_lista(lambda x: multiplica(x, 2), numeros)

    print(f"Soma aplicada à lista: {resultado_soma}")
    print(f"Multiplicação aplicada à lista: {resultado_multiplica}")

if __name__ == "__main__":
    main()
