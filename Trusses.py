### Programa para resolver Armaduras Estáticamente Determinadas.

import numpy as np
import math

print('Programa para Resolver Armaduras determinadas')
print('Luis Jorge Chávez Cernas 6°C')
print(' ')
NJ = int(input('Numero de Juntas: '))
NM = int(input('Numero de Miembros: '))
NR = int(input('Numero de Componentes de Reaccion: '))
NF = int(input('Numero de Fuerzas: '))
IND = NM + NR - 2 * NJ

### Contadores
ContadorNodos = 1
ContadorMiembros = 0
ContadorReacciones = 0
ContadorFuerzas = 0

### Matrices
MatrizNodos = []


### Evitar Armaduras Indeterminadas
while (2 * NJ) != (NM + NR):
    print(' ')
    if IND>0:
        print ('Armadura Hiperestatica')
    if IND<0:
        print ('Armadura Hipoestatica')
    print('Estructura Estáticamente Indeterminada, Favor de Corregir')
    print(' ')
    
    NJ = input('Numero de Juntas: ')
    NM = input('Numero de Miembros: ')
    NR = input('Numero de Componentes de Reaccion: ')

matriz_A = np.zeros((2 * NJ, 2 * NJ)) 
matriz_B = np.zeros((2 * NJ, 1))


### Nodos
print(' ')
print('Favor de Introducir Coordenadas de Nodos')
print(' ')

while ContadorNodos <= NJ:
    print ('Nodo', ContadorNodos)
    X = input('Coordenada X: ')
    Y = input('Coordenada Y: ')
    print(' ')
    M = [X, Y]
    MatrizNodos.append(M)
    ContadorNodos = ContadorNodos + 1

print (MatrizNodos)

### Miembros [Falta]
print(' ')
print('Favor de Introducir Datos de Miembros')
print(' ')

while ContadorMiembros < NM:
    print('Barra'), ContadorMiembros + 1
    A = input('Nodo de Inicio de Miembro: ')
    A = A - 1
    B = input('Nodo de Termino de Miembro: ')
    B = B - 1
    print(' ')
    X1,Y1 = MatrizNodos[A]
    X2,Y2 = MatrizNodos[B]
    A = A * 2
    B = B * 2
    Dx = X2 - X1
    Dy = Y2 - Y1
    L = math.sqrt((Dx ** 2) + (Dy ** 2))
    Cx = Dx / L
    Cy = Dy / L
    matriz_A [A, ContadorMiembros] = (Cx * (-1))
    matriz_A [A + 1, ContadorMiembros] = (Cy * (-1))
    matriz_A [B, ContadorMiembros] = Cx
    matriz_A [B + 1, ContadorMiembros] = Cy

    ContadorMiembros = ContadorMiembros + 1



### Reacciones [Falta]
print(' ')
print('Favor de Introducir Datos de Reacciones')
print(' ')

while ContadorReacciones < NR:
    NumNodo = input('Numero de Nodo de Reaccion: ')
    NumNodo = ((NumNodo - 1) * 2)
    R = input('Direccion de Reaccion [X = 1, Y = 2]: ')
    NumNodo = NumNodo + (R - 1)
    matriz_A [NumNodo, ContadorReacciones + NM] = 1
    ContadorReacciones = ContadorReacciones + 1


### Fuerzas [Falta]
print(' ')
print('Favor de Introducir Datos de Fuerzas')
print(' ')
while ContadorFuerzas < NF:
    print('Fuerza ', ContadorFuerzas + 1)
    F = input('Magnitud de Fuerza: ')
    NFuerza = input('Nodo Donde se Encuentra: ')
    NFuerza = ((NFuerza - 1) * 2)
    R = input('Direccion de Fuerza [X = 1, Y = 2]: ')
    NFuerza = NFuerza + (R - 1)
    matriz_B [NFuerza, 0] = (F * (-1))
    ContadorFuerzas = ContadorFuerzas + 1
    

print ('Las fuerzas se muestran en orden decendente [F1, F2, ...]')
print ('Las reacciones inician donde terminan las fuerzas')
print ('Fuerza Negativa = Tension')
print ('Fuerza Positiva = Compresion')
### Matriz
matriz_Q = np.linalg.solve (matriz_A, matriz_B)

print (' ')
print (matriz_Q)



