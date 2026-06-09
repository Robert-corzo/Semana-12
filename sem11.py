def imprimir(mat):
    for f in mat:
        print(f)
    print()

def validar(lab, f, c):
    if f >= len(lab[0]):
        return False
    if c >= len(lab):
        return False
    if lab[f][c] == 0:
        return False
    return True


def laberinto(lab, res, f, c ):
    if f == len(lab[0]) - 1 and c == len(lab) - 1:
        if lab[f][c] == 1:
            res[f][c] = 1
            imprimir(res)
            return True
        else:
            return False
    else:
        if validar(lab, f, c):
            res[f][c] = 1
            imprimir(res)
            if laberinto(lab, res, f, c+1 ):
                return True
            elif laberinto(lab, res, f+1, c ):
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False


lab = [
    [1,0,0,0],
    [1,1,1,1],
    [0,1,0,0],
    [1,1,1,0]
]
res = [[0 for _ in range(4)] for _ in range(4)]

if laberinto(lab, res, 0, 0 ):
    print("Escapamos")
else:
    print("SIN salida")