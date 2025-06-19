# operasi list

dataAngka = [1,2,5,7,9,4,6,7,8,3,6,7,3,2,3,5,6,7,8,0]
print(dataAngka)

jumlahData = dataAngka.count(6)
print(f"jumlah angka 6 ada {jumlahData}")
jumlahData = dataAngka.count(2)
print(f"jumlah angka 2 ada {jumlahData}")

data = ['umay','somay','daraman','gg']
print(data)

dataIndex = data.index("somay")
print(f"index somay ada ke {dataIndex}")

dataIndex = data.index("gg")
print(f"index somay ada ke {dataIndex}")

data.sort()
print(f"data di urut akan menjadi {data}")

dataAngka.sort()
print(f"dataAngka di urut akan menjadi {dataAngka}")

data.reverse()
print(data)

dataAngka.reverse()
print(dataAngka)