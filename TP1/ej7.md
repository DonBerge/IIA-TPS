La heuristica elegida para ejercicio 7 consiste en dividir el tablero en cuadriculas no superponibles(en el codigo son 16 cuadriculas). En esta division posiblemente halla cuadriculas que no tengan pastillas y otras que si. A la hora de calcular la heuristica, se calcula el largo del minimo camino que visita todas las cuadriculas que tienen pastillas + la cantidad de pastillas restantes del tablero.

Esta heuristica surgio de la idea de generalizar el problema de visitar las 4 esquinas del tablero al problema de comer todas las pastillas. En este caso cada cuadricula representa una "esquina" a visitar, solo que las cuadriculas ocupan mas espacio.


![alt text](image.png)

*Ejemplo de division del tablero "trickySearch" en 16 cuadriculas, las cuadriculas que no tienen pastillas se ocultaron. En este caso, un camino optimo consiste en visitar la cuadricula azul, luego la roja, luego la verde y por ultimo la naranja con un costo de 12. El costo minimo para resolver el laberinto es de 60.*

En el layout "trickySearch", el laberinto se divide en 16 segmentos de los cuales solo 4 tienen pastillas. El agente encuentra la solución en aproximadamente 2.15 segundos explorando 7527 nodos.

## Explicacion de consistencia
La heuristica es consistente si:

$$h(n) \leq 1 + h(n')$$

Para cualquier estado $n$ y para cualquier sucesor $n'$

Suponiendo que se esta en un estado $n$ y se pasa a un sucesor $n'$ con $h(n)>h(n')$,
entonces pudieron pasar 3 cosas.

1. Se dio un paso que pertence a un posible camino optimo que visita todas las cuadriculas.
2. Se comio una pastilla.
3. Las 2 anteriories a la vez.

Si pasa 1, entonces $h(n)$ y $h(n')$ difieren en una unidad por lo que se mantiene la consistencia.

Si pasa 2, entonces el numero de pastillas disminuye en 1 y la consistencia se mantiene. Si la cuadricula donde esta la pastilla desaparece(porque se comieron todas las pastillas de la cuadricula)