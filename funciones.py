import numpy as np
import pandas as pd


def restarFil(A,inicio,destino):
    aux = np.copy(A[inicio])
    A[inicio] = A[destino]
    A[destino] = aux
    
## pre: array no vacío de números decimales
## pos: devuelve la posicion a partir de 'inicioBusqueda' en la que se encuentra el maximo elemento en valor abs. de la columna
def pivotPos(col,inicioBusqueda):
    max=0
    pos=0
    for i in range(inicioBusqueda, col.size):
        if np.abs(col[i]) > max:
            max = np.abs(col[i])
            pos = i
    return pos
#pre: matriz cuadrada no nula
#pos: Devuelve copia de A con fila i  y j permutadas
def permutarFil(A,i,j):
    aux = np.copy(A[i])
    A[i] = A[j]
    A[j] = aux

## pre: Matriz A no nula de numeros reales
## pos: Devuelve matriz  triangulada junto con la Matriz de permutaciones que se requirieron en la triangulación. Si la matriz NO es cuadrada o no un pivot resulta 0 retorna None.

def calcularLU(A):
    if(A.shape[0] != A.shape[1]): return None
    U = np.copy(A)
    L = []
    P = [[1,0,0],[0,1,0],[0,0,1]]
    for j in range(0, U.shape[1]):
        ## pivoteo
        colj = U[:,j]
        pivot = pivotPos(colj,j)
        ## pivot es 0 y ninguna permutación puede arreglar eso
        if U[j,j] == 0 and j == U.shape[0]-1: return None
        ## permutar si pivot no esta en la posicion adecuada
        if pivot != j :
            permutarFil(U,j,pivot)
            ## Agregar la permutacion a la matriz de permutaciones P
            permutarFil(P,j,pivot)

        ## despejar debajo de col de pivot
        for i in range(j+1, U.shape[1]):
            if U[i,j] != 0:
                coeficiente = U[i,j] / U[j,j]
                U[j,:] = coeficiente * U[j,:]
        ## resto fila i - fila pivot y hago un cero debajo de pivot, sigo con la prox. fila debajo
                U[i,:] = U[i,:] - U[j,:]
        ##encontrarL
    return L, U, P


def inversaLU(L, U, P=None):
    Inv = []
    # su código
    
    ###########
    return Inv

def main():
    T = pd.read_csv('T.csv', header=None).values
    print(calcularLU(T))

if __name__ == "__main__":
    main()

