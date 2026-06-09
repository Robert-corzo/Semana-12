def imprimir(mat):
    for f in mat:
        print(f)
    print()

def validar(lab, f, c, res):
    # Verificar límites
    if f < 0 or f >= len(lab) or c < 0 or c >= len(lab[0]):
        return False
    # Verificar si es pared (0) o ya visitada (1)
    if lab[f][c] == 0 or res[f][c] == 1:
        return False
    return True

def laberinto(lab, res, f, c, fin_f, fin_c):
    # Caso base: Llegamos a la meta
    if f == fin_f and c == fin_c:
        res[f][c] = 1
        imprimir(res)
        return True

    if validar(lab, f, c, res):
        res[f][c] = 1
        imprimir(res) # Muestra el avance
        
        # Intentar las 4 direcciones: Abajo, Derecha, Arriba, Izquierda
        movimientos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for df, dc in movimientos:
            if laberinto(lab, res, f + df, c + dc, fin_f, fin_c):
                return True
        
        # Backtracking: Si no funcionó, marcamos como 0 y mostramos el retroceso
        res[f][c] = 0
        imprimir(res)
        return False
    
    return False

# Matriz basada en tu imagen
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

# Inicio (0,0), Fin (8,8)
if laberinto(lab, res, 0, 0, 8, 8):
    print("¡Ruta encontrada!")
else:
    print("SIN salida")