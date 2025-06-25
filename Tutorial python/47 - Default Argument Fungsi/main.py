def nama(nama = "kamu"):
    print(f"Halo {nama}, selamat datang di fungsi nama")

nama("terry")
nama()

def peserta(nama,peserta = 1):
    print(f"Halo {nama}, selamat datang di fungsi peserta")
    print(f"peserta = {peserta}")
    
peserta("Terry", 2)
peserta("Terry")

def hitung(angka1,angka2 = 10):
    hasil = angka1 + angka2
    print(f"hasil dari {angka1} + {angka2} = {hasil}")
    
hitung(5)
hitung(angka2=20,angka1=10) #ini juga bisa di balikkan urutannya

def hitung2(angka1=10,angka2=10,angka3=10,angka4=10,angka5=10):
    hasil = angka1 + angka2 + angka3 + angka4 + angka5
    print(f"hasil dari {angka1} + {angka2} + {angka3} + {angka4} + {angka5} = {hasil}")
    
hitung2(angka4=60)
# hitung2(,,,) # ini akan error karena gk bisa melewati parameter yang tidak diisi
