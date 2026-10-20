#!/usr/bin/env python3
"""Genera un notebook .ipynb listo para Google Colab a partir de un kata de Codewars.

Uso:
    python kata2notebook.py <id-o-slug-del-kata> [-o salida.ipynb]

Ejemplo:
    python kata2notebook.py multiply -o kata_multiply.ipynb

El notebook generado:
  1. Descarga el enunciado del kata desde la API pública de Codewars.
  2. Incluye un mini-framework de tests estilo Codewars (describe/it/assert_equals).
  3. Una celda para que el alumno escriba su solución.
  4. Una celda de tests (editable por el profesor o el alumno).
  5. Una celda de comparación: pega soluciones de referencia o de la comunidad
     y compara resultados, tiempos y el diff línea a línea.
"""

import argparse
import json
import sys
import urllib.request

API = "https://www.codewars.com/api/v1/code-challenges/{slug}"


def fetch_kata(slug: str) -> dict:
    with urllib.request.urlopen(API.format(slug=slug)) as r:
        return json.load(r)


def md_cell(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}


def code_cell(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


SETUP_CELL = '''\
# ============================================================
#  BANCO DE PRUEBAS — framework de tests estilo Codewars
#  (no hace falta modificar esta celda, solo ejecutarla)
# ============================================================
import time
import difflib
import urllib.request
import json
import traceback

def cargar_kata(slug_o_id):
    """Descarga los datos del kata desde la API pública de Codewars."""
    url = f"https://www.codewars.com/api/v1/code-challenges/{slug_o_id}"
    with urllib.request.urlopen(url) as r:
        return json.load(r)

def mostrar_kata(kata):
    from IPython.display import Markdown, display
    rank = kata.get("rank") or {}
    display(Markdown(
        f"## {kata['name']}  ·  `{rank.get('name', '?')}`\\n"
        f"**Enlace:** {kata['url']}  \\n"
        f"**Tags:** {', '.join(kata.get('tags', []))}\\n\\n---\\n\\n"
        + kata.get("description", "")
    ))

# ---- mini framework estilo Codewars ----
_fallos = []
_aciertos = []

def _reset():
    _fallos.clear()
    _aciertos.clear()

def describe(nombre):
    print(f"\\n== {nombre} ==")

def it(nombre):
    print(f"  · {nombre}")

def assert_equals(real, esperado, msg=""):
    if real == esperado:
        _aciertos.append(1)
        print(f"    ✔ OK  →  {real!r}")
    else:
        _fallos.append((real, esperado, msg))
        print(f"    ✘ FALLO  →  obtenido {real!r}  esperado {esperado!r}  {msg}")

def resumen():
    total = len(_aciertos) + len(_fallos)
    print(f"\\n{'='*40}\\nResultado: {len(_aciertos)}/{total} tests superados")
    if _fallos:
        print("¡Sigue intentándolo! Revisa los fallos de arriba.")
    else:
        print("¡Todos los tests superados! 🎉 Ahora compara tu solución abajo.")

def comparar_con_referencia(mi_funcion, referencias, casos):
    """Ejecuta mi_funcion y cada función de referencia sobre 'casos'
    (lista de tuplas de argumentos) y compara resultados y tiempos."""
    for nombre, src in referencias.items():
        ns = {}
        exec(src, ns)
        ref = ns.get("solucion") or next(iter(ns.values()))
        print(f"\\n### {nombre}")
        for caso in casos:
            args = caso if isinstance(caso, tuple) else (caso,)
            try:
                t0 = time.perf_counter()
                esperado = ref(*args)
                t_ref = (time.perf_counter() - t0) * 1e6
            except Exception as e:
                print(f"  referencia falla en {args}: {e}")
                continue
            try:
                t0 = time.perf_counter()
                obtenido = mi_funcion(*args)
                t_mio = (time.perf_counter() - t0) * 1e6
            except Exception:
                print(f"  tu solución lanza excepción en {args}:")
                traceback.print_exc(limit=1)
                continue
            marca = "✔" if obtenido == esperado else "✘"
            print(f"  {marca} {args} → tuyo={obtenido!r} ref={esperado!r}  "
                  f"(tú: {t_mio:.0f}µs / ref: {t_ref:.0f}µs)")

def diff(mi_src, ref_src, nombre="referencia"):
    """Muestra un diff línea a línea entre tu código y otra solución."""
    d = difflib.unified_diff(
        ref_src.splitlines(), mi_src.splitlines(),
        fromfile=nombre, tofile="tu solución", lineterm="")
    print("\\n".join(d))
'''

PLAN_MD = """\
## Paso 1.5 · Mi plan (modo pensar)

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

PLAN_CELL = '''\
# PASO 1.5 (continuación) — tu plan en formato revisable
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
'''

COMPARE_CELL = '''\
# ============================================================
#  PASO 4 — Compara tu solución con otras
#  Tras resolver el kata en codewars.com se desbloquean las
#  soluciones de la comunidad: pégalas aquí para analizarlas.
#  Tu profesor también puede darte soluciones de referencia.
# ============================================================

# Tu código (pégalo tal cual para el diff):
mi_codigo = """
def solucion(...):
    pass  # pega aquí tu solución
"""

# Soluciones con las que comparar (nombre: código).
# Deben definir una función llamada 'solucion' (o ser la única función).
soluciones_referencia = {
    "solución del profesor": """
def solucion(...):
    pass  # solución de referencia
""",
}

# Los mismos casos de prueba de la celda anterior:
casos = [
    # (argumentos...) — rellénalos igual que en tus tests
]

# Descomenta cuando tengas algo que comparar:
# comparar_con_referencia(solucion, soluciones_referencia, casos)
# diff(mi_codigo, list(soluciones_referencia.values())[0])
'''

FOOTER_MD = """\
---
### Cómo usar este banco de pruebas
1. **Lee el enunciado** y abre el kata en codewars.com.
2. **Escribe tu solución** en la celda correspondiente.
3. **Completa los tests**: añade casos de ejemplo del enunciado y casos límite que se te ocurran. Escribir buenos tests es parte del ejercicio.
4. **Resuelve el kata en la web** con tu solución cuando pase tus tests.
5. **Compara**: al resolverlo, Codewars desbloquea las soluciones de la comunidad. Pega las que te interesen en la última celda y analiza qué hacen distinto: ¿más cortas? ¿más rápidas? ¿más legibles? ¿por qué?
"""


def load_translation(slug: str, lang: str) -> str | None:
    """Busca traducciones/<slug>.md junto al script. Devuelve None si no existe."""
    from pathlib import Path
    p = Path(__file__).parent / "traducciones" / f"{slug}.md"
    return p.read_text(encoding="utf-8").strip() if p.exists() else None


def build_notebook(kata: dict, slug: str, lang: str = "es") -> dict:
    rank = (kata.get("rank") or {}).get("name", "")
    header = f"""\
# Banco de pruebas Codewars: {kata['name']} (`{rank}`)

Notebook generado con `kata2notebook.py` a partir de
[{kata['url']}]({kata['url']}).

> Trabaja el kata aquí antes de enviarlo a Codewars. La API pública no
> incluye el código inicial ni los tests oficiales: en el Paso 2 defines
> la firma de la función (mírala en la web del kata) y en el Paso 3 tus
> propios tests.
"""
    cells = [
        md_cell(header),
        code_cell(
            "# PASO 0 — ejecuta esta celda para cargar las utilidades\n" + SETUP_CELL
        ),
        code_cell(
            f'# PASO 1 — carga el enunciado del kata\nkata = cargar_kata("{slug}")\nmostrar_kata(kata)'
        ),
        # placeholder: la celda de traducción se inserta aquí si existe
    ]
    traduccion = load_translation(slug, lang)
    if traduccion:
        cells.insert(3, md_cell(
            "## Enunciado en castellano (traducción)\n\n"
            "> Traducción al castellano del enunciado; el original en inglés "
            "se muestra en el Paso 1.\n\n" + traduccion
        ))

    cells += [
        md_cell(PLAN_MD),
        code_cell(PLAN_CELL),
        code_cell(
            "# PASO 2 — TU SOLUCIÓN\n"
            "# Copia la firma de la función desde codewars.com\n\n"
            "def solucion():\n"
            "    raise NotImplementedError('escribe aquí tu solución')\n"
        ),
        code_cell(
            '# PASO 3 — TUS TESTS\n'
            '_reset()\n\n'
            'describe("Ejemplos del enunciado")\n'
            'it("caso 1")\n'
            '# assert_equals(solucion(...), valor_esperado)\n\n'
            'describe("Casos límite")\n'
            'it("...")\n'
            '# assert_equals(solucion(...), ...)\n\n'
            'resumen()\n'
        ),
        code_cell(COMPARE_CELL),
        md_cell(FOOTER_MD),
    ]
    return {
        "cells": cells,
        "metadata": {
            "colab": {"provenance": [], "name": f"kata-{slug}.ipynb"},
            "kernelspec": {"display_name": "Python 3", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("slug", help="id o slug del kata (p.ej. 'multiply' o '50654ddff44f800200000004')")
    p.add_argument("-o", "--output", help="fichero .ipynb de salida (por defecto kata-<slug>.ipynb)")
    args = p.parse_args()

    kata = fetch_kata(args.slug)
    slug = kata["slug"]
    out = args.output or f"kata-{slug}.ipynb"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(build_notebook(kata, slug), f, ensure_ascii=False, indent=1)
    print(f"✔ Notebook generado: {out}  ({kata['name']}, {kata['rank']['name']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
