### ¿Quién es el asesino?

¡Han matado a varias personas! Has conseguido reducir los sospechosos a unos pocos. Por suerte, conoces a todas las personas que cada sospechoso vio el día de los asesinatos.

**Tarea.** Recibes un diccionario con los nombres de los sospechosos y las personas que cada uno vio ese día, que puede tener esta pinta:

```python
{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
```

y también una lista con los nombres de las víctimas:

```python
['Lucas', 'Bill']
```

Devuelve el nombre del único asesino: en este caso `'James'`, porque es la única persona que vio tanto a `'Lucas'` como a `'Bill'`.
