# «O exclusiva» (xor)

## Resumen

En algunos lenguajes existe un operador lógico llamado «o exclusiva» (*exclusive or*). Evalúa dos booleanos y devuelve `true` si **exactamente uno de los dos es verdadero**; en caso contrario, `false`.

```
False xor False == False   # ambos falsos
True  xor False == True    # exactamente uno es verdadero
False xor True  == True    # exactamente uno es verdadero
True  xor True  == False   # ambos verdaderos: xor solo es True si EXACTAMENTE uno lo es
```

## Tarea

Define una función `xor(a, b)` donde `a` y `b` son las dos expresiones a evaluar. Debe devolver el resultado booleano de la «o exclusiva».
