### Descifra el código Morse

> Este kata es el primero de una serie de tres sobre el código Morse. Cuando lo resuelvas puedes pasar al [siguiente](https://www.codewars.com/kata/decode-the-morse-code-advanced).

En este kata tienes que escribir un descifrador sencillo de [código Morse](https://es.wikipedia.org/wiki/C%C3%B3digo_morse). Hoy casi nadie lo usa, porque la voz y los datos digitales lo han sustituido, pero todavía se emplea en algunos sitios del mundo.

El Morse convierte cada carácter en una secuencia de «puntos» y «rayas». Por ejemplo, la letra `A` es `·−`, la `Q` es `−−·−` y el dígito `1` es `·−−−−`. No distingue mayúsculas de minúsculas; lo tradicional es usar mayúsculas.

Cuando se escribe un mensaje en Morse:

- **un espacio** separa los códigos de dos caracteres;
- **tres espacios** separan dos palabras.

Por ejemplo, el mensaje `HEY JUDE` en Morse es `···· · −·−−   ·−−− ··− −·· ·`.

**NOTA:** los espacios que sobren al principio o al final del código no significan nada y hay que ignorarlos.

Además de letras, dígitos y algunos signos de puntuación, hay códigos especiales de servicio. El más famoso es la señal internacional de socorro [SOS](https://es.wikipedia.org/wiki/SOS), que se codifica como `···−−−···`. Estos códigos especiales cuentan como **un solo carácter** y normalmente se transmiten como palabras sueltas.

**Tu tarea:** escribe una función que reciba el código Morse y devuelva el texto descifrado, legible para una persona.

```python
decode_morse('.... . -.--   .--- ..- -.. .')
# debe devolver "HEY JUDE"
```

**NOTA:** en el código tienes que usar los caracteres ASCII `.` y `-`, no los símbolos Unicode `·` y `−`.

En Codewars la tabla Morse ya viene **precargada como diccionario**: puedes usar `MORSE_CODE['.--']`. En este notebook la tienes en la celda del Paso 0.

Todas las cadenas de los tests son Morse válido, así que no hace falta comprobar errores ni excepciones.

¡Suerte!
