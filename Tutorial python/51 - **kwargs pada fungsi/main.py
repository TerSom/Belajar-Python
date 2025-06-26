# belajar tentang kegunaan **kwargs pada fungsi

def fungsi(**kwargs):
    nama = kwargs['nama']
    umur = kwargs['umur']
    tinggi = kwargs['tinggi']
    print(f"Nama: {nama}, Umur: {umur}, Tinggi: {tinggi} cm")


fungsi(nama="Terry", umur=17, tinggi=180)


# studi kasus penggunaan **kwargs pada fungsi

def math(*args,**kwargs):
    hasil = 0
    if kwargs['option'] == "tambah":
        for angka in args:
            hasil += angka
    elif kwargs['option'] == "kali":
        hasil = 1
        for angka in args:
            hasil *= angka
    else:
        print("angka tidak ada")
    return hasil 


hasil = math(1, 2, 3, 4, 5, option ="tambah")
print(f"Hasil dari fungsi tambah adalah: {hasil}")
hasil = math(1, 2, 3, 4, 5, option ="kali")
print(f"Hasil dari fungsi kali adalah: {hasil}")