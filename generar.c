#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double fn1(double x);
double fn2(double x);
double fn3(double x);
int binario(int n);
void grafico(double (*func)(double), int *arr, int tam);

int main(int argc, char *argv[]) {
    int tam, min, max, i, j, temp, maxVal;
    int *arr, *bin;

    if (argc == 4) {
        tam = atoi(argv[1]);
        min = atoi(argv[2]);
        max = atoi(argv[3]);
    } else {
        printf("Ingrese el tamaño del arreglo: ");
        scanf("%d", &tam);
        printf("Ingrese el rango mínimo: ");
        scanf("%d", &min);
        printf("Ingrese el rango máximo: ");
        scanf("%d", &max);
    }
    arr = (int*) malloc(tam * sizeof(int));
    bin = (int*) malloc(tam * sizeof(int));
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

    printf("Arreglo ordenado y en decimal: ");
    for(i = 0; i < tam; i++) {
        printf("[%d] ", arr[i]);
        bin[i] = binario(arr[i]);
    }
    printf("\nValor máximo: %d\n", maxVal);
    printf("Arreglo ordenado y en binario: ");
    for(i = 0; i < tam; i++) {
        printf("[%d] ", bin[i]);
    }
    printf("\nValor máximo: %d\n", bin[tam-1]);

    int e;
    printf("\nIngrese el número de la función a utilizar:\n");
    printf("1. f(x) = x * x\n");
    printf("2. f(x) = (x - 5.0 / 2.0 + sin(x))\n");
    printf("3. f(x) = (3 * n) - 5\n");
    scanf("%d", &e);
    switch (e){
    case 1:
        printf("\n\tHistograma de fn1 es: f(x)=x*x\n");
        grafico(fn1, arr, tam);
        break;
    case 2:
        printf("\n\tHistograma de fn2 es f(x)=(x - 5.0 / 2.0 + sin(x))\n");
        grafico(fn2, arr, tam); 
        break;
    case 3: 
        printf("\n\tHistograma de fn3 es f(x)=(3 * n) - 5\n");
        grafico(fn3, arr, tam);
        break;
    default:
        break;
    }
    free(arr);
    free(bin);
    return 0;
}

double fn1(double x) {
    return x * x;
}

double fn2(double x) {
    return (x - 5.0 / 2.0 + sin(x));
}

double fn3(double x) {
    return (3 * x) - 5;
}

int binario(int n) {
    int bin = 0, i = 1;
    while(n > 0) {
        bin += (n % 2) * i;
        n /= 2;
        i *= 10;
    }
    return bin;
}

void grafico(double (*func)(double), int *arr, int tam) {
    int i, j;
    for(i = 0; i < tam; i++) {
        double result = func(arr[i]);
        printf("%3.0f | ", result);
        for(j = 0; j < (int) result; j++) {
            printf("*");
        }
        printf("\n");
    }
}
