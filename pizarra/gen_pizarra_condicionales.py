#!/usr/bin/env python3
"""Genera escenas .excalidraw tipo pizarra para katas de condicionales."""
import json, random, sys

W, Y = "#ffffff", "#ffd166"
C, P, G, R = "#76e4f7", "#f4a7c3", "#7bed9f", "#ff6b6b"

CONFIGS = {
    "even-or-odd": {
        "title": "KATA (8 kyu):  Par o impar — Even or Odd",
        "pide": "Recibes un entero y devuelves\nun TEXTO: \"Even\" si es par,\n\"Odd\" si es impar.",
        "decision": [
            ("¿n % 2 == 0?", C),
            ("SÍ  →  devuelve \"Even\"", G),
            ("NO  →  devuelve \"Odd\"", R),
        ],
        "pista": "n % 2  es el RESTO de dividir entre 2.\nPar: resto 0.  Impar: resto 1.\nOjo: devuelve TEXTO, no booleano.",
        "algoritmo": [
            "lee el entero n",
            "calcula n % 2",
            "si resto == 0 → \"Even\"",
            "si resto != 0 → \"Odd\"",
            "devuelve el texto",
        ],
        "tests": [
            'even_or_odd(2)   →  "Even"     (2 % 2 = 0)',
            'even_or_odd(7)   →  "Odd"      (7 % 2 = 1)',
            'even_or_odd(0)   →  "Even"     ¡caso límite!',
            'even_or_odd(-3)  →  "Odd"      negativos también',
        ],
    },
    "is-n-divisible-by-x-and-y": {
        "title": "KATA (8 kyu):  ¿Es n divisible por x E y?",
        "pide": "Dados n, x, y (positivos, sin ceros),\ndevuelve True/False: ¿n es divisible\npor x Y por y A LA VEZ?",
        "decision": [
            ("¿n % x == 0  and  n % y == 0?", C),
            ("SÍ  →  True", G),
            ("NO  →  False", R),
        ],
        "pista": "«divisible» = resto 0 al dividir.\nAND: deben cumplirse LAS DOS.\nNo hace falta escribir if/else:\npuedes devolver la comparación directa.",
        "algoritmo": [
            "¿n % x == 0?  (¿cabe x en n?)",
            "¿n % y == 0?",
            "une con  and",
            "devuelve el booleano",
            "bonus: return n%x==0 and n%y==0",
        ],
        "tests": [
            "n=3,  x=1, y=3  → True    3÷1 y 3÷3",
            "n=12, x=2, y=6  → True    12÷2 y 12÷6",
            "n=100,x=5, y=3  → False   100÷3 no exacto",
            "n=12, x=7, y=5  → False   ni 7 ni 5",
        ],
    },
    "transportation-on-vacation": {
        "title": "KATA (8 kyu):  Alquiler de coche",
        "pide": "Cada día cuesta $40.\n7+ días → -$50 de descuento.\n3+ días → -$20.\nDevuelve el precio total para d días.",
        "decision": [
            ("¿d >= 7?  → total - 50", G),
            ("¿d >= 3?  → total - 20", Y),
            ("si no     → sin descuento", C),
        ],
        "pista": "¡Orden importa! Primero el descuento\nmayor: si d=7 también cumple d>=3.\nif → elif → else. Total base = 40 * d.",
        "algoritmo": [
            "total = 40 * d",
            "si d >= 7 → total -= 50",
            "elif d >= 3 → total -= 20",
            "si no → total se queda igual",
            "devuelve total",
        ],
        "tests": [
            "d=1   → 40      40·1, sin descuento",
            "d=3   → 100     120 - 20",
            "d=6   → 220     240 - 20",
            "d=7   → 230     280 - 50  (¡no -70!)",
            "d=10  → 350     400 - 50",
        ],
    },
}


