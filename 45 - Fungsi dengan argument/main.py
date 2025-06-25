def Hello(nama):
    print(f"Halo {nama} selamat datang di fungsi Hello")
    print("Selamat Datang di Pengenalan Fungsi")
    
Hello("Terry")

def tambah(angka1,angka2):
    hasil = angka1 + angka2
    print(f"hasil dari {angka1} + {angka2} = {hasil}")
    
tambah(5,10)

def sayHi(listPeserta):
    dataPeserta = listPeserta.copy()
    for peserta in dataPeserta:
        print(f"Halo {peserta}, selamat datang")
namaPeserta = ['Terry','Budi','Siti','Joko']
sayHi(namaPeserta)