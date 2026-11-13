Crea una función que devuelva el nombre del ganador de un combate entre dos luchadores.

Los luchadores se turnan para atacarse y gana quien mate primero al otro. Se muere al tener `health <= 0`.

Cada luchador es un objeto de la clase `Fighter` (la clase aparece en el enunciado original). `health` y `damage_per_attack` (en Python) son enteros mayores que `0`. Puedes modificar los objetos `Fighter`.

La función recibe un tercer argumento, un texto, con el nombre del luchador que ataca primero.

Ejemplo:
```
declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"

Lew ataca a Harry; Harry se queda con 3 de vida.
Harry ataca a Lew; Lew se queda con 6.
Lew ataca a Harry; Harry se queda con 1.
Harry ataca a Lew; Lew se queda con 2.
Lew ataca a Harry: Harry se queda con -1, muere y Lew gana.
```
