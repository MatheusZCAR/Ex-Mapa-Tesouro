import numpy as np

linha = 1   # tem que deixar a variável global
coluna = 1
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


def andar_pra_baixo():
    matrix[linha][coluna] = "."   # substitui a casa atual onde S está por uma casa vaga
    linha += 1
    print("Caminhou uma casa pra baixo")
    passos += 1
    print(f"Total de passos: {passos}")
    if matrix[linha][coluna] == "T":      # se a casa vaga na verdade for o Tesouro, avisar que o tesouro foi encontrado
            print("Tesouro encontrado!")
            return("T")
    else:
        matrix[linha][coluna] = "S"    # move S para a casa que estava vaga antes
    return

def andar_pra_cima():
    matrix[linha][coluna] = "."
    linha -= 1
    print("Caminhou uma casa pra cima")
    passos += 1
    print(f"Total de passos: {passos}")
    if matrix[linha][coluna] == "T":
            print("Tesouro encontrado!")
            return("T")
    else:
        matrix[linha][coluna] = "S"
    return

def andar_pra_direita():
    matrix[linha][coluna] = "."
    coluna += 1
    print("Caminhou uma casa pra direita")
    passos += 1
    print(f"Total de passos: {passos}")
    if matrix[linha][coluna] == "T":
            print("Tesouro encontrado!")
            return("T")
    else:
        matrix[linha][coluna] = "S"
    return

def andar_pra_esquerda():
    matrix[linha][coluna] = "."
    coluna -= 1
    print("Caminhou uma casa pra esquerda")
    passos += 1
    print(f"Total de passos: {passos}")
    if matrix[linha][coluna] == "T":
            print("Tesouro encontrado!")
            return("T")
    else:
        matrix[linha][coluna] = "S"
    return




'''
    while matrix[linha][coluna] != "T":
    
    if matrix[linha + 1][coluna] == "." or matrix[linha + 1][coluna] == "T":  # andar pra baixo
        andar_pra_baixo()
    
    if matrix[linha - 1][coluna] == "." or matrix[linha - 1][coluna] == "T": # andar pra cima
        
        if matrix[linha + 1][coluna] == "." or matrix[linha + 1][coluna] == "T":    # verifica se dá pra andar mais pra baixo
            andar_pra_baixo()
        
        else:
            
        
    
    elif matrix[linha][coluna + 1] == "." or matrix[linha][coluna + 1] == "T":
        coluna += 1
        print("Caminhou uma casa para direita")
        passos += 1
        andouDireita = 1
        print(f"Total de passos: {passos}")
        
        if matrix[linha][coluna] == "T":
            print("Tesouro encontrado!") 
    
    elif matrix[linha][coluna - 1] == "." or matrix[linha][coluna - 1] == "T":
        coluna -= 1
        print("Caminhou uma casa para esquerda")
        passos += 1
        andouDireita = 0
    


    
    
    
    
    
    
    
    

    if matrix[linha][coluna] == "T":
        print("Tesouro encontrado!")
        break
    elif matrix[linha][coluna] == "#":
        if(verificador == 0):
            print("Parede encontrada!")
            linha -= 1
            coluna += 1
            verificador = 1
        else:
            linha += 1
            coluna -= 1
            verificador = 0
    else:
        print("Caminhando...")
        linha += 1
'''