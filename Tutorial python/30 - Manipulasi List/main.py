# operasi untuk list

data = ["umay","somay",'ilham']
print(data)

# memilih data dalam list
dataPertama = data[0]
print(dataPertama)

dataAkhir = data[-1]
print(dataAkhir)

# mencari panjang dalam list
dataPanjang = len(data)
print(f"panjang data adalah {dataPanjang}")

# menambah data dalam list

data.insert(1,"asep")
print(data)

data.append("darman")
print(data)

listNamaBaru = ["mie ayam","esteh",'daraman']
data.extend(listNamaBaru)
print(data)

# merubah data list
data[2] = "somayenak"
print(data)

# menghapus atau meremove data

data.remove('darman')
print(data)

data.pop()
print(data)

dataAkhir = data.pop()
print(dataAkhir)

