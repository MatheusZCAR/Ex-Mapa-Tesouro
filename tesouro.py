import numpy as np

matrix = np.array([
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", ".", ".", ".", ".", "#"],
    ["#", ".", "#", ".", "#", "#", "#"],
    ["#", ".", ".", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", ".", "#"],
    ["#", ".", ".", "T", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
])


baixo = 1
direita = 1
verificador = 0


while matrix[baixo][direita]:
    if matrix[baixo][direita] == "T":
        print("Tesouro encontrado!")
        break
    elif matrix[baixo][direita] == "#":
        if(verificador == 0):
            print("Parede encontrada!")
            baixo -= 1
            direita += 1
            verificador = 1
        else:
            baixo += 1
            direita -= 1
            verificador = 0
    else:
        print("Caminhando...")
        baixo += 1
