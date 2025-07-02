# data = int(input("masukan angka : "))
# hasil = 0

# try:
#     hasil = 10/data
# except:
#     print(f"input tidak boleh 0")
    
# print(f"hasilnya adalah {hasil}")

# contoh diaplikasi

while(True):
    angka = int(input("masukan angka : "))
    hasil = 0

    try:
        hasil = 10/angka
        print(f"hasil angka adalah {hasil}")
        isDone = input("lanjut? (y/n)")
        if isDone == "n":
            break
    except:
        print("angka tidak boleh 0")

print("program satu selesai")