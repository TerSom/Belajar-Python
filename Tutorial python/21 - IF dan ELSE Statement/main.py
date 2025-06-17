# belajar tentang penkondisian if dan else

# 1.else inline
nama = input("masukan nama kamu = ")

if nama=="agus":print(f"nice {nama}")
print("program selesai")

# 2.program if indentation
if nama=="agus":
    print(f"nice {nama}")
    print(f"kelas dah {nama}")
print("program selesai")

# 3.else statment
if nama=="agus":
    print(f"ggg gaming {nama}")
else:
    print(f"lu siapa bro")
print(f"program selesai {nama}")

# kalkulator dengan 1 operator dengan if else
angka1 = float(input("masukan angka bro ke 1 = "))
operator = input("masukan operatro + = ")
angka2 = float(input("masukan angka ke 2 = "))

if operator == "+":
    print(angka1 + angka2)
else:
    print("masukan operator tambah bro")