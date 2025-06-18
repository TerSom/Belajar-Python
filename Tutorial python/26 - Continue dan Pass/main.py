# belajar tentang continue break pass

# pass itu dummy atau tidka di esekusi

angka = 0

while angka < 5:
    angka+= 1
    print(f"angka sekarang ke {angka}")
    if angka == 3:
        pass #ini tidak akan di esekusi

    print("adam")

print("finish")

# continue aadalah akan membuat loop meloncat ke step selanjutnya contohnya


while angka < 5:
    angka+= 1
    print(f"angka sekarang ke {angka}")
    if angka == 3:
        print("gg gaming")
        continue
    print("adam")

print("finish")