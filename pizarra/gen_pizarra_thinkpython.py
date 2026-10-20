#!/usr/bin/env python3
"""Genera escenas .excalidraw tipo pizarra para los katas de Think Python (cap. 1-5)."""
import json, random, sys

W, Y = "#ffffff", "#ffd166"
C, P, G, R = "#76e4f7", "#f4a7c3", "#7bed9f", "#ff6b6b"

CONFIGS = {
    "beginner-series-number-2-clock": {
        "title": "KATA (8 kyu):  Reloj — horas a milisegundos",
        "pide": "Dadas h horas, m minutos y s\nsegundos desde medianoche, devuelve\nlos milisegundos transcurridos.",
        "decision": [
            ("No hay if: es ARITMÉTICA", C),
            ("total_seg = h*3600 + m*60 + s", Y),
            ("ms = total_seg * 1000", Y),
        ],
        "pista": "1 h = 3600 s, 1 min = 60 s,\n1 s = 1000 ms.\nDevuelve (return), no imprimas.",
        "algoritmo": [
            "recibe h, m, s",
            "multiplica h por 3600",
            "suma m por 60",
            "suma s",
            "multiplica por 1000 y devuelve",
        ],
        "tests": [
            "past(0,1,1)   → 61000      el ejemplo del kata",
            "past(1,0,0)   → 3600000    una hora",
            "past(0,0,0)   → 0          medianoche",
            "past(1,0,1)   → 3601000",
        ],
    },
    "string-repeat": {
        "title": "KATA (8 kyu):  Repetir cadena",
        "pide": "Recibes n (entero >= 0) y s (cadena).\nDevuelve s repetida n veces.",
        "decision": [
            ("¿n = 0?  → cadena vacía", C),
            ("¿n > 0?  → s pegada n veces", G),
            ("Operador clave:  s * n", Y),
        ],
        "pista": "\"abc\" * 3 → \"abcabcabc\"\nPython multiplica cadenas: ¡no hace\nfalta bucle! Piensa: return s * n",
        "algoritmo": [
            "recibe n y s",
            "multiplica la cadena: s * n",
            "devuelve el resultado",
        ],
        "tests": [
            'repeat_str(6, "I")     → "IIIIII"',
            'repeat_str(5, "Hello") → "Hello"x5',
            'repeat_str(0, "abc")   → ""        ¡caso límite!',
        ],
    },
    "find-nearest-square-number": {
        "title": "KATA (8 kyu):  Cuadrado más cercano",
        "pide": "Dado n positivo, devuelve el cuadrado\nperfecto más cercano. Si n ya es\ncuadrado, devuélvelo tal cual.",
        "decision": [
            ("raíz = sqrt(n), redondea con round()", C),
            ("¿baja o sube? round() decide", Y),
            ("resultado = raíz_redondeada ** 2", G),
        ],
        "pista": "import math → math.sqrt(n)\nround() elige el entero más cercano.\nEj: sqrt(111)=10.53→11→11²=121",
        "algoritmo": [
            "import math",
            "r = math.sqrt(n)",
            "k = round(r)",
            "devuelve k ** 2",
        ],
        "tests": [
            "nearest_sq(111) → 121   11² (10.53→11)",
            "nearest_sq(144) → 144   ya es cuadrado",
            "nearest_sq(10)  → 9     10<10.5→3²",
            "nearest_sq(1)   → 1",
        ],
    },
    "exclusive-or-xor-logical-operator": {
        "title": "KATA (8 kyu):  O exclusiva (xor)",
        "pide": "xor(a, b) devuelve True solo si\nEXACTAMENTE uno de a, b es True.\nLos dos iguales → False.",
        "decision": [
            ("¿a != b?", C),
            ("distintos → True", G),
            ("iguales  → False", R),
        ],
        "pista": "xor = «uno u otro, pero no ambos».\nEquivalente corto: return a != b\n(se pueden usar and/or/not también).",
        "algoritmo": [
            "compara a con b",
            "si son distintos → True",
            "si son iguales → False",
            "forma corta: return a != b",
        ],
        "tests": [
            "xor(False, False) → False   ninguno",
            "xor(True,  False) → True    uno solo",
            "xor(False, True)  → True    uno solo",
            "xor(True,  True)  → False   ¡los dos!",
        ],
    },
    "calculate-bmi": {
        "title": "KATA (8 kyu):  Índice de masa corporal",
        "pide": "bmi = peso / altura².\nDevuelve el TEXTO de la categoría\nsegún el valor.",
        "decision": [
            ("bmi <= 18.5 → \"Underweight\"", C),
            ("bmi <= 25.0 → \"Normal\"", G),
            ("bmi <= 30.0 → \"Overweight\"", Y),
            ("bmi > 30    → \"Obese\"", R),
        ],
        "pista": "Cadenas de if/elif/else de menor a\nmayor: el primer <= que se cumpla\ngana. Cada > ya viene filtrado.",
        "algoritmo": [
            "bmi = peso / altura ** 2",
            "if bmi <= 18.5 → Underweight",
            "elif bmi <= 25 → Normal",
            "elif bmi <= 30 → Overweight",
            "else → Obese",
        ],
        "tests": [
            "bmi(50,1.80)  → \"Underweight\"  15.4",
            "bmi(80,1.80)  → \"Normal\"       24.7",
            "bmi(90,1.80)  → \"Overweight\"   27.8",
            "bmi(110,1.80) → \"Obese\"        34.0",
        ],
    },
    "is-this-a-triangle": {
        "title": "KATA (7 kyu):  ¿Es un triángulo?",
        "pide": "Dados 3 lados a,b,c ¿se puede\nconstruir un triángulo (área > 0)?\nTrue si sí, False si no.",
        "decision": [
            ("Desigualdad triangular estricta:", C),
            ("a+b>c AND a+c>b AND b+c>a", Y),
            ("las 3 a la vez → True, si no False", G),
        ],
        "pista": "¡ESTRICTO! 1,2,3 no vale (degenerado).\nTodos los lados > 0 ya implícito.\nEs el is_triangle del cap. 5.",
        "algoritmo": [
            "comprueba a + b > c",
            "comprueba a + c > b",
            "comprueba b + c > a",
            "une con  and  y devuelve",
        ],
        "tests": [
            "(1,2,2) → True     (4,2,3) → True",
            "(2,2,2) → True     (1,2,3) → False",
            "(-5,1,3)→ False    (0,2,3) → False",
            "(1,2,9) → False    lado largo domina",
        ],
    },
    "rock-paper-scissors": {
        "title": "KATA (8 kyu):  Piedra, papel o tijeras",
        "pide": "Dos jugadas como cadenas. Devuelve\n\"Player 1 won!\", \"Player 2 won!\"\no \"Draw!\" según las reglas.",
        "decision": [
            ("¿p1 == p2?  → \"Draw!\"", C),
            ("¿p1 gana? (3 pares) → \"Player 1 won!\"", G),
            ("si no → \"Player 2 won!\"", R),
        ],
        "pista": "Ganar p1 solo en 3 casos:\nrock>scissors, scissors>paper,\npaper>rock. Todo lo demás: p2.",
        "algoritmo": [
            "if p1 == p2 → Draw!",
            "elif p1 en un par ganador → P1",
            "else → Player 2 won!",
        ],
        "tests": [
            '("\"scissors\",\"paper\") → Player 1 won!',
            '("\"scissors\",\"rock\")  → Player 2 won!',
            '("\"paper\",\"paper\")    → Draw!',
        ],
    },
    "grasshopper-summation": {
        "title": "KATA (8 kyu):  Sumatoria 1..num",
        "pide": "Devuelve 1+2+...+num.\nnum siempre positivo > 0.\nSolo el resultado, sin texto.",
        "decision": [
            ("Recursión: ¿caso base?", C),
            ("num == 1 → devuelve 1", Y),
            ("si no → num + summation(num-1)", G),
        ],
        "pista": "Recursión (cap.5): caso base n=1.\nAlternativa: bucle acumulando, o la\nfórmula n*(n+1)//2. Elige una.",
        "algoritmo": [
            "si num == 1 → return 1",
            "si no → return num + f(num-1)",
            "o: bucle sumando 1..num",
            "o: return num*(num+1)//2",
        ],
        "tests": [
            "summation(1) → 1     caso base",
            "summation(2) → 3     1+2",
            "summation(8) → 36    1+..+8",
            "summation(22)→ 253",
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
