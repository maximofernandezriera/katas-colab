#!/usr/bin/env python3
"""Inserta la hoja de ruta de lectura y la escalera de ayudas en cada notebook."""
import json, glob, re

HOJA_RUTA = """## Hoja de ruta — lee el kata antes de programar

Rellena esto **antes** de escribir código (hay una versión imprimible en `guia-lectura-kata.html`):

1. **¿Qué recibo?** Nº de parámetros y tipos (número, texto, booleano…):
2. **¿Qué devuelvo?** ¿Número, texto, booleano? ¿El texto debe ser exacto?
3. **Ejemplo, con mis palabras:** coge un ejemplo del enunciado y explica por qué da ese resultado.
4. **Casos límite:** ¿qué pasa con 0, negativos, cadena vacía, valores iguales…?
5. **La decisión:** ¿qué pregunta de sí/no hace el `if`? ¿Cuántas respuestas posibles hay y en qué orden?
6. **Plan:** escribe los pasos en castellano, uno por línea, sin código.
7. **Después:** ¿mis tests cubren esos casos límite? ¿Qué aprendí?
"""

# Nivel 1 (pista), Nivel 2 (pseudocódigo), Nivel 3 (esqueleto) por slug
AYUDAS = {
 "multiply": (
  "Es una kata de **depuración**: la función multiplica bien, pero el resultado nunca sale de ella. ¿Qué palabra clave le falta?",
  "función multiply(a, b):\n    calcular a × b\n    DEVOLVER el resultado   ← return",
  "def multiply(a, b):\n    ___ a * b"),
 "count-the-smiley-faces": (
  "Una cara sonriente tiene ojos (`:` o `;`), nariz opcional (`-` o `~`) y boca (`)` o `D`), en ese orden. Cualquier otro carácter la invalida. El patrón encaja perfecto con una expresión regular `[:;][-~]?[)D]`, o con tres preguntas encadenadas.",
  "contador ← 0\npara cada cara en la lista:\n    ¿ojos válidos? ¿nariz (si hay) válida? ¿boca válida?\n    si las tres → contador + 1\ndevolver contador",
  "import re\ndef count_smileys(arr):\n    return len(re.findall(r'___', ' '.join(arr)))"),
 "beginner-series-number-2-clock": (
  "No hay `if`: es aritmética pura. 1 h = 3600 s, 1 min = 60 s, 1 s = 1000 ms. El kata pide **devolver** (`return`), no imprimir.",
  "función past(h, m, s):\n    segundos ← h × 3600 + m × 60 + s\n    devolver segundos × 1000",
  "def past(h, m, s):\n    return (h * ___ + m * ___ + s) * ___"),
 "string-repeat": (
  "En Python las cadenas se **multiplican** por un entero: `\"ab\" * 3` → `\"ababab\"`. No necesitas bucle. ¿Qué pasa si `n` es 0?",
  "función repeat_str(n, s):\n    devolver s repetido n veces   ← s * n",
  "def repeat_str(n, s):\n    return s ___ n"),
 "find-nearest-square-number": (
  "`math.sqrt(n)` da el número cuyo cuadrado sería `n`; `round()` elige el entero más cercano. Después eleva ese entero al cuadrado.",
  "import math\nfunción nearest_sq(n):\n    k ← entero más cercano a sqrt(n)   ← round\n    devolver k al cuadrado           ← k ** 2",
  "import math\ndef nearest_sq(n):\n    k = ___(math.sqrt(n))\n    return k ___ 2"),
 "even-or-odd": (
  "`n % 2` es el resto de dividir entre 2: par → 0, impar → 1. Ojo: devuelves **texto** (`\"Even\"`/`\"Odd\"`), no booleano. Respeta las mayúsculas.",
  "función even_or_odd(n):\n    si n % 2 == 0 → devolver \"Even\"\n    si no        → devolver \"Odd\"",
  "def even_or_odd(number):\n    if number ___ 2 == 0:\n        return ___\n    else:\n        return ___"),
 "is-n-divisible-by-x-and-y": (
  "«Divisible» = resto 0. Deben cumplirse **las dos** condiciones a la vez (`and`). Truco: puedes devolver la comparación directamente, sin escribir if/else.",
  "función is_divisible(n, x, y):\n    devolver (n % x == 0)  Y  (n % y == 0)",
  "def is_divisible(n, x, y):\n    return n % x ___ 0 ___ n % y == 0"),
 "transportation-on-vacation": (
  "Precio base = 40 × días. Descuentos: 7+ días → −50, 3+ días → −20. **El orden importa**: comprueba primero el descuento mayor (si d=7 también cumple d>=3).",
  "total ← 40 × d\nsi d >= 7 → total − 50\nsi no, d >= 3 → total − 20\ndevolver total",
  "def rental_car_cost(d):\n    total = ___ * d\n    if d >= ___:\n        total -= 50\n    elif d >= 3:\n        total -= ___\n    return total"),
 "exclusive-or-xor-logical-operator": (
  "«O exclusiva» = uno u otro, **pero no ambos**: solo es `True` cuando los dos valores son **distintos**. ¿Qué operador compara «distinto»?",
  "función xor(a, b):\n    distintos → True, iguales → False\n    forma corta: devolver a != b",
  "def xor(a, b):\n    return a ___ b"),
 "calculate-bmi": (
  "`bmi = peso / altura ** 2`. Encadena `if/elif/else` **de menor a mayor** (18.5, 25, 30): cada `elif` solo se evalúa si el anterior falló.",
  "b ← peso / altura²\nsi b <= 18.5 → Underweight\nsi no, b <= 25 → Normal\nsi no, b <= 30 → Overweight\nsi no → Obese",
  "def bmi(weight, height):\n    b = weight / height ___ 2\n    if b <= 18.5:  return \"Underweight\"\n    elif b <= ___:   return \"Normal\"\n    elif b <= ___:   return \"Overweight\"\n    else:               return ___"),
 "is-this-a-triangle": (
  "Desigualdad triangular: cada lado < suma de los otros dos. **Estricta** (`>`, no `>=`): `1,2,3` no vale porque el kata exige área > 0. Tres comprobaciones con `and`.",
  "función is_triangle(a, b, c):\n    devolver (a+b>c) Y (a+c>b) Y (b+c>a)",
  "def is_triangle(a, b, c):\n    return a + b ___ c ___ a + c > b ___ b + c > a"),
 "rock-paper-scissors": (
  "El jugador 1 solo gana en **3 casos**: rock>scissors, scissors>paper, paper>rock. Primero empate (`p1 == p2`), luego los 3 pares con `or`, y lo demás es del jugador 2.",
  "si p1 == p2 → \"Draw!\"\nsi (p1,p2) es par ganador → \"Player 1 won!\"\nsi no → \"Player 2 won!\"",
  "def rps(p1, p2):\n    if p1 ___ p2:\n        return \"Draw!\"\n    if (p1 == \"rock\" and p2 == ___) or \\\n       (p1 == ___ and p2 == \"paper\") or \\\n       (p1 == \"paper\" and p2 == ___):\n        return \"Player 1 won!\"\n    return ___"),
 "grasshopper-summation": (
  "Tres caminos: (a) **recursión** — caso base `num == 1` y caso general `num + f(num-1)`; (b) bucle acumulando; (c) fórmula `n*(n+1)//2`. Si se pide recursión, usa (a).",
  "recursiva:\n  si num == 1 → 1   (caso base)\n  si no → num + summation(num-1)\nfórmula: num * (num + 1) // 2",
  "def summation(num):\n    if num == ___:\n        return 1\n    return num + ___(num - 1)\n# o: return num * (num + ___) // 2"),
}

