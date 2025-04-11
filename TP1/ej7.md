# EJ 7

La heurística elegida para ejercicio 7 consiste en dividir el tablero en cuadriculas no superponibles(en el código son 16 cuadriculas, pero puede ser cualquier potencia de 2). En esta division posiblemente halla cuadriculas que no tengan pastillas y otras que si. A la hora de calcular la heurística, se calcula el largo del mínimo camino que visita todas las cuadriculas que tienen pastillas.

Esta heurística surgió de la idea de generalizar el problema de visitar las 4 esquinas del tablero al problema de comer todas las pastillas. En este caso cada cuadricula representa una "esquina" a visitar, solo que las cuadriculas ocupan mas espacio.

Para mejorar la heurística, se restringe el tamaño de las cuadriculas para que haya al menos dos esquinas opuestas que tengan pastillas. Además algunos resultados pueden calcularse más de una vez por lo que se memorizan los resultados y calculados para mejorar la velocidad de computo(a costa de usar mas memoria). La heurística se acerca mas a la solución real a medida que se aumentan las cuadriculas, pero también aumenta el tiempo de computo y la memoria utilizada.

Por ejemplo para el layout trickySearch, el laberinto se divide en 16 cuadriculas.

![alt text](<Captura desde 2025-04-09 20-07-23.png>)

Si se eliminan las cuadriculas sin pastillas y se restringe el tamaño de las cuadriculas restantes, entonces solo quedan 4 cuadriculas.

![alt text](image.png)

El mínimo camino que visita todas las cuadriculas consta de 17 pasos, mientras
que el costo real de comer todas las pastillas es de 60 pasos. Usando esta
heurística el agente encuentra la solución en aproximadamente 0.8 segundos
explorando 9086 nodos.

La heurística es admisible porque un recorrido que tiene que comer todas las
pastillas como mínimo tiene que visitar todas las cuadriculas(y siempre donde
hay una cuadricula hay por lo menos 1 pastilla). Además es consistente porque en cada paso la distancia a la solución varia en solo 1 paso.