from collections import deque

# Representação do grafo como um dicionário de listas de adjacências
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def busca_em_largura(grafo, inicio, objetivo):
    # Fila para armazenar os nós a serem visitados
    fila = deque([inicio])
    # Dicionário para armazenar os caminhos
    caminho = {inicio: None}

    while fila:
        # Retira o nó da frente da fila
        no_atual = fila.popleft()

        # Verifica se atingiu o objetivo
        if no_atual == objetivo:
            caminho_final = []
            while no_atual is not None:
                caminho_final.append(no_atual)
                no_atual = caminho[no_atual]
            return caminho_final[::-1]  # Retorna o caminho invertido

        # Adiciona os vizinhos à fila, se não foram visitados
        for vizinho in grafo[no_atual]:
            if vizinho not in caminho:
                fila.append(vizinho)
                caminho[vizinho] = no_atual

    return None  # Caso não haja caminho

# Testando o algoritmo
inicio = 'A'
objetivo = 'F'
caminho = busca_em_largura(grafo, inicio, objetivo)

if caminho:
    print(f"Caminho encontrado: {caminho}")
else:
    print("Caminho não encontrado.")
