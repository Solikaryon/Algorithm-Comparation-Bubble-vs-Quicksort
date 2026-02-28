#!/usr/bin/env python3
#coding: utf-8
# Created on Thu Nov 9 16:25:29 2023
# @author: Monjaraz Briseño Luis Fernando 

import numpy as np
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as manimation

# Configuración de semillas para reproducibilidad
random.seed(10)
np.random.seed(10)

def Burbuja(lista):
    """Implementación del algoritmo Burbuja con contador de iteraciones."""
    n = len(lista)
    iterations = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            iterations += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return iterations

def Quicksort(lista):
    """Implementación recursiva de Quicksort con contador de iteraciones."""
    if len(lista) <= 1:
        return lista, 0
    else:
        pv = lista[0]
        # Particionado
        m = [x for x in lista[1:] if x <= pv]
        ma = [x for x in lista[1:] if x > pv]
        
        rm, iterations_m = Quicksort(m)
        rma, iterations_ma = Quicksort(ma)
        
        iterations_total = iterations_m + iterations_ma + (len(lista) - 1)
        return rm + [pv] + rma, iterations_total

# Configuración de los tamaños de los arreglos para la prueba
elementNumArray = [100, 200, 400, 800, 1600, 3200, 6400, 12800]

iteracionesBurbuja = []
iteracionesQuicksort = []
tiemposBurbuja = []
tiemposQuicksort = []

# Configuración del escritor de video (FFMPEG)
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Burbuja Vs Quicksort Analysis', 
                artist='Monjaraz Briseño Luis Fernando',
                comment='Análisis de complejidad algorítmica')
writer = FFMpegWriter(fps=24, metadata=metadata)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
ax1.title.set_text('Burbuja')
ax2.title.set_text('Quicksort')
ax1.set_ylabel("Iteraciones")
ax1.set_xlabel("# Elementos")
ax2.set_xlabel("# Elementos")

# Nombre del archivo de salida para la animación
output_file = "MonjarazBriseñoLuisFernando_Tarea11_BurbujaVsQuicksort.mp4"

with writer.saving(fig, output_file, 100):
    plt.ion()
    for idx, elementNum in enumerate(elementNumArray):
        # Generar lista aleatoria
        lista = np.random.randint(0, 100000, elementNum).tolist()
        
        # Medición de Burbuja
        start_burbuja = time.time()
        iterations_burbuja = Burbuja(lista.copy())
        finish_burbuja = time.time()
        
        # Medición de Quicksort
        start_quicksort = time.time()
        _, iterations_quicksort = Quicksort(lista.copy())
        finish_quicksort = time.time()
        
        # Almacenar resultados
        iteracionesBurbuja.append(iterations_burbuja)
        iteracionesQuicksort.append(iterations_quicksort)
        
        # Actualización de gráficas
        ax1.plot(elementNumArray[:idx+1], iteracionesBurbuja, 'r', label='Burbuja')
        ax2.plot(elementNumArray[:idx+1], iteracionesQuicksort, 'b', label='Quicksort')
        
        # Etiquetas de tiempo en la gráfica
        ax1.text(elementNum, iterations_burbuja, f" {finish_burbuja - start_burbuja:.6f}s", 
                 color='black', ha='left', va='center')
        ax2.text(elementNum, iterations_quicksort, f" {finish_quicksort - start_quicksort:.6f}s", 
                 color='black', ha='left', va='center')
        
        # Salida en terminal
        print(f"Iteraciones (Burbuja) para {elementNum} elementos: {iterations_burbuja}")
        print(f"Tiempo (Burbuja): {finish_burbuja - start_burbuja:.6f}s")
        print(f"Iteraciones (Quicksort) para {elementNum} elementos: {iterations_quicksort}")
        print(f"Tiempo (Quicksort): {finish_quicksort - start_quicksort:.6f}s\n")
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        # Grabar frames para la animación
        for i in range(24):
            writer.grab_frame()

plt.ioff()
plt.show()