def make_scene(cfg):
    random.seed(7)
    els = []

    def base(t, x, y, w, h, **kw):
        e = dict(id=f"e{len(els)}", type=t, x=x, y=y, width=w, height=h, angle=0,
                 strokeColor=kw.get("sc", W), backgroundColor=kw.get("bg", "transparent"),
                 fillStyle="hachure", strokeWidth=kw.get("sw", 2), strokeStyle="solid",
                 roughness=1, opacity=100, groupIds=[], frameId=None,
                 roundness={"type": 3} if t == "rectangle" else None,
                 seed=random.randint(1, 2**31), version=1, versionNonce=random.randint(1, 2**31),
                 isDeleted=False, boundElements=None, updated=1, link=None, locked=False)
        els.append(e)
        return e

    def text(x, y, s, size=20, color=W, align="left"):
        w = max(len(l) for l in s.split("\n")) * size * 0.55
        h = len(s.split("\n")) * size * 1.25
        e = base("text", x, y, w, h, sc=color)
        e.update(text=s, fontSize=size, fontFamily=1, textAlign=align,
                 verticalAlign="top", baseline=int(h * 0.82), containerId=None,
                 originalText=s, lineHeight=1.25, autoResize=True)
        return e

    def rect(x, y, w, h, color=W):
        return base("rectangle", x, y, w, h, sc=color)

    def arrow(x1, y1, x2, y2, color=Y):
        e = base("arrow", x1, y1, abs(x2 - x1), abs(y2 - y1), sc=color)
        e.update(points=[[0, 0], [x2 - x1, y2 - y1]], lastCommittedPoint=None,
                 startBinding=None, endBinding=None, startArrowhead=None, endArrowhead="arrow")
        return e

    # Título
    text(40, 30, cfg["title"], 34, Y)

    # ¿Qué pide?
    rect(40, 110, 400, 150, C)
    text(60, 125, "¿QUÉ PIDE?", 22, C)
    text(60, 165, cfg["pide"], 20, W)

    # La decisión (lo importante en condicionales)
    rect(40, 290, 400, 40 + len(cfg["decision"]) * 55, G)
    text(60, 305, "LA DECISIÓN  (if / elif / else)", 22, G)
    yy = 345
    for linea, color in cfg["decision"]:
        text(70, yy, linea, 22, color)
        yy += 55

    # El algoritmo (columna derecha)
    algo_h = 60 + len(cfg["algoritmo"]) * 45 + 30
    rect(480, 110, 380, algo_h, P)
    text(500, 125, "EL ALGORITMO", 22, P)
    ya = 170
    for i, paso in enumerate(cfg["algoritmo"]):
        text(500, ya, paso, 20, W)
        ya += 45
        if i < len(cfg["algoritmo"]) - 1:
            arrow(505, ya - 15, 505, ya - 2)

    # Pista de profesor (columna derecha, bajo el algoritmo)
    yp = 110 + algo_h + 40
    rect(480, yp, 380, 160, Y)
    text(500, yp + 15, "PISTA DE CLASE", 20, Y)
    text(500, yp + 50, cfg["pista"], 18, W)

    # Tests a todo lo ancho, abajo
    bottom_y = max(yp + 160, 290 + 40 + len(cfg["decision"]) * 55) + 40
    rect(40, bottom_y, 820, 70 + len(cfg["tests"]) * 42, W)
    text(60, bottom_y + 15, "COMPRUÉBALO: los tests del kata", 22, Y)
    yt = bottom_y + 60
    for t in cfg["tests"]:
        text(60, yt, t, 19, W)
        yt += 42

    return {
        "type": "excalidraw", "version": 2,
        "source": "https://github.com/excalidraw/excalidraw",
        "elements": els,
        "appState": {"gridSize": None, "viewBackgroundColor": "#0e2f26"},
        "files": {},
    }


for slug, cfg in CONFIGS.items():
    scene = make_scene(cfg)
    with open(f"pizarra-{slug}.excalidraw", "w") as f:
        json.dump(scene, f)
    print("OK", slug, len(scene["elements"]), "elementos")
