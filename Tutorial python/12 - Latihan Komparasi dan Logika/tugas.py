# tugas pertama

# -----0+++++5-----8+++++11------

inputAngka = float(input("masukan angka lebih dari 0 atau kurang dari 5 atau lebih dari 8 atau kurang dari 11 \n ="))

lebihDariNol = inputAngka > 0
kurangDariLima = inputAngka < 5
# -----0+++++5-----
kondisiPertama = lebihDariNol and kurangDariLima


lebihDariDelapan = inputAngka > 8
kurangDariSebelas = inputAngka < 11
# -----8+++++11------
kondisiKedua = lebihDariDelapan and kurangDariSebelas


iscorect = kondisiPertama or kondisiKedua
print(iscorect)


# tugas kedua

# +++++0----5++++++8-----11+++++

inputAngka = float(input("masukan angka kurang dari 0 atau lebih dari 5 atau kurang dari 8 atau lebih dari 11 \n ="))

kurangdariNol = inputAngka < 0
lebihdariLima = inputAngka > 5
# +++++0----5++++++
kondisiPertama = kurangdariNol or lebihdariLima

kurangdariDelapan = inputAngka < 8
lebihdariSebelas = inputAngka > 11
# ++++++8-----11+++++
kondisiKedua = kurangdariDelapan or lebihdariSebelas

iscorect = kondisiPertama and kondisiKedua
print(iscorect)


