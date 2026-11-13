En un pueblo pequeño la población al comienzo de un año es `p0 = 1000`. Cada año aumenta un `2 por ciento` y además llegan `50` habitantes nuevos por año. ¿Cuántos años necesita el pueblo para tener una población mayor o igual a `p = 1200` habitantes?

```
Al final del primer año habrá:
1000 + 1000 * 0.02 + 50 => 1070 habitantes

Al final del 2.º año habrá:
1070 + 1070 * 0.02 + 50 => 1141 habitantes (** el número de habitantes es entero **)

Al final del 3.er año habrá:
1141 + 1141 * 0.02 + 50 => 1213

Hacen falta 3 años completos.
```

En general, dados los parámetros `p0, percent, aug` (habitantes que llegan o se van cada año), `p` (población que hay que igualar o superar), la función `nb_year` debe devolver `n`, el número de años completos necesarios para llegar a una población mayor o igual a `p`.

`aug` es un entero, `percent` es un número decimal positivo o cero, `p0` y `p` son enteros positivos (> 0).

```
Ejemplos:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
```

Notas:
* Convierte el parámetro `percent` a porcentaje dentro de la función: si `percent` es 2, usa 0.02.
* No existen fracciones de persona. Al final de cada año la población es un entero: `252.8` personas se redondea a `252`.
