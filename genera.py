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

def gray_code(n):
    binary = bin(n ^ (n >> 1))[2:]
    return binary.zfill(len(bin(n)) - 2) 

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
    
    binario_arr = [binario(num) for num in arr]
    
    print("Arreglo ordenado y en decimal:", arr)
    print("Arreglo ordenado y en BINARIO:", binario_arr)
    
    gray_arr = [gray_code(num) for num in arr]
    print("Arreglo en código Gray:")
    for gray_num in gray_arr:
        print("[{}]".format(gray_num), end=" ")

    print("\nValor máximo", max_val)
    
    num_individuos = int(input('¿Cuántos individuos desea graficar? '))
    
    arr = arr[:num_individuos]
    
    opcion = input("¿Desea maximizar (M) o minimizar (m) la función? ")

    if opcion == 'm' or opcion == 'M':
        print("1.- Funcion x^2")
        print("2.- Funcion x-5/2+sin(x)")
        print("3.- Funcion 2x+1")
        e = int(input('Ingresa el número de la función a utilizar por favor: '))

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
        plt.plot(arr, arr_fn)
        
        if opcion == 'm':
            punto_min = arr[np.argmin(arr_fn)]
            valor_min = np.min(arr_fn)
            label_min = f'Mínimo en x={punto_min}'
            plt.text(punto_min, valor_min, f'({punto_min}, {valor_min})', fontsize=10, ha='right')
            plt.scatter(punto_min, valor_min, color='red', label=label_min)
        else: 
            punto_max = arr[np.argmax(arr_fn)]
            valor_max = np.max(arr_fn)
            label_max = f'Máximo en x={punto_max}'
            plt.text(punto_max, valor_max, f'({punto_max}, {valor_max})', fontsize=10, ha='right')
            plt.scatter(punto_max, valor_max, color='blue', label=label_max)
        
        plt.xlabel('Valores del arreglo')
        plt.ylabel('Valores de la función')
        plt.title(f'Histograma de fn{e}')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Opción no válida.")
