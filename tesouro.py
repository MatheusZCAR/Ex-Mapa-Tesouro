import numpy as np   # biblioteca para manipulação de matrizes
import random as ran  # biblioteca para escolhas aleatórias

linha = 1  # linha da matriz, somar 1 fará com que o personagem vá para baixo, subtrair 1 fará com que o personagem S vá para cima
coluna = 1 # coluna da matriz, somar 1 fará com que o personagem vá para direita, subtrair 1 fará com que o personagem S vá para esquerda
opcoes = [1, 2, 3, 4]   # possibilidades de movimentos
passos = 0  # número de passos dados

matrix = np.array([
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", ".", ".", ".", ".", "#"],
    ["#", ".", "#", ".", "#", "#", "#"],
    ["#", ".", ".", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", ".", "#"],
    ["#", ".", ".", "T", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
])  # a matriz representa o mapa do tesouro, sendo # caminho bloqueado, . caminho livre, S o jogador e T o tesouro

def andar_baixo():   # função de andar para baixo
    global linha, coluna, opcoes, passos, matrix   # tornando as variáveis globais para que possam ser usadas dentro da função
    if matrix[linha + 1][coluna] != "#":   # se o caminho de baixo não estiver bloqueado
        matrix[linha][coluna] = "."   # define o caminho atual como livre
        linha += 1   # vai para baixo
        passos += 1  # soma 1 passo
        
        if matrix[linha][coluna] == "T":  # se o caminho que fomos é o T, achamos o tesouro
            print(f"Tesouro encontrado em {passos} passos")
            return
        else:   # caso contrário, só andamos para baixo
            print("Andando para baixo")
            matrix[linha][coluna] = "S"   # definimos a nova posição como a do jogador
            return

def andar_cima():
    global linha, coluna, opcoes, passos, matrix
    if matrix[linha - 1][coluna] != "#":
        matrix[linha][coluna] = "."
        linha -= 1
        passos += 1
        
        if matrix[linha][coluna] == "T":
            print(f"Tesouro encontrado em {passos} passos")
            return
        else:
            print("Andando para cima")
            matrix[linha][coluna] = "S"
            return

def andar_direita():
    global linha, coluna, opcoes, passos, matrix
    if matrix[linha][coluna + 1] != "#":
        matrix[linha][coluna] = "."
        coluna += 1
        passos += 1
        
        if matrix[linha][coluna] == "T":
            print(f"Tesouro encontrado em {passos} passos")
            return
        else:
            print("Andando para direita")
            matrix[linha][coluna] = "S"
            return

def andar_esquerda():
    global linha, coluna, opcoes, passos, matrix
    if matrix[linha][coluna - 1] != "#":
        matrix[linha][coluna] = "."
        coluna -= 1
        passos += 1
        
        if matrix[linha][coluna] == "T":
            print(f"Tesouro encontrado em {passos} passos")
            return
        else:
            print("Andando para esquerda")
            matrix[linha][coluna] = "S"
            return
    
def main():   # função principal
    global linha, coluna, opcoes, passos, matrix
    while matrix[linha][coluna] != "T":   # enquanto não chegarmos ao tesouro, executaremos o código
        escolhido = ran.choice(opcoes)   # escolhido é uma variável que recebe a escolha aleatória das opcoes
        
        if escolhido == 1:  # se a opção for 1, ande para baixo
            andar_baixo()
        if escolhido == 2:  # se a opção for 2, ande para cima
            andar_cima()
        if escolhido == 3:  # se a opção for 3, ande para direita
            andar_direita()
        if escolhido == 4:  # se a opção for 4, ande para esquerda
            andar_esquerda()
            
if __name__ == "__main__":   # para iniciar na main
    main()
