# Laboratorio Python Tutor: ToLeetSpeak

Material del alumnado · autoría Devin.

El kata se resuelve juntando tres piezas que ya conoces. Aquí van por
separado, a propósito: ver cada una moverse en
[Python Tutor](https://pythontutor.com/) cuesta un minuto y te ahorra
diez de depurar a ciegas. Unirlas es tu trabajo.

Cómo usarlo: abre el enlace, pulsa «Next» paso a paso y mira qué
variables cambian en cada momento. No hace falta cuenta.

## Pieza 1: consultar el diccionario

```python
LEET = {'A': '@', 'E': '3', 'L': '1', 'T': '7'}
letra = 'E'
if letra in LEET:
    print(LEET[letra])
else:
    print(letra)
```

[Abrir pieza 1 en Python Tutor](https://pythontutor.com/visualize.html#code=LEET%20%3D%20%7B%27A%27%3A%20%27%40%27%2C%20%27E%27%3A%20%273%27%2C%20%27L%27%3A%20%271%27%2C%20%27T%27%3A%20%277%27%7D%0Aletra%20%3D%20%27E%27%0Aif%20letra%20in%20LEET%3A%0A%20%20%20%20print%28LEET%5Bletra%5D%29%0Aelse%3A%0A%20%20%20%20print%28letra%29&cumulative=false&heapPrimitives=nevernest&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0)

Qué mirar: `letra in LEET` da `True` o `False` según la letra esté en
el diccionario. Cambia `'E'` por `' '` (un espacio) en tu cabeza:
¿por qué rama iría?

## Pieza 2: recorrer una cadena carácter a carácter

```python
palabra = 'LEET'
for letra in palabra:
    print(letra)
```

[Abrir pieza 2 en Python Tutor](https://pythontutor.com/visualize.html#code=palabra%20%3D%20%27LEET%27%0Afor%20letra%20in%20palabra%3A%0A%20%20%20%20print%28letra%29&cumulative=false&heapPrimitives=nevernest&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0)

Qué mirar: el bucle se repite una vez por carácter, en orden, y
`letra` va tomando cada valor. Los espacios también son caracteres:
si la cadena fuera `'I AM'`, el bucle daría cuatro vueltas.

## Pieza 3: acumular en una cadena nueva

```python
resultado = ''
for letra in 'HOLA':
    resultado = resultado + letra
print(resultado)
```

[Abrir pieza 3 en Python Tutor](https://pythontutor.com/visualize.html#code=resultado%20%3D%20%27%27%0Afor%20letra%20in%20%27HOLA%27%3A%0A%20%20%20%20resultado%20%3D%20resultado%20%2B%20letra%0Aprint%28resultado%29&cumulative=false&heapPrimitives=nevernest&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0)

Qué mirar: `resultado` crece un carácter por vuelta: `''`, `'H'`,
`'HO'`, `'HOL'`, `'HOLA'`. Empezar en `''` (cadena vacía, con las
comillas) es lo que permite sumarle texto desde la primera vuelta.

## Después del laboratorio

Vuelve al notebook `clase-to-leet-speak-devin.ipynb` y escribe tu
`to_leet_speak` juntando las tres piezas. Cuando los tests pasen de
0/10 a 10/10, rellena `comparacion-posterior-devin.md`.
