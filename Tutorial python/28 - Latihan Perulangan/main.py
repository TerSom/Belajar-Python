sisi = 10

# Menggunakan for
print("=== Menggunakan for ===")
count = 0
for i in range(sisi):
    count += 1
    print("*" * count)

# Menggunakan while
print("\n=== Menggunakan while ===")
count = 0
while True:
    count += 1
    print("*" * count)
    if count == 5:
        break

# Menggunakan while genap saja
print("\n=== Menggunakan while genap saja ===")
count = 1
while True:
    if count % 2:
        count += 1
        continue
    print("*" * count)
    count += 1
    if count > sisi:
        break

# Menggunakan while ganjil saja
print("\n=== Menggunakan while ganjil saja ===")
count = 1
while True:
    if count % 2:
        print("*" * count)
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break

# Menggunakan while ganjil membuat segitiga
print("\n=== Menggunakan while ganjil membuat segitiga ===")
count = 1
spasi = int(sisi / 2)
while True:
    if count % 2:
        print(" " * spasi, "*" * count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break

# Membuat segitiga
print("\n=== Membuat segitiga ===")
count = 1
spasi = int(sisi / 2)
while True:
    print(" " * spasi, "*" * count)
    spasi -= 1
    count += 2
    if count > sisi:
        break

# Membuat ketupat
print("\n=== Membuat ketupat ===")
sisi = 5

# Bagian atas ketupat
for i in range(1, sisi + 1):
    print(" " * (sisi - i), end = "")
    print("* " * i)

# Bagian bawah ketupat
for i in range(sisi - 1, 0, -1):
    print(" " * (sisi - i), end = "")
    print("* " * i)