def escalera_md(slug):
    n1, n2, n3 = AYUDAS[slug]
    return f"""## Escalera de ayudas (úsala solo si te atascas 15 min)

Regla: baja un peldaño por vez — Nivel 1 → Nivel 2 → Nivel 3. Nunca saltes al último sin leer el primero.

<details>
<summary><b>Nivel 1 — Pista de clase</b></summary>

{n1}
</details>

<details>
<summary><b>Nivel 2 — Pseudocódigo</b></summary>

```
{n2}
```
</details>

<details>
<summary><b>Nivel 3 — Esqueleto con huecos</b> (rellena los `___`)</summary>

```python
{n3}
```
</details>
"""

PLAN_MD = """## Paso 1.5 · Mi plan (modo pensar)

**Piensa antes de programar.** Rellena esta plantilla en lenguaje natural o
pseudocódigo — es parte de la entrega y tu profesor la revisará.

**ENTRADA:** ¿qué recibo? (parámetros y tipos, en mis palabras)
> …

**PLAN:** pasos numerados, cada uno empezando por verbo (*leer*, *comprobar*,
*devolver*, *calcular*…). Mínimo 3 pasos.
> 1. …
> 2. …
> 3. …

**SALIDA:** ¿qué devuelvo exactamente?
> …

**CASOS QUE VIGILO:** los casos límite que detecté en la hoja de ruta
> …
"""

