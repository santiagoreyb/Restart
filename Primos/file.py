import os

primos = []
for num in range(2, 251):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(str(num))

with open("results.txt", "w") as archivo:
    archivo.write(", ".join(primos))


ruta_completa = os.path.abspath("results.txt")
print(f"Archivo guardado en: {ruta_completa}")
print("Contenido del archivo:", primos)
