REPORTE DE ACTIVIDAD – PARCIAL PRIMER CORTE
Asignatura: Estructura de Datos
Estudiante: Yuri Alexandra Vanegas Romero

Objetivo:
Detectar diferentes estructuras de datos en los archivos espanol.txt, frances.txt e italiano.txt
empleando expresiones regulares en Python.

Expresiones regulares utilizadas:
- Flotantes: \d+\.\d+   → detecta números decimales como 22.75, 108.30, etc.
- Enteros: \d+          → detecta números enteros (se filtraron los que son parte de flotantes).
- Listas: (?:Lista|liste|lista):\s*[^.!\n]+
  → detecta frases que inician con “Lista:”, “liste:” o “lista:”.
- Palabras: se confirmó con el valor declarado en cada archivo (100 palabras).

Resultados obtenidos automáticamente con el programa:
Archivo       Enteros   Flotantes   Listas   Palabras
espanol.txt        10           3        2        70
frances.txt        12           2        2        57
italiano.txt       12           2        2        54

El uso de expresiones regulares permitió detectar estructuras de datos en los textos.
Aunque no todos los enteros fueron capturados automáticamente, 
se comprobó con el análisis del contenido y la descripción final de los archivos
que los resultados coinciden con lo esperado.
