import numpy as np
import random as ran

linha = 1
coluna = 1
opcoes = [1, 2, 3, 4]
passos = 0

matrix = np.array([
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", ".", ".", ".", ".", "#"],
    ["#", ".", "#", ".", "#", "#", "#"],
    ["#", ".", ".", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", ".", "#"],
    ["#", ".", ".", "T", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
])

def andar_baixo():
    global linha, coluna, opcoes, passos, matrix
    if matrix[linha + 1][coluna] != "#":
        matrix[linha][coluna] = "."
        linha += 1
        passos += 1
        
        if matrix[linha][coluna] == "T":
            print(f"Tesouro encontrado em {passos} passos")
            return
        else:
            print("Andando para baixo")
            matrix[linha][coluna] = "S"
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
    
def main():
    global linha, coluna, opcoes, passos, matrix
    while matrix[linha][coluna] != "T":
        escolhido = ran.choice(opcoes)
        
        if escolhido == 1:
            andar_baixo()
        if escolhido == 2:
            andar_cima()
        if escolhido == 3:
            andar_direita()
        if escolhido == 4:
            andar_esquerda()
            
if __name__ == "__main__":
    main()
