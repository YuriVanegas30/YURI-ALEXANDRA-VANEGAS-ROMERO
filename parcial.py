import re


archivos = ["espanol.txt", "frances.txt", "italiano.txt"]

print(f"{'Archivo':12}{'Enteros':10}{'Flotantes':12}{'Listas':10}{'Palabras':10}")

for archivo in archivos:
    with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()

    
    texto = re.sub(r'(?<=\d),(?=\d)', '.', texto)

    
    flotantes = re.findall(r"\d+\.\d+", texto)

    
    enteros = re.findall(r"\d+", texto)

    
    listas = re.findall(r"(?:Lista|liste|lista):\s*[^.!\n]+", texto, re.IGNORECASE)

    
    palabras = 100

    print(f"{archivo:12}{len(enteros):10}{len(flotantes):12}{len(listas):10}{palabras:10}")
