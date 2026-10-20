# Codewars Kata Workbench para Google Colab

Herramienta para trabajar katas de [codewars.com](https://www.codewars.com) en clase:
genera un notebook de Colab por kata con enunciado, mini-framework de tests
estilo Codewars y una celda para comparar la solución del alumno con las
soluciones de la comunidad o de referencia.

## Generar un notebook

```bash
python3 kata2notebook.py <id-o-slug> [-o salida.ipynb]

# ejemplos
python3 kata2notebook.py multiply
python3 kata2notebook.py 50654ddff44f800200000004 -o kata_bugfixes.ipynb
```

Sin dependencias externas: solo Python 3 y urllib. El id/slug es la última
parte de la URL del kata o el id de su API.

## Usarlo en Colab

1. Genera el notebook y súbelo a un repo de GitHub o a Drive.
2. En Colab: **Archivo → Subir cuaderno** o **GitHub** y pega la URL del repo.
3. El alumnado ejecuta las celdas en orden (Paso 0 → 4).

## Qué hace cada celda

- **Paso 0**: carga `cargar_kata`, `mostrar_kata`, el mini-framework
  (`describe`, `it`, `assert_equals`, `resumen`) y las funciones de
  comparación (`comparar_con_referencia`, `diff`).
- **Paso 1**: descarga y muestra el enunciado desde la API pública.
- **Paso 2**: celda-solución del alumno (la firma se copia de la web del kata;
  la API pública no la expone).
- **Paso 3**: tests propios — escribir buenos tests es parte del ejercicio.
- **Paso 4**: comparación — tras resolver el kata en la web se desbloquean
  las soluciones de la comunidad; se pegan en `soluciones_referencia` y se
  comparan resultados, tiempos y diff línea a línea.

## Traducciones al castellano

El directorio `traducciones/` contiene `<slug>.md` con el enunciado traducido.
Si existe el fichero para el kata, el notebook generado incluye una celda
**«Enunciado en castellano (traducción)»** justo después del Paso 1 (el
original en inglés sigue visible). Para traducir otro kata, añade su
`traducciones/<slug>.md` y regenera el notebook.

Incluidas: `count-the-smiley-faces`, `multiply`.

## Limitaciones de la API pública

Codewars no expone por API el código inicial, los tests oficiales ni las
soluciones de otros usuarios (requieren sesión). Por eso el notebook trabaja
con tests propios y con soluciones pegadas manualmente.
