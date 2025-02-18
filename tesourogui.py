import numpy as np
import random as ran
import tkinter as tk
from tkinter import ttk


tamanho_celula = 50
linha, coluna = 1, 1
opcoes = [1, 2, 3, 4]
passos = 0

def exibir_mensagem():
    msg_root = tk.Toplevel()
    msg_root.title("Fim do Jogo")
    label = tk.Label(msg_root, text=f"Tesouro encontrado!\nPassos: {passos}", font=("Arial", 14))
    label.pack(pady=20)
    ttk.Button(msg_root, text="Fechar", command=root.quit).pack(pady=10)

matrix = np.array([
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", ".", ".", ".", ".", "#"],
    ["#", ".", "#", ".", "#", "#", "#"],
    ["#", ".", ".", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", ".", "#"],
    ["#", ".", ".", "T", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
])

# Criando a janela do Tkinter
root = tk.Tk()
root.title("Mapa do Tesouro")
canvas = tk.Canvas(root, width=len(matrix[0]) * tamanho_celula, height=len(matrix) * tamanho_celula)
canvas.pack()

# Função para desenhar o labirinto
def desenhar_labirinto():
    canvas.delete("all")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cor = "white"
            if matrix[i][j] == "#":
                cor = "black"
            elif matrix[i][j] == "S":
                cor = "blue"
            elif matrix[i][j] == "T":
                cor = "gold"
            canvas.create_rectangle(j * tamanho_celula, i * tamanho_celula,
                                    (j + 1) * tamanho_celula, (i + 1) * tamanho_celula, fill=cor, outline="gray")

def mover_personagem(direcao):
    global linha, coluna, passos
    nova_linha, nova_coluna = linha, coluna
    
    if direcao == "baixo" and matrix[linha + 1][coluna] != "#":
        nova_linha += 1
    elif direcao == "cima" and matrix[linha - 1][coluna] != "#":
        nova_linha -= 1
    elif direcao == "direita" and matrix[linha][coluna + 1] != "#":
        nova_coluna += 1
    elif direcao == "esquerda" and matrix[linha][coluna - 1] != "#":
        nova_coluna -= 1
    
    if (nova_linha, nova_coluna) != (linha, coluna):
        matrix[linha][coluna] = "."
        linha, coluna = nova_linha, nova_coluna
        passos += 1
        
        if matrix[linha][coluna] == "T":
            matrix[linha][coluna] = "S"
            desenhar_labirinto()
            exibir_mensagem()
            return
        
        matrix[linha][coluna] = "S"
    
    desenhar_labirinto()
    root.after(100, mover_aleatorio)

def mover_aleatorio():
    if matrix[linha][coluna] != "T":
        escolhido = ran.choice(opcoes)
        if escolhido == 1:
            mover_personagem("baixo")
        elif escolhido == 2:
            mover_personagem("cima")
        elif escolhido == 3:
            mover_personagem("direita")
        elif escolhido == 4:
            mover_personagem("esquerda")

desenhar_labirinto()
root.after(100, mover_aleatorio)

# Botão para sair
ttk.Button(root, text="Sair", command=root.quit).pack()

root.mainloop()
