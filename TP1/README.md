Resolucion de los laberintos de esquinas con bfs:

tinyCorners: 28 pasos en 0 segundos expandiendo 252 nodos
mediumCorners: 106 pasos en 0 segundos expandiendo 1966 nodos
bigCorners: 162 pasos en 0.1 segundos expandiendo 7949 nodos

# Heuristicas tratadas para el ejercicio 6
Distancia de manhattan a la esquina no visitada mas cercana + Distancia de manhattan a la esquina no visitada mas cercana a la encontrada anteriormente, y asi. Disminuye considerablemente los nodos explorados pero no es consistente(se rompe la consistencia en tinyCorners y mediumCorners)

Cantidad de esquinas no visitadas: Aparentemente consistente pero la cantidad de nodos explorados disminuye muy poco

Distancia de manhattan a la esquina no visitada mas cercana: Expande mas nodos y es inconsistente, descartada.

Metodo 1 usando la distancia euclidea: Resultados similares,
sigue sin ser consistente pero la diferencia entre h(n) y c(n,n')+h(n') es cada vez menor.

Metodo 1 usando la norma infinito: Aparentemente consistente y expande muchisimos menos nodos. Sin embargo, no cumple la meta de explorar menos de 800 nodos en mediumCorners(expande alrededor de 848 nodos)

Revisar todos los ordenes posibles para visitar las esquinas y calcular el menor recorrido total entre todos los ordenes. Puede sonar prohibitivamente lento(de hecho, la complejidad es O(n!) por cada calculo de la heuristica), pero como solo son 4 pastillas hay que revisar como mucho 4! = 24 posibles ordenes. Se pueden precomputar algunos resultados para bajar la complejidad a O(1). Es aparentemente admisible y consistente, disminuye muchisimo la cantidad de nodos explorados y cumple con la meta de menos de 800 nodos explorados en mediumCorners(expande 741 nodos).

