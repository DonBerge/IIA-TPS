### Heuristica elegida
La heuristica elegida para el ejercicio 6 es aquella que corresponde a la
resolución del problema de comer las pastillas en las esquinas cuando no hay
paredes en el laberinto.

$$h(n)=\text{numero minimo de pasos para alcanzar las 4 esquinas si no hay
paredes}$$

La heuristica es admisible, ya que el numero de pasos para obtener las pastillas
en un laberinto vacio no puede disminuir si se colocan paredes, por lo que la
heuristica no sobreestima el costo de la solucion.

### Consistencia de la heuristica
La condicion de consistencia se define como sigue:

Una heuristica h es consistente si, para todo estado $n$ y sus sucesores $n'$ se
tiene que:
$$h(n) \leq c(n,n') + h(n')$$

En este caso particular, $c(n,n')=1$ por lo que la propiedad a demostrar queda
como:
$$h(n)\leq 1 + h(n')$$

#### Demostración
Suponiendo que se parte de un estado $n$ y se pasa a un estado $n'$, si se esta
en un tablero sin paredes este paso puede pertenecer a alguno de los posibles
caminos que llevan a comer todas las pastillas en el minimo de pasos
(en cuyo caso $h(n') < h(n)$) o no pertence a ninguno de ellos y por ende es
un "paso en falso"(en cuyo caso $h(n')>h(n)$)

La propiedad se cumple en el ultimo caso ya que $h(n)<h(n')<h(n')+1$.

Para el primer caso, la definición indica que h es "el numero de pasos para llegar
si no hay paredes", por lo que si se da un paso que es camino a la solución $h$
solo puede disminuir en una unidad(sino pacman se movio mas de una vez), por lo
que se cumple que $h(n)=1+h(n')$.

Por lo tanto, se cumple la propiedad de consistencia y la heuristica es
consistente.

#### Demostración por indución
Voy a probar la consistencia con una propiedad mas fuerte,
$\forall n, \forall n': n' \text{ es sucesor de n } \implies |h(n)-h(n')|=1$

...

### Calculo de la heuristica
Suponiendo que se esta en una casilla incial $s$ alejada de las esquinas
y se quieren visitar todas las esquinas con pastillas en un tablero sin muros.

```
+-------------------+
|A                 B|
|                   |
|         S         |
|                   |
|C                 D|
+-------------------+
```

Para resolver este problema conviene primero resolver un problema mas sencillo,
si S se encuentra en una esquina, ¿cual es el menor numero de pasos para llegar
desde S hasta las demas esquinas?


Por ejemplo, un laberinto donde se da esta situacion es el siguiente
```
+-------------------+
|S                 B|
|                   |
|                   |
|                   |
|C                 D|
+-------------------+
```

Bien las 3 esquinas restantes podrian tener pastillas o alguna puede no tenerla,
la solución debe tener en cuenta estos casos.

Para resolver esto, se puede seguir un algoritmo tipo Greedy. Se va primero a
la esquina mas cercana a S, luego se va desde esta esquina a la siguiente mas
cercana y asi a visitar todas las esquinas.

Este algoritmo obtiene la solución optima del problema de alcanzar las esquinas
partiendo desde una esquina.

#### Demostración(algo larga)
Para demostrar voy a hacer un analisis por casos, donde hay que visitar 3
esquinas desde S, dos esquinas o solamente una.

##### Caso de tres esquinas
Sean $l$ el largo del tablero y $h$ la altura y suponiendo que se tiene un
tablero como sigue
```
+-------------------+
|S                 B|
|                   |
|                   |
|                   |
|C                 D|
+-------------------+
```

Hay 6 posibles formas de visitar las esquinas:

1. S->B->D->C, costo $2l+h$
2. S->B->C->D, costo $3l+h$
3. S->C->B->D, costo $3h+l$
4. S->C->D->B, costo $2h+l$
5. S->D->B->C, costo $3h+2l$
6. S->D->C->B, costo $3l+2h$

La ruta de menor costo va a ser la optima:

$2l+h$ $\leq$ $3l+h$

$2l+h$ $\leq$ $2l+3h$

$2l+h$ $\leq$ $3l+2h$

Por lo tanto las rutas 2, 5 y 6 no pueden ser optimas.

$2h+l$ $\leq$ $3h+l$, por lo tanto la ruta 3 no puede ser optima.

Entonces la ruta mas optima se decide entre la ruta 1 y la ruta 4.

La ruta 1 es mejor que la 4 sii $2l+h \leq 2h+l$, esto ocurre si $l\leq h$

La ruta 4 es mejor que la 4 sii $2h+l \leq 2l+h$, esto ocurre si $h\leq l$

Al ejecutar el algoritmo para el tablero anterior, si $l\leq h$ entonces el 
punto mas cercano es B, el punto mas cercano de B es D(ya que C esta distancia
$l+h$) y desde ahi solo se puede ir a C, por lo que el algoritmo escoje la ruta
1 de costo $2l+h$. Si en cambio $h\leq l$ entonces el algoritmo ira primero al 
punto C, luego a D y finalmente a B, se escoje la ruta 4 de costo $2h+l$.

Por lo tanto el algoritmo resuelve correctamente en el caso de tres esquinas.

Esta demostración se hizo para cuando S esta en la esquina superior izquierda,
pero todas las demas configuraciones son analogas ya que los tableros son
simetricos.

##### Caso de dos esquinas
Hay 3 posibles configuraciones para analizar
```
CONFIGURACION 1
+-------------------+
|S                 B|
|                   |
|                   |
|                   |
|C                  |
+-------------------+
```
```
CONFIGURACION 2
+-------------------+
|S                 B|
|                   |
|                   |
|                   |
|                  C|
+-------------------+
```

```
CONFIGURACION 3
+-------------------+
|S                  |
|                   |
|                   |
|                   |
|B                 C|
+-------------------+
```

En la configuración 1, hay 2 posibles rutas:

1. S -> B -> C, costo $2l+h$

2. S -> C -> B. costo $2h+l$

La mejor ruta depende de la comparación entre $l$ y $h$, si $l\leq h$ la ruta 1
es mas optima, en cuyo caso el algoritmo elige va primero al punto B y luego a
C. Por lo que resuelve optimamente. Si $h\leq l$, la ruta 2 es mas optima, aqui
C es el punto mas cercano, por lo que denuevo se resuelve de manera optima.

En la configuración 2 las rutas son:

1. S->B->C, costo $l+h$
2. S->C->B, costo $2h+l$

En este caso la ruta ganadora es siempre la 1, ya que para cualquier valor de
$l$ y $h$ el costo de 1 siempre es menor.

En este caso B esta a distancia $l$ de S y C a distancia $l+h$, por lo que el
punto mas cercano es B. Este punto es elegido por el algoritmo y la ruta optima
es encontrada.

La configuración 3 se resuelve de manera analoga a la 2.

##### Caso de una esquina

En este caso solo hay una unica ruta, por lo que el algoritmo la elige sin
problema.

En todas las posibles configuraciones el algoritmo encuentra una solución optima
, por lo tanto resuelve correctamente el problema de comer las pastillas en
las esquinas cuando se parte de una esquina.

##### Resolucion caso general
Este algoritmo para encontrar la distancia puede usarse para resolver el caso
donde la posicion inicial S no esta en las esquinas.

```
+-------------------+
|A                 B|
|                   |
|         S         |
|                   |
|C                 D|
+-------------------+
```

En este caso cualquier ruta de menor coste tiene que empezar por alguno de los
siguietes casos:

1. S -> A -> ...
2. S -> B -> ...
3. S -> C -> ...
4. S -> D -> ...

Todos los casos continuan en un escenario donde hay que llegar desde una esquina
del tablero a todas las demas, por lo que se puede usar el algoritmo greedy
anterior para resolver estos casos.

Asi, un candidato a solución puede obtenerse calculando la distancia desde el punto
inicial S a todas las esquinas y luego calcular la distancia faltanta usando
el algoritmo greedy. La solución del problema general consiste en el minimo de
todos los candidatos a solución(que son 4, por lo que computar la solucion no
es muy costoso).