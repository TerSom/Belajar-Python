nama_global = "darman"

# akses global scope fungsi
def nama():
    print(f"nama {nama_global}")
    
nama()

# akses global scope percabangan
if True:
    print(f"nama {nama_global}")


# akses global scope dalam loop
for i in range(1,5):
    print(f"nama {i} - {nama_global}")



# variabel local scop

def namaLocal():
    nama = "asep" # <- = variabel local scop

namaLocal() 
# print(nama) tidak bisa di lakukan

# contoh penggnaan

def fungsi():
    print(f"nama{nama}")

nama = 'otong'
fungsi()

# contoh merubah variabel local menjadi global
angka = 1
nama = "umay"

def fungsi2(nilaiBaru,namaBaru):
    global angka 
    global nama
    angka = nilaiBaru
    nama = namaBaru
    

print(f"sebelum {nama,angka}")
fungsi2(5,'darman')
print(f"sesudah{angka,nama}")