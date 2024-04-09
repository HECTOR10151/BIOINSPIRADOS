#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
    int tam, min, max, i, j, temp, maxVal;
    int *arr;
    printf("Ingrese el tamaño del arreglo: ");
    scanf("%d", &tam);
    printf("Ingrese el rango mínimo: ");
    scanf("%d", &min);
    printf("Ingrese el rango máximo: ");
    scanf("%d", &max);
    arr = (int*) malloc(tam * sizeof(int));
    srand(time(0));
    for(i = 0; i < tam; i++) {
        arr[i] = (rand() % (max - min + 1)) + min;
    }
    for(i = 0; i < tam-1; i++) {
        for(j = 0; j < tam-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    maxVal = arr[tam-1];
    printf("Arreglo ordenado: ");
    for(i = 0; i < tam; i++) {
        printf("%d ", arr[i]);
    }
    printf("\nValor máximo: %d\n", maxVal);
    return 0;
}