#!/usr/bin/env python3
"""Genera pizarra.excalidraw: esquema tipo pizarra del kata 'Count the smiley faces!'."""
import json, random

random.seed(7)
els = []

def base(t, x, y, w, h, **kw):
    e = dict(id=f"e{len(els)}", type=t, x=x, y=y, width=w, height=h, angle=0,
             strokeColor=kw.get("sc", "#ffffff"), backgroundColor=kw.get("bg", "transparent"),
             fillStyle="hachure", strokeWidth=kw.get("sw", 2), strokeStyle="solid",
             roughness=1, opacity=100, groupIds=[], frameId=None,
             roundness={"type": 3} if t == "rectangle" else None,
             seed=random.randint(1, 2**31), version=1, versionNonce=random.randint(1, 2**31),
             isDeleted=False, boundElements=None, updated=1, link=None, locked=False)
    els.append(e)
    return e

def text(x, y, s, size=20, color="#ffffff", align="left"):
    # aproxima el ancho: Virgil ~0.55em por caracter
    w = max(len(l) for l in s.split("\n")) * size * 0.55
    h = len(s.split("\n")) * size * 1.25
    e = base("text", x, y, w, h, sc=color)
    e.update(text=s, fontSize=size, fontFamily=1, textAlign=align,
             verticalAlign="top", baseline=int(h * 0.82), containerId=None,
             originalText=s, lineHeight=1.25, autoResize=True)
    return e

def rect(x, y, w, h, color="#ffffff", bg="transparent", sw=2):
    return base("rectangle", x, y, w, h, sc=color, bg=bg, sw=sw)

def arrow(x1, y1, x2, y2, color="#ffd166"):
    e = base("arrow", x1, y1, abs(x2 - x1), abs(y2 - y1), sc=color)
    e.update(points=[[0, 0], [x2 - x1, y2 - y1]], lastCommittedPoint=None,
             startBinding=None, endBinding=None, startArrowhead=None, endArrowhead="arrow")
    return e

W, Y = "#ffffff", "#ffd166"   # tiza blanca / amarilla
C, P, G, R = "#76e4f7", "#f4a7c3", "#7bed9f", "#ff6b6b"  # cian rosa verde rojo

# ---- Pizarra ----
text(40, 30, "KATA CODEWARS (6 kyu):  Cuenta las caras sonrientes", 34, Y)

# ---- Bloque 1: qué pide ----
rect(40, 110, 400, 120, C)
text(60, 125, "¿QUÉ PIDE?", 22, C)
text(60, 160, "Dado un array de cadenas, devuelve\ncuántas son caras sonrientes VÁLIDAS.", 20, W)

# ---- Bloque 2: anatomía ----
rect(40, 260, 400, 300, Y)
text(60, 275, "ANATOMÍA DE LA CARA :)", 22, Y)
text(60, 315, "ojos     →   :   o   ;", 24, W)
text(60, 355, "nariz    →   -   o   ~", 24, W)
text(60, 395, "boca     →   )   o   D", 24, W)
text(60, 430, "(la nariz es opcional)", 18, C)
text(60, 460, "¡El orden siempre es el mismo!", 20, P)
text(60, 492, "ojos  →  [nariz]  →  boca", 20, P)
text(60, 528, "otros caracteres = NO válida", 18, R)

# ---- Bloque 3: patrón ----
rect(480, 110, 340, 150, G)
text(500, 125, "EL PATRÓN (¡regex!)", 22, G)
text(500, 165, "[:;]  [-~]?  [)D]", 30, W)
text(500, 210, "ojos · nariz opcional · boca", 18, W)

# ---- Bloque 4: ejemplos ----
rect(480, 290, 340, 130, W)
text(500, 305, "VÁLIDAS", 22, G)
text(500, 345, ":)   :D   ;-D   :~)", 26, G)
rect(480, 440, 340, 120, W)
text(500, 455, "NO VÁLIDAS", 22, R)
text(500, 495, ";(   :>   :}   :]", 26, R)

# ---- Bloque 5: algoritmo ----
rect(860, 110, 380, 450, P)
text(880, 125, "EL ALGORITMO", 22, P)
text(880, 170, "contador = 0", 22, W)
arrow(900, 200, 900, 240)
text(880, 250, "para cada cara del array:", 20, W)
text(900, 285, "¿ojos válidos?", 20, C)
text(900, 320, "¿nariz válida o ausente?", 20, C)
text(900, 355, "¿boca válida?", 20, C)
arrow(900, 385, 900, 425)
text(880, 435, "si OK → contador += 1", 22, G)
text(880, 480, "devuelve contador", 22, W)
text(880, 520, "array vacío → 0", 18, Y)

# ---- Ejemplos resueltos ----
rect(40, 600, 1200, 140, W)
text(60, 615, "COMPRUÉBALO: los tests del kata", 22, Y)
text(60, 660, "[':)', ';(', ';}', ':-D'] → 2        válidas: :) y :-D\n[';D', ':-(', ':-)', ';~)'] → 3     válidas: ;D :-) ;~)\n[';]', ':[', ';*', ':$', ';-D'] → 1   válida: ;-D", 22, W)

scene = {
    "type": "excalidraw", "version": 2,
    "source": "https://github.com/excalidraw/excalidraw",
    "elements": els,
    "appState": {"gridSize": None, "viewBackgroundColor": "#0e2f26"},
    "files": {},
}
with open("pizarra-smiley-faces.excalidraw", "w") as f:
    json.dump(scene, f)
print("OK", len(els), "elementos")
