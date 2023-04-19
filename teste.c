#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

double mochila_fracionaria(int n, int* weights, int* values, int capacity) {
    int i;
    double total_value = 0.0;
    double* ratios = (double*) malloc(sizeof(double) * n);

    for (i = 0; i < n; i++) {
        ratios[i] = (double) values[i] / (double) weights[i];
    }

    while (capacity > 0) {
        int best_item = -1;
        double best_ratio = -1.0;

        for (i = 0; i < n; i++) {
            if (weights[i] > 0 && ratios[i] > best_ratio) {
                best_ratio = ratios[i];
                best_item = i;
            }
        }

        if (best_item == -1) {
            break;
        }

        if (weights[best_item] <= capacity) {
            total_value += (double) values[best_item];
            capacity -= weights[best_item];
            weights[best_item] = 0;
        } else {
            total_value += best_ratio * capacity;
            weights[best_item] -= capacity;
            capacity = 0;
        }
    }

    free(ratios);
    return total_value;
}

int main() {
    setlocale(LC_ALL, "Portuguese");
    int n, capacity, i;
    int* weights, *values;
    double avg_time;
    clock_t start, end;

    printf("Insira o número de itens: ");
    scanf("%d", &n);

    weights = (int*) malloc(sizeof(int) * n);
    values = (int*) malloc(sizeof(int) * n);

    printf("Insira os pesos dos itens, separados por espaço: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &weights[i]);
    }

    printf("Insira os valores dos itens, separados por espaço: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &values[i]);
    }

    printf("Insira a capacidade da mochila: ");
    scanf("%d", &capacity);

    start = clock();
    printf("Valor máximo da mochila: %.2lf\n", mochila_fracionaria(n, weights, values, capacity));
    end = clock();

    avg_time = (double) (end - start) / CLOCKS_PER_SEC;
    printf("Tempo de execução da função: %.6lf segundos\n", avg_time);

    free(weights);
    free(values);

    return 0;
}
