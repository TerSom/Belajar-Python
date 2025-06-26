# belajar tentang kegunaan *args pada fungsi

def nama(nama,umur,tinggi):
    hasil = nama + " berumur " + str(umur) + " tahun dan tinggi " + str(tinggi) + " cm"
    return hasil

print(nama("terry",17,180))

def listNama(ListArgumen):
    data = ListArgumen.copy()
    nama = data[0]
    umur = data[1]
    tinggi = data[2]
    print(f"nama: {nama} berumur {umur} tahun dan tinggi {tinggi} cm")
    return data

listNama(["terry",17,180])

def listNama2(*args):
    nama = args[0]
    umur = args[1]
    tinggi = args[2]
    print(f"nama: {nama} berumur {umur} tahun dan tinggi {tinggi} cm")
    
listNama2("terry",17,180)

# studi kasus penggunaan *args pada fungsi

def tambah(*jumlah:int) -> int:
    hasil = 0
    for i in jumlah:
        hasil += i
    return hasil

print(f"hasil dari tambah adalah {tambah(10,20,30)}")
print(f"hasil dari tambah adalah {tambah(1,2,3,4,5,67,7,8,9)}")