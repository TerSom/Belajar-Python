count = 0
sisi = 10

# # menggunakan for
for i in range(sisi):
    count += 1
    print("*"*count)


# menggunakan while
count = 0
while True:
    count += 1 
    print("*"*count)
    if count == 5:
        break

# menggunakan while genap saja
count = 1
while True:
    if count%2:
        count += 1
        continue
    print("*"*count)
    count += 1
    if count > sisi:
        break

# menggunakan while ganjil saja
count = 1
while True:
    if count%2:
        print("*"*count)
        count += 1
    else:
        count += 1
        continue
    
    if count > sisi:
        break


# menggunakan while ganjil membuat segitiga
count = 1
spasi = int(sisi/2)

while True:
    if count%2:
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break

# # membuat segitiga

count = 1
spasi = int(sisi/2)

while True:
    print(" "*spasi,"*"*count)
    spasi -= 1
    count += 2
    if count > sisi:
        break
