#!/usr/bin/env python

import sys
import random
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(lista):
    n_pasos = 0
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j-1] > lista[j]:
            lista[j-1], lista[j] = lista[j], lista[j-1]
            j -= 1
            n_pasos += 1
    return (lista, n_pasos)

def random_list(n):
    return random.sample(range(1,n*n),n)

def test(n=1, tamaño=20):
    results = []
    for i in range(0,n):
        lista = random_list(tamaño)
        ordenada = insertion_sort(lista)
        results.append(ordenada[-1])
    return results


def main(n=1, t=20):
    l = test(n, t)
    nl = np.asarray(l)
    mu, sigma = 100, 15
    x = nl
    hist, bins = np.histogram(x, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.show()

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        main(int(sys.argv[1]))
    elif (len(sys.argv) == 3):
        main(int(sys.argv[1]), int(sys.argv[2]))
    if (len(sys.argv) == 1):
        main()

    
    
