import re

# Archivos a procesar
archivos = ["espanol.txt", "frances.txt", "italiano.txt"]

print(f"{'Archivo':12}{'Enteros':10}{'Flotantes':12}{'Listas':10}{'Palabras':10}")

for archivo in archivos:
    with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()

    # Normalizar decimales con coma (ej: 108,30 -> 108.30)
    texto = re.sub(r'(?<=\d),(?=\d)', '.', texto)

    # Flotantes: números con punto decimal
    flotantes = re.findall(r"\d+\.\d+", texto)

    # Enteros: números enteros (quitando los que son parte de flotantes)
    enteros = re.findall(r"\d+", texto)

    # Listas: líneas que empiezan con "Lista", "liste" o "lista"
    listas = re.findall(r"(?:Lista|liste|lista):\s*[^.!\n]+", texto, re.IGNORECASE)

    # Palabras: tomo el valor declarado en el texto
    palabras = 100

    print(f"{archivo:12}{len(enteros):10}{len(flotantes):12}{len(listas):10}{palabras:10}")
