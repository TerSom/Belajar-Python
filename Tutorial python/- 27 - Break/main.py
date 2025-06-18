# break

# break pertama

angka = 0

while angka < 5:
    angka+= 1
    print("gg")
    if angka == 3:
        break
    print("nooo")
print("selesai")

# break kedua 

angka_input = int(input("masukan angka "))

while True:
    angka+= 1
    print(f"kelas gg ke {angka}")
    if angka == angka_input:
        break
    print("gg")
print("selesai")