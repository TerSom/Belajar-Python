def pangkat(angka):
    quadrat = angka ** 2
    return quadrat

a = pangkat(5)
print(f"hasil dari 5 kuadrat = {a}")
print(pangkat(10))
z = 10 +  pangkat(5)
print(f"hasil dari z adalah {z}")


def fungsiTambah(angka1, angka2):
    return angka1 + angka2

F = fungsiTambah(10,20)
print(f"hasil dari fungsiTambah(10,20) = {F}")

def operasiMatematika(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah,kurang,kali,bagi

t,k,ka,b = operasiMatematika(10,5)
print(f"hasil dari oeprasi matematika(10,5) = {t}")
print(f"hasil dari oeprasi matematika(10,5) = {k}")
print(f"hasil dari oeprasi matematika(10,5) = {ka}")
print(f"hasil dari oeprasi matematika(10,5) = {b}")


# hasilnya akan None karena fungsi tidak mengembalikan nilai

# def tambahgg(angka1,angka2):
#     hasil = angka1 + angka2
    
# a = tambahgg(10,20)
# print(f"hasil dari tambahgg(10,20) = {a}")