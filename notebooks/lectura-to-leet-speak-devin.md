# Lectura: ToLeetSpeak

Material del alumnado · autoría Devin · kata de Codewars (7 kyu):
<https://www.codewars.com/kata/57c1ab3949324c321600013f>

## Qué pide el kata

Escribir una función `to_leet_speak(texto)` que reciba una frase en
inglés y la devuelva traducida a «leetspeak», esa escritura juguetona
que cambia letras por números y símbolos parecidos. Ojo: es una
codificación didáctica para practicar, no un cifrado seguro.

## Entrada

Una cadena (`str`) que solo contiene:

- letras MAYÚSCULAS inglesas, de la A a la Z
- espacios

No llegan minúsculas, números, signos ni tildes. No hay que validar
nada ni tratar casos raros.

## Salida

Otra cadena con la misma longitud donde:

- cada letra se ha sustituido por su símbolo según el diccionario
- cada espacio se queda como espacio

## Ejemplos

```python
to_leet_speak('LEET')           # '1337'
to_leet_speak('HOLA MUNDO')     # '#01@ MUND0'
to_leet_speak('I LOVE PYTHON')  # '! 10V3 PY7#0N'
to_leet_speak('')               # ''
```

## El diccionario exacto

Es el del enunciado. Si copias un solo símbolo mal, falla ese test.

```python
LEET = {
    'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F',
    'G': '6', 'H': '#', 'I': '!', 'J': 'J', 'K': 'K', 'L': '1',
    'M': 'M', 'N': 'N', 'O': '0', 'P': 'P', 'Q': 'Q', 'R': 'R',
    'S': '$', 'T': '7', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', 'Z': '2',
}
```

Fíjate en dos cosas:

- algunas letras se traducen a sí mismas (`'D': 'D'`, `'F': 'F'`…)
- el espacio NO está en el diccionario: es lo que hace que pase tal
  cual si tu función gestiona bien el «si no está, cópialo igual»

## Casos para pensar antes de programar

- `''` (cadena vacía): el bucle no entra y devuelves `''`. Gratis.
- `'A  B'` (dos espacios seguidos): debe dar `'@  8'`, con los dos
  espacios intactos.
- `'DFJKMNPQRUVWXY'` (solo letras que no cambian): sale igual que
  entra.
- `'A B'` (un solo espacio): `'@ 8'`.

## Plan en tres pasos

1. `resultado = ''` — aquí iremos acumulando la traducción.
2. Recorrer `texto` con un `for`, carácter a carácter. Si la letra
   está en `LEET`, añadir `LEET[letra]`; si no está, añadir la letra
   tal cual.
3. `return resultado` cuando el bucle termine.

El detalle está en `plan-3-pasos-devin.md`, que puedes editar y
convertir en tu propio pseudocódigo.
