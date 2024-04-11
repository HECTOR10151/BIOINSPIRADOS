import random
import matplotlib.pyplot as plt
import numpy as np
import math
def fn1(x):
    return x*x
def fn2(x):
    return x - 5/2 + np.sin(x)
def fn3(x):
    return 2*x+1
def binario(x):
    bin,i=0,1
    while (n>0):
        bin+=i*(n%2)
        n//=2
        i*=10
    return bin
if __name__ == '__main__':
    
    tam=int(input('Ingrese el tamaño del arreglo: '))
    min=int(input('Ingrese el valor mínimo: '))
    max=int(input('Ingrese el valor máximo: '))
    arr=[random.randint(min,max) for i in range(tam)]#bucle de numero aleatorios con los rangos
    arr.sort()#ordenar el arreglo
    maxi=arr[-1]#el maximo encontrado
    mini=arr[0]#el minimo encontrado
    print("Arreglo ordenado y en decimal:",end="")
    for num in arr:
        print("[{}]".format(num),end=" ")#imprimir el arreglo
    print("\nValor maximo",max)#imprimir el valor maximo
    print("1.- Funcion x^2")
    print("2.- Funcion x-5/2+sin(x)")
    print("3.- Funcion 2x+1")
    e=int(input('Ingresa el numero de  la funcion a utilizar por favor: '))
    if e == 1:
        print("\n\tHistograma de fn1 es: f(x)=x^2\n")
        plt.plot(arr, fn1(np.array(arr)))
        plt.xlabel('Valores del arreglo')#nombre del eje x
        plt.ylabel('Valores de la función')#nombre del eje y
        plt.title('Histograma de fn1: f(x)=x*x')#titulo del histograma
        plt.grid(True)#cuadricula activada
        plt.show()#mostrar el histograma
    elif e == 2:
        print("\n\tHistograma de fn2 es f(x)=(x - 5.0 / 2.0 + sin(x))\n")
        plt.plot(arr, fn2(np.array(arr)))
        plt.xlabel('Valores del arreglo')
        plt.ylabel('Valores de la función')
        plt.title('Histograma de fn1: x-5/2+sin(x)')
        plt.grid(True)
        plt.show()
    elif e == 3:
        print("\n\tHistograma de fn3 es f(x)=(3 * n) - 5\n")
        plt.plot(arr, fn3(np.array(arr)))
        plt.xlabel('Valores del arreglo')
        plt.ylabel('Valores de la función')
        plt.title('Histograma de fn1: f(x)=(3 * n) - 5')
        plt.grid(True)
        plt.show()