PLAN_CELL = """# PASO 1.5 (continuación) — tu plan en formato revisable
# Escribe cada paso de tu plan como una cadena. La celda comprueba
# que el plan existe y tiene al menos 3 pasos (no corrige el contenido).

mi_plan = [
    # "1. leer ...",
    # "2. comprobar ...",
    # "3. devolver ...",
]

if not mi_plan:
    print("⚠ Tu plan está vacío: rellena la lista mi_plan con tus pasos.")
elif len(mi_plan) < 3:
    print(f"⚠ Solo {len(mi_plan)} paso(s): detalla el plan un poco más.")
else:
    print(f"✔ Plan registrado: {len(mi_plan)} pasos.")
    for paso in mi_plan:
        print("   ", paso)
"""

updated = []
for path in sorted(glob.glob('kata-*.ipynb')):
    nb = json.load(open(path))
    slug = None
    for c in nb['cells']:
        m = re.search(r'cargar_kata\("([^"]+)"\)', ''.join(c['source']))
        if m:
            slug = m.group(1); break
    if slug not in AYUDAS:
        print('SIN AYUDA:', path, slug); continue
    cells = nb['cells']
    changed = False
    # already inserted?
    if not any('Hoja de ruta' in ''.join(c['source']) for c in cells):
        cells.insert(4, {"cell_type":"markdown","metadata":{},"source":HOJA_RUTA.splitlines(keepends=True)})
        # escalera goes right after the solution cell (now index 5)
        cells.insert(6, {"cell_type":"markdown","metadata":{},"source":escalera_md(slug).splitlines(keepends=True)})
        changed = True
    # insert plan cells before the PASO 2 solution cell, if missing
    if not any('Mi plan (modo pensar)' in ''.join(c['source']) for c in cells):
        sol_idx = next(i for i,c in enumerate(cells)
                       if c['cell_type']=='code' and 'PASO 2' in ''.join(c['source']))
        cells.insert(sol_idx, {"cell_type":"code","metadata":{},"outputs":[],"execution_count":None,
                               "source":PLAN_CELL.splitlines(keepends=True)})
        cells.insert(sol_idx, {"cell_type":"markdown","metadata":{},"source":PLAN_MD.splitlines(keepends=True)})
        changed = True
    if not changed:
        print('YA TIENE:', path); continue
    json.dump(nb, open(path,'w'), ensure_ascii=False, indent=1)
    updated.append(path)
    print('OK', path, slug)
print(len(updated), 'notebooks actualizados')
