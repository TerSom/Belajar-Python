angkaList = [1,4,5,7,8,4,]

# for loop
for angka in angkaList:
    print(f"angka {angka}")

namaList = ['umay','gg','dadang']

for nama in namaList:
    print(f"nama {nama}")


# for loop range
angkaList = [1,4,5,7,8,4,]

panjangList = len(angkaList)

for angka in range(panjangList):
    print(f"angka {angka}")


# menggunakan while
angkaList = [1,4,5,7,8,4,]

panjangList = len(angkaList)

while angka > panjangList:
    print(f"angka {angkaList[angka]}")

# list comprehesion

data = ['nanang',242,'ucup']
[print(f"data {i}") for i in data]

dataAngka = [2,3,5,2]

pangkatDataAngka = [i**2 for i in dataAngka]
print(pangkatDataAngka)

# list enumerate
dataEnumerate = ['nanang',242,'ucup']
for index,data in enumerate(dataEnumerate):
    print(f"indexnya {index} datanya {data}")



