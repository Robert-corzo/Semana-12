def imprimir(mat):
    for f in mat:
        print(f)
    print()

def validar(lab, f, c, res):
    if f < 0 or f >= len(lab):        
        return False
    if c < 0 or c >= len(lab[0]):     
        return False
    if lab[f][c] == 0:
        return False
    if res[f][c] == 1:
        return False
    return True


def laberinto(lab, res, f, c ):
    if f == len(lab)-1 and c == len(lab[0])-1:
        if lab[f][c] == 1:
            res[f][c] = 1
            imprimir(res)
            return True
        else:
            return False
    else:
        if validar(lab, f, c, res):
            res[f][c] = 1
            imprimir(res)

            if laberinto(lab, res, f+1, c ):#Abajo
                return True
            elif laberinto(lab, res, f, c+1 ): #Derecha
                return True
            elif laberinto(lab, res, f, c-1 ):#Izquierda
                return True
            elif laberinto(lab, res, f-1, c ):#Arriba
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False


lab = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1]

]
res = [[0 for _ in range(9)] for _ in range(9)]

if laberinto(lab, res, 0, 0 ):
    print("Escapamos")
else:
    print("SIN salida")