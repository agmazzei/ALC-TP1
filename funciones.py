import numpy as np
import pandas as pd



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
#pos: Devuelve copia de A con fila inicio  y destino permutadas
def permutarFil(A,inicio,destino):

    Acpy = np.copy(A)
    aux = np.copy(Acpy[inicio])
    Acpy[inicio] = Acpy[destino]
    Acpy[destino] = aux
    return Acpy

def calcularLU(A):
    Acpy = np.copy(A)
    L, U = [],[]
    P = [[1,0,0],[0,1,0],[0,0,1]]
    I = P
    for j in range(0, Acpy.shape[1]):
        
        ## encontrar pivot
        colj = Acpy[:,j]
        pivot = pivotPos(colj,j)
        ## pivot es 0 no se puede hacer LU
        if Acpy[pivot,j] == 0: return
        ## permutar si pivot no esta en la posicion adecuada
        if pivot != j :
            Acpy = permutarFil(Acpy,j,pivot)
            P = np.matmul(permutarFil(P,j,pivot),P)
            ## Agregar la permutacion a la matriz de permutaciones P

        ## despejar debajo de col de pivot
        for i in range(j+1, Acpy.shape[1]):
            if Acpy[i,j] != 0:
                coeficiente = Acpy[i,j] / Acpy[j,j]
                Acpy[j,:] = coeficiente * Acpy[j,:]
        ## resto fila i - fila pivot y hago un cero debajo de pivot, sigo con la prox. fila debajo
                Acpy[i,:] = Acpy[i,:] - Acpy[j,:]
        ##calcularLUsinPermutaciones(PA,L,U)
    return L, U, P


def inversaLU(L, U, P=None):
    Inv = []
    # su código
    
    ###########
    return Inv

def main():
    T = pd.read_csv('T.csv', header=None).values
    calcularLU(T)

if __name__ == "__main__":
    main()

