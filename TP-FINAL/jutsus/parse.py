import json

input_file = "lista.txt"
output_file = "secuencias.json"

secuencias = {}

def translate_sign(sign):
    translations = {
        'Bird': 'bird',
        'Boar': 'boar',
        'Monkey': 'monkey',
        'Dog': 'dog',
        'Tiger': 'tiger',
        'Snake': 'snake',
        'Rat': 'rat',
        'Sheep': 'ram',
        'Horse': 'horse',
        'Dragon': 'dragon',
        'Ox': 'ox',
        'Rabbit': 'hare'
    }
    return translations.get(sign, None)

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or ':' not in line:
            continue
        nombre, elementos = line.split(':', 1)
        nombre = nombre.strip()
        elementos = [translate_sign(e.strip()) for e in elementos.split(',') if e.strip()]
        elementos_sin_nones = [e for e in elementos if e is not None]
        # Solo guardar secuencias no vacias
        if elementos_sin_nones:
            secuencias[nombre] = elementos_sin_nones

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(secuencias, f, ensure_ascii=False, indent=2)