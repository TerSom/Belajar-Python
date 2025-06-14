# operasi dan manipulasi string

# menyambung string atau (concatenate)
namaPertama = "Kelas"
namaKedua = "W"
namaKetiga = "Prambowo"

namaLengkap = namaPertama + " " + namaKedua + "'" + namaKetiga
print(namaLengkap)

# menghitung panjang string
panjangNama = len(namaLengkap)
print("panjang dari", namaLengkap + " " +str(panjangNama))

# operator untuk string

P = "P"
status = P in namaLengkap
print("apakah hurup", P ,"ada di", namaLengkap + " " +str(status))

p = "p"
status = p in namaLengkap
print("apakah hurup", p ,"ada di", namaLengkap + " " +str(status))

P = "P"
status = P not in namaLengkap
print("apakah hurup", P ,"ada di", namaLengkap + " " +str(status))

# mengulang string
print(20*"wk")
print("wk"*20)

# indexing
print("index ke o adalah", namaLengkap[0])
print("index ke 2 adalah", namaLengkap[2])
print("index ke 6 adalah", namaLengkap[6])
print("index ke 0:4 adalah", namaLengkap[0:5])


print("huruf terkecil adalah", min(namaLengkap))
print("huruf terkecil adalah", max(namaLengkap))


asciidCode = ord(" ")
print(asciidCode)
asciidCode = ord("w")
print(asciidCode)

# operator dalam bentuk methon
data = "darman manawan merana amanah aman menawan"
jumlah = data.count("m")
print(str(jumlah))