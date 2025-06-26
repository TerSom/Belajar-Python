# penggunaan type hints pada fungsi

def nama(argumen:int) -> int:
    hasil = 10**argumen
    return hasil

HASIL = nama(2)
print(f"Hasil dari fungsi nama adalah: {HASIL}")
