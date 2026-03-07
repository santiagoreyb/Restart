# hemoglobin_analysis.py
# Análisis de la secuencia de proteína de la hemoglobina beta humana
# Fuente: UniProt P68871 / NCBI NP_000510.1
# Ejercicios 3-9: análisis de secuencia, composición, peso molecular y más

import json

# ─────────────────────────────────────────────
# Ejercicio 2 ─ Cargar la secuencia limpia
# ─────────────────────────────────────────────
with open("/workspaces/Restart/Hemoglobina/hemoglobin_clean.txt", "r") as f:
    sequence = f.read().strip()

# ─────────────────────────────────────────────
# Ejercicio 4 ─ Información general
# ─────────────────────────────────────────────
protein_name = "Hemoglobin subunit beta [Homo sapiens]"

print("=" * 55)
print("  ANÁLISIS DE HEMOGLOBINA BETA HUMANA")
print("=" * 55)
print(f"Proteína  : {protein_name}")
print(f"Longitud  : {len(sequence)} aminoácidos")
print(f"Secuencia : {sequence[:30]}...")
print()

# ─────────────────────────────────────────────
# Ejercicio 5 ─ Composición de aminoácidos
# ─────────────────────────────────────────────
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

print("─" * 55)
print("COMPOSICIÓN DE AMINOÁCIDOS")
print("─" * 55)

amino_count = {}
for aa in amino_acids:
    amino_count[aa] = sequence.count(aa)

# Mostrar en columnas ordenadas por frecuencia
for aa, count in sorted(amino_count.items(), key=lambda x: -x[1]):
    bar = "█" * count
    print(f"  {aa}: {count:>3}  {bar}")
print()

# ─────────────────────────────────────────────
# Ejercicio 6 ─ Peso molecular (diccionario)
# ─────────────────────────────────────────────
mw_table = {
    "A": 89.09,  "C": 121.16, "D": 133.10, "E": 147.13,
    "F": 165.19, "G":  75.03, "H": 155.16, "I": 131.17,
    "K": 146.19, "L": 131.17, "M": 149.21, "N": 132.12,
    "P": 115.13, "Q": 146.15, "R": 174.20, "S": 105.09,
    "T": 119.12, "V": 117.15, "W": 204.23, "Y": 181.19,
}

# ─────────────────────────────────────────────
# Ejercicio 7 ─ Función reutilizable
# ─────────────────────────────────────────────
def calculate_molecular_weight(seq: str) -> float:
    """
    Calcula el peso molecular aproximado de una secuencia
    de aminoácidos (en Daltons).
    Se resta agua (18.02 Da) por cada enlace peptídico formado.
    """
    water = 18.02
    raw_weight = sum(mw_table.get(aa, 0) for aa in seq)
    # Se restan (n-1) moléculas de agua por los enlaces peptídicos
    molecular_weight = raw_weight - (len(seq) - 1) * water
    return round(molecular_weight, 2)


mol_weight = calculate_molecular_weight(sequence)

print("─" * 55)
print("PESO MOLECULAR")
print("─" * 55)
print(f"  Peso molecular calculado: {mol_weight:,.2f} Da")
print(f"  Peso molecular calculado: {mol_weight/1000:,.2f} kDa")
print()

# ─────────────────────────────────────────────
# Ejercicio 9 ─ Aminoácidos hidrofóbicos
# ─────────────────────────────────────────────
hydrophobic = list("AVILMFWY")

hydrophobic_count = sum(sequence.count(aa) for aa in hydrophobic)
hydrophobic_pct   = round((hydrophobic_count / len(sequence)) * 100, 2)

print("─" * 55)
print("AMINOÁCIDOS HIDROFÓBICOS  (A, V, I, L, M, F, W, Y)")
print("─" * 55)
print(f"  Cantidad  : {hydrophobic_count}")
print(f"  Porcentaje: {hydrophobic_pct}%")
print()

# ─────────────────────────────────────────────
# Ejercicio 8 ─ Guardar resultados en JSON
# ─────────────────────────────────────────────
results = {
    "protein_name"      : protein_name,
    "sequence_length"   : len(sequence),
    "amino_acid_count"  : amino_count,
    "molecular_weight_Da": mol_weight,
    "hydrophobic_count" : hydrophobic_count,
    "hydrophobic_percent": hydrophobic_pct,
}

with open("/workspaces/Restart/Hemoglobina/hemoglobin_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print("─" * 55)
print("✔  Resultados guardados en: hemoglobin_results.json")
print("=" * 55)