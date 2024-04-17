import random
import matplotlib.pyplot as plt
import numpy as np
import math

def fn1(x):
    return x*x

def fn2(x):
    return (x - 5.0) / (2.0 + np.sin(x))

def fn3(x):
    return 2*x + 1

def binario(x):
    bin, i = 0, 1
    while (x > 0):
        bin += i*(x%2)
        x //= 2
        i *= 10
    return bin

if __name__ == '__main__':
    tam = int(input('Ingrese el tamaño del arreglo: '))
    min_val = int(input('Ingrese el valor mínimo: '))
    max_val = int(input('Ingrese el valor máximo: '))
    arr = [random.randint(min_val, max_val) for _ in range(tam)]
    arr.sort()
    bin = [binario(num) for num in arr]
    print("Arreglo ordenado y en decimal:", end="")
    for num in arr:
        print("[{}]".format(num), end=" ")
    print("\n")
    print("Arreglo ordenado y en BINARIO:", end="")
    for num in bin:
        print("[{}]".format(num), end=" ")  
    print("\nValor máximo", max_val)
    print("1.- Funcion x^2")
    print("2.- Funcion x-5/2+sin(x)")
    print("3.- Funcion 2x+1")
    e = int(input('Ingresa el número de la función a utilizar por favor: '))

    # Solicitar al usuario si desea maximizar o minimizar
    opcion = input("¿Desea maximizar (M) o minimizar (m) la función? ")
    if e == 1:
        fn = fn1
    elif e == 2:
        fn = fn2
    elif e == 3:
        fn = fn3
    else:
        print("Opción no válida.")
        exit()

    arr_fn = fn(np.array(arr))
    if opcion.lower() == 'm':
        punto = arr[np.argmin(arr_fn)]
        valor = np.min(arr_fn)
        label = f'Mínimo en x={punto}'
    elif opcion.lower() == 'M':
        punto = arr[np.argmax(arr_fn)]
        valor = np.max(arr_fn)
        label = f'Máximo en x={punto}'
    else:
        print("Opción no válida.")
        exit()

    plt.plot(arr, arr_fn)
    plt.scatter(punto, valor, color='red', label=label)
    plt.xlabel('Valores del arreglo')
    plt.ylabel('Valores de la función')
    plt.title(f'Histograma de fn{e}')
    plt.legend()
    plt.grid(True)
    plt.show()