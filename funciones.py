import numpy as np
import pandas as pd


## pre: array no vacío de números decimales
## pos: devuelve la posicion a partir de 'inicioBusqueda' en la que se encuentra el maximo elemento en valor abs. de la columna
def maxCol(col,inicioBusqueda):
    max,pos=0,0
    
    for i in range(inicioBusqueda, col.size):
        if np.abs(col[i]) > max:
            max = np.abs(col[i])
            pos = i
    return pos
#pre: matriz no nula
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
    L = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
    P = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
    for j in range(0, U.shape[1]):
        ## pivoteo
        colj = U[:,j]
        posMax = maxCol(colj,j)
        ## pivot es 0 y ninguna permutación puede arreglar eso
        if U[j,posMax] == 0: return None
        ## permutar si pivot no esta en la posicion adecuada
        if posMax != j :
            permutarFil(U,j,posMax)
            ## Agregar la permutacion a la matriz de permutaciones P
            permutarFil(P,j,posMax)

        ## despejar debajo de col de pivot
        filas = U.shape[0]
        for i in range(j+1, filas):
            if U[i,j] != 0:
                filParaTriangular = (U[i,j] / U[j,j]) * U[j,:]
        ## resto fila i - fila pivot y hago un cero debajo de pivot, sigo con la prox. fila debajo
                U[i,:] = U[i,:] - filParaTriangular
                
        
##encontrarL
    ##calculo PA
    columnasU = U.shape[1]
    filasL = U.shape[1]
    PA = np.matmul(P,A)
    
        ## calculo L elemento a elemento de L
    for k in range(0, columnasU):
        for m in range(0, filasL):
            filL = np.copy(L[m,:])
            colU = np.copy(U[:,k])
            filL[k] = 0.0
            L[m,k] = (PA[m,k] - (filL @ colU)) / U[k,k]
        
    return L, U, P


def inversaLU(L, U, P=None):
    Inv = []

    return Inv

def main():
    T = pd.read_csv('T.csv', header=None).values


if __name__ == "__main__":
    main